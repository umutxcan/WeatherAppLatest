 Hava Durumu Uygulaması (Flask + Docker + Jenkins)
Bu proje, Flask kullanılarak geliştirilmiş basit bir hava durumu uygulamasıdır. Uygulama, bir şehir adı girildiğinde o şehre ait hava durumu ve nem bilgisini sunar. Proje Docker ile containerize edilmiştir ve Jenkins ile otomatik deployment süreci kontrol edilmektedir.

📦 İçerik
Dockerfile: Flask tabanlı web sunucusu imajı oluşturur.

requirements.txt: Gerekli Python paketlerini listeler.

app.py: Web uygulamasının ana dosyasıdır.

Jenkinsfile: CI/CD işlemleri için Jenkins pipeline tanımıdır (isteğe bağlı).

✅ Gereksinimler
Docker

Jenkins (Deployment için)

(Opsiyonel) VS Code + Docker eklentisi

🚀 Kurulum Adımları
1. Reposityo Klonlayın
bash
Copy
Edit
git clone https://github.com/kullanici-adiniz/hava-durumu-uygulamasi.git
cd hava-durumu-uygulamasi
2. Docker İmajını Oluşturun
bash
Copy
Edit
docker build -t weatherapp-image .
3. Container’ı Başlatın
bash
Copy
Edit
docker run -d -p 5000:5000 --name weatherapp-container weatherapp-image
Jenkins kullanıyorsanız, build ve deploy adımlarınızı otomatik hale getirebilirsiniz. Jenkinsfile içeriğine göre pipeline işlemleri yürütülür.

🌍 Uygulamaya Erişim
Uygulama başarıyla çalıştıktan sonra şu adreslerden erişebilirsiniz:

İsminizi döndürmek için:

arduino
Copy
Edit
http://localhost:5000
Hava durumu verisi almak için (örneğin İstanbul):

bash
Copy
Edit
http://localhost:5000/weather?city=istanbul
Bu endpoint; şehrin adını, sıcaklığı ve nem oranını JSON formatında döndürür.

🐳 Durdurma ve Temizleme
Container’ı durdurmak için:

bash
Copy
Edit
docker stop weatherapp-container
docker rm weatherapp-container
Yeniden kurulum yapmak isterseniz:

bash
Copy
Edit
docker build -t weatherapp-image .
docker run -d -p 5000:5000 --name weatherapp-container weatherapp-image
🛠 Notlar
app.py içinde app.run(host="0.0.0.0", port=5000) satırı yer almalıdır ki uygulama dışarıdan erişilebilir olsun.

Hava durumu verisi büyük ihtimalle bir API kullanılarak alınıyordur, örneğin OpenWeatherMap. API anahtarınız varsa .env dosyasında gizli tutmayı unutmayın.
