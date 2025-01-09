# Ağaç Türü Sınıflandırma ve Tespit Projesi

Bu proje, **YOLOv8** (You Only Look Once) derin öğrenme modelini kullanarak ağaç türlerini tespit etmek amacıyla geliştirilmiştir. Kullanıcılar, farklı ağaç türlerinin fotoğraflarını yükleyebilir ve bu model, fotoğraflardaki ağaç türlerini doğru bir şekilde tanımlayıp sınır kutuları ile görselleştirebilir. Model, kullanıcıya tahmin edilen türlerin isimlerini ve güven skorlarını sunar.

## Özellikler:
- **Ağaç Türü Tespiti:** Eğitimli model, görüntülerdeki ağaç türlerini (örneğin, meşe, çam, vs.) doğru bir şekilde tespit eder.
- **YOLOv8 Kullanımı:** Model, **YOLOv8** (You Only Look Once) nesne tespit algoritmasıyla eğitilmiş olup, hızlı ve yüksek doğrulukla nesne tespiti yapar.
- **Sonuç Görselleştirme:** Tespit edilen ağaç türleri ve güven skorları ekranda görüntülenir, ayrıca sonuçlar kaydedilir.
- **Python ve OpenCV Kullanımı:** Proje, Python programlama dili ve OpenCV kütüphanesi kullanılarak geliştirilmiştir.

## Kurulum:
Bu projeyi çalıştırabilmek için aşağıdaki adımları takip edebilirsiniz.

### Gerekli Kütüphaneler:
- `torch`
- `opencv-python`
- `matplotlib`
- `ultralytics`
