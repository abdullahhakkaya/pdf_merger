import fitz
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .forms import PDFUploadForm
import uuid
import os
import time
from pathlib import Path

def cleanup_old_files():
    # Cleanup files older than 1 hour
    current_time = time.time()
    one_hour = 60 * 60
    
    # Cleanup uploaded files
    uploads_dir = Path(settings.MEDIA_ROOT) / 'uploads'
    if uploads_dir.exists():
        for file in uploads_dir.glob('*.pdf'):
            if current_time - file.stat().st_mtime > one_hour:
                try:
                    file.unlink()
                except:
                    pass

    # Cleanup merged files
    for file in Path(settings.MEDIA_ROOT).glob('merged_*.pdf'):
        if current_time - file.stat().st_mtime > one_hour:
            try:
                file.unlink()
            except:
                pass

def merge_half_pages(file_path):
    try:
        doc = fitz.open(file_path)
        new_doc = fitz.open()

        for i in range(0, len(doc), 2):
            if i + 1 < len(doc):
                top = doc[i]
                bottom = doc[i+1]
                width = top.rect.width
                height = top.rect.height + bottom.rect.height
                new_page = new_doc.new_page(width=width, height=height)
                new_page.show_pdf_page(fitz.Rect(0, 0, width, top.rect.height), doc, i)
                new_page.show_pdf_page(fitz.Rect(0, top.rect.height, width, height), doc, i+1)
            else:
                new_doc.insert_pdf(doc, from_page=i, to_page=i)

        out_path = f"media/merged_{uuid.uuid4().hex}.pdf"
        new_doc.save(out_path)
        
        # Delete the input file after processing
        try:
            os.remove(file_path)
        except:
            pass
            
        return "/" + out_path  # Relative URL for download
    except Exception as e:
        raise Exception(f"PDF işlenirken bir hata oluştu: {str(e)}")
    finally:
        if 'doc' in locals():
            doc.close()
        if 'new_doc' in locals():
            new_doc.close()

def index(request):
    # Run cleanup on each request
    cleanup_old_files()
    
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            # Validate file size (max 50MB)
            if uploaded_file.size > 50 * 1024 * 1024:
                return render(request, 'merger/index.html', {
                    'form': form,
                    'error': 'Dosya boyutu 50MB\'dan küçük olmalıdır.'
                })
                
            # Validate file type
            if not uploaded_file.name.lower().endswith('.pdf'):
                return render(request, 'merger/index.html', {
                    'form': form,
                    'error': 'Lütfen sadece PDF dosyası yükleyin.'
                })
            
            try:
                file_path = default_storage.save(f"uploads/{uploaded_file.name}", uploaded_file)
                full_path = default_storage.path(file_path)
                merged_pdf_url = merge_half_pages(full_path)
                
                return render(request, 'merger/index.html', {
                    'form': form,
                    'merged_pdf_url': merged_pdf_url
                })
            except Exception as e:
                return render(request, 'merger/index.html', {
                    'form': form,
                    'error': str(e)
                })
    else:
        form = PDFUploadForm()
    
    return render(request, 'merger/index.html', {'form': form})
