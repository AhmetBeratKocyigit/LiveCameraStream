# 📷 Live Camera Stream with Flask

Bu proje, Flask ve OpenCV kullanarak bilgisayar kamerasından canlı görüntü akışı sağlar. Akış, HTML sayfası üzerinden anlık olarak görüntülenebilir. Basit bir web arayüzü ile canlı video izlenmesini sağlar.

## 🚀 Özellikler

- Gerçek zamanlı kamera görüntüsü aktarımı  
- Flask ile hızlı ve kolay kurulum  
- CORS desteği sayesinde farklı istemcilerden erişim  
- HTML üzerinden kolay görüntüleme  

## 🛠 Gereksinimler

- Python 3.x  
- OpenCV (`cv2`)  
- Flask  
- flask-cors  

Kurulum için aşağıdaki komutu çalıştırabilirsiniz

```bash
pip install flask opencv-python flask-cors
```

## ▶️ Kullanım

1. Flask Sunucusunu Başlatın

```bash
python camera.py
```
Sunucu çalıştıktan sonra aynı bilgisayar içinde, http127.0.0.18000video adresinden canlı video akışına ulaşabilirsiniz.

## 🌐 Uzak Erişim

Başka bir cihazdan canlı görüntüyü izlemek isterseniz, `127.0.0.1` yerine bilgisayarınızın yerel IP adresini kullanın.

### 💡 IP Adresinizi Nasıl Bulabilirsiniz

Windows sistemlerde IP adresinizi öğrenmek için

1. `Başlat` menüsüne tıklayın ve `cmd` yazarak Komut İstemi'ni açın.
2. Aşağıdaki komutu yazın ve Enter'a basın

```bash
ipconfig
```

3. Açılan listede IPv4 Address veya IPv4 Adresi satırını bulun (genellikle 192.168.x.x veya 10.x.x.x formatındadır).
Örnek çıktı
```nginx
IPv4 Adresi. . . . . . . . . . .  192.148.4.25
```
HTML dosyanızdaki img etiketi içindeki URL’yi aşağıdaki gibi değiştirin
```html
img src=http192.148.4.258000video
```
> ⚠️ IP adresiniz zaman zaman değişebilir. Aynı ağa bağlı cihazlardan erişim için doğru IP’yi kontrol ettiğinizden emin olun.
