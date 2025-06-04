# 📄 PDF Sayfa Birleştirici (Django)

Bu proje, dikey olarak iki parçaya bölünmüş PDF sayfalarını birleştirip okunabilir tam sayfalar haline getiren bir web uygulamasıdır.

## 🚀 Özellikler

- Yarım veya bölünmüş PDF sayfalarını otomatik olarak birleştirir.
- Kolay bir HTML arayüzü ile dosya yükleyip çıktıyı indirmenizi sağlar.

## Ekran Görüntüleri

<table>
  <tr>
    <td colspan=2 ><img src="https://raw.githubusercontent.com/abdullahhakkaya/pdf_merger/main/static/images/index-1.png"/></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/abdullahhakkaya/pdf_merger/main/static/images/index-2.png"/></td>
    <td><img src="https://raw.githubusercontent.com/abdullahhakkaya/pdf_merger/main/static/images/index-3.png"/></td>
  </tr>
</table>


## Örnek PDF

<table>
  <tr>
    <td><center>Birleştirme Öncesi</center></td>
    <td><center>Birleştirme Sonrası</center></td>
  </tr>
  <tr>
    <td><img src="https://raw.githubusercontent.com/abdullahhakkaya/pdf_merger/main/static/images/pdf-1.png"/></td>
    <td><img src="https://raw.githubusercontent.com/abdullahhakkaya/pdf_merger/main/static/images/pdf-2.png"/></td>
  </tr>
</table>


## 🧰 Kurulum

### 1. Depoyu klonlayın
```bash
git clone https://github.com/abdullahhakkaya/pdf_merger.git
cd pdf_merger
```

### 2. Sanal ortam oluşturun ve etkinleştirin
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Gereksinimleri yükleyin
```bash
pip install -r requirements.txt
```
Not: 'PyMuPDF (fitz)' modülünü kullanıyoruz. Yüklenmediğinde şu komutu çalıştırın:
```bash
pip install PyMuPDF
```

### 4. Veritabanı migrasyonları
```bash
python manage.py migrate
```

### 5. Geliştirme sunucusunu başlatın
```bash
python manage.py runserver
```

### 6. Uygulamayı açın
Tarayıcınızda şu adrese gidin:
http://127.0.0.1:8000

