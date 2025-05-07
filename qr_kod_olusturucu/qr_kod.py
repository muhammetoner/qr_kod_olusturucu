import tkinter as tk
from tkinter import filedialog  # Bilgisayarın neresine kaydetmek istediğimizi sorgulayacak olan kütüphane
import pyqrcode
from pyqrcode import QRCode

# Temel metodlar
def qr_kodu_olustur():
    url = url_girdi.get()  # Kullanıcının girdiği URL'yi alıyoruz
    if url:
        qr_url = pyqrcode.create(url)  # QR kod görüntüsünü oluşturmak için .create()
        
        # Dosyayı nereye kaydetmek istediğimizi sorgulayan metod .asksaveasfilename()
        dosya_yolu = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG Dosyaları", "*.svg")])  
        if dosya_yolu:
            qr_url.svg(dosya_yolu, scale=8)  # Doğrudan dosya yolu veriyoruz
            
            durumEtiketi.config(text="QR Kodu Oluşturuldu ve Kaydedildi", fg="green")  # Başarı mesajı
        else:
            durumEtiketi.config(text="Kaydetme işlemi iptal edildi", fg="red")  # Kullanıcı iptal ederse hata mesajı
    else:
        durumEtiketi.config(text="Lütfen bir URL girin!", fg="red")  # Kullanıcı URL girmezse uyarı ver

# Arayüz Tasarımı
uygulma_pencere = tk.Tk()  # Tkinter ana pencereyi oluşturma
uygulma_pencere.title("QR Kod Oluşturucu")  # Pencere başlığını ayarla
uygulma_pencere.geometry("400x200")  # Pencere boyutunu belirleme

# Kullanıcıdan giriş almak için label ve entry oluşturuyoruz
etiket = tk.Label(uygulma_pencere, text="URL'yi Giriniz: ")  # Kullanıcıya bilgi veren etiket
url_girdi = tk.Entry(uygulma_pencere, width=40)  # Kullanıcının URL gireceği giriş kutusu

# Buton ve Durum Etiketi
qrKodOlusturButonu = tk.Button(uygulma_pencere, text="QR Kodu Oluştur", command=qr_kodu_olustur)  # Buton oluşturuyoruz
durumEtiketi = tk.Label(uygulma_pencere, text="", fg="black")  # QR kodunun durumunu bildiren etiket

# Yerleşim (Grid Sistemi ile)
etiket.grid(row=0, column=0, padx=10, pady=10)  # Etiketi pencereye yerleştir
url_girdi.grid(row=0, column=1, padx=10, pady=10)  # URL giriş kutusunu yerleştir
qrKodOlusturButonu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Butonu yerleştir
durumEtiketi.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  # Durum mesajını gösterecek etiketi yerleştir

# Uygulamayı Başlat
uygulma_pencere.mainloop()  # Tkinter döngüsünü başlat

