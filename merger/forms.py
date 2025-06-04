from django import forms

class PDFUploadForm(forms.Form):
    file = forms.FileField(label="PDF Dosyası Yükleyin", required=True)
