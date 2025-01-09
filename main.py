import os
from ultralytics import YOLO
import cv2

# Eğitilmiş modeli yükle
model = YOLO(r"C:\Users\burak\Desktop\Ağaç Proje\best.pt")

# Test görüntüsünü tahmin et
results = model.predict(source=r"C:\Users\burak\Desktop\Ağaç Proje\test1.jpeg", save=True)

# Tahmin sonuçlarını yazdır
print("Tahmin Sonuçları:")
for result in results:
    for box in result.boxes:
        cls = model.names[int(box.cls)]  # Sınıf adı
        confidence = float(box.conf)    # Güven değerini float'a dönüştür
        print(f"Tür: {cls}, Güven: {confidence:.2f}")

# `runs/detect` klasöründeki en son kaydedilen klasörü bul
detect_folder = os.path.join("runs", "detect")
latest_run = max([os.path.join(detect_folder, d) for d in os.listdir(detect_folder)], key=os.path.getctime)

# En son klasördeki tahmin edilen görüntüyü al
predicted_image_path = os.path.join(latest_run, os.listdir(latest_run)[0])  # İlk görüntüyü al
print(f"Son tahmin edilen görüntü: {predicted_image_path}")

# Kaydedilen görüntüyü yükle
predicted_image = cv2.imread(predicted_image_path)

# Görüntüyü ekranda göster
cv2.imshow("Tahmin Sonucu - En Son Kaydedilen Görüntü", predicted_image)

# Çıkış için bir tuşa basılmasını bekle
cv2.waitKey(0)
cv2.destroyAllWindows()
