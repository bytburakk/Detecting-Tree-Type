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







# Tree Species Classification and Detection Project

This project is developed to detect tree species using the **YOLOv8** (You Only Look Once) deep learning model. Users can upload images of different tree species, and the model will accurately classify the tree species in the images, visualizing them with bounding boxes. The model also provides the predicted species names and confidence scores.

## Features:
- **Tree Species Detection:** The trained model detects tree species (such as oak, pine, etc.) in images accurately.
- **YOLOv8 Usage:** The model is trained with the **YOLOv8** (You Only Look Once) object detection algorithm, which performs fast and accurate object detection.
- **Results Visualization:** Detected tree species and their confidence scores are displayed on the image, and the results are saved.
- **Python and OpenCV Usage:** The project is developed using Python programming language and OpenCV library.

## Installation:
To run this project, follow the steps below.

### Required Libraries:
- `torch`
- `opencv-python`
- `matplotlib`
- `ultralytics`

You can install the required libraries using the following command:
```bash
pip install torch opencv-python matplotlib ultralytics

