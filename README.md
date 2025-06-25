# Trinity Math Scene - Manim Animasyon Projesi

Bu proje, [Manim](https://github.com/ManimCommunity/manim) kütüphanesi kullanılarak oluşturulmuş matematiksel ve teolojik kavramları görselleştiren bir animasyon projesidir. Üçlü birlik (Trinity) kavramını matematiksel modeller ve görsel animasyonlarla açıklamaktadır.

## İçerik

- **Matematiksel Modeller**: Üçlü birlik kavramının matematiksel temsilleri
- **3D Görselleştirmeler**: Vektör analizi ve geometrik modeller
- **Teolojik Referanslar**: Kutsal Kitap'tan alıntılar ve açıklamalar
- **Animasyonlar**: Akıcı geçişler ve dinamik görsel efektler

## Demo

Projenin çalışan halini görmek için `TrinityMathScene.mp4` dosyasını inceleyebilirsiniz.

## Kurulum

### Gereksinimler

- Python 3.7+
- Manim Community Edition
- NumPy

### Adım Adım Kurulum

1. **Manim'i yükleyin:**
```bash
pip install manim
```

2. **Projeyi klonlayın:**
```bash
git clone https://github.com/kullaniciadi/manimm.git
cd manimm
```

3. **Animasyonu çalıştırın:**
```bash
manim -pql manim.py TrinityMathScene
```

## Kullanım

### Temel Komutlar

```bash
# Kaliteli render (önerilen)
manim -pqh manim.py TrinityMathScene

# Hızlı önizleme
manim -pql manim.py TrinityMathScene

# Sadece render (otomatik oynatma yok)
manim -qh manim.py TrinityMathScene
```

### Parametreler

- `-p`: Render sonrası otomatik oynatma
- `-q`: Kalite seviyesi (l=low, m=medium, h=high, k=4k)
- `-s`: Belirli bir sahneyi render et

## Özellikler

### Görsel Efektler
- **Gölge Efektleri**: `add_shadow()` fonksiyonu ile 3D görünüm
- **Glow Efektleri**: Matematiksel ifadelerde parıltı efektleri
- **3D Kamera Hareketleri**: Dinamik açı değişimleri
- **Vektör Animasyonları**: 3D uzayda vektör gösterimleri

### Matematiksel Modeller
- **Küme Teorisi**: `T = {Baba, Oğul, Kutsal Ruh}`
- **Vektör Analizi**: Üç vektörün toplamı
- **Euler Formülü**: `e^(ix) = cos(x) + i*sin(x)`
- **Ousia/Hipostaz**: `|Ousia| = 1, |Hipostaz| = 3`

### Teolojik İçerik
- Yasa 6:4 - "Tanrımız RAB, tek RAB'dir!"
- 1. Yuhanna 5:7 - Üç tanık
- 2. Korintliler 13:14 - Kapanış duası

## Özelleştirme

### Font Değişikliği
```python
FONT = "EB Garamond"  # Farklı font kullanabilirsiniz
```

### Renk Teması
```python
config.background_color = BLACK  # Arka plan rengi
# Renk paletini değiştirebilirsiniz
```

### Animasyon Süreleri
```python
self.wait(duration)  # Bekleme sürelerini ayarlayabilirsiniz
```

## Dosya Yapısı

```
manimm/
├── manim.py                 # Ana animasyon dosyası
├── TrinityMathScene.mp4     # Render edilmiş video
└── README.md               # Bu dosya
```

## Geliştirme

### Yeni Sahne Ekleme
```python
class YeniSahne(ThreeDScene):
    def construct(self):
        # Animasyon kodunuz buraya
        pass
```

### Özel Efektler
```python
def add_shadow(mobject, offset=0.05, shadow_color=GRAY):
    # Gölge efekti fonksiyonu
    pass
```

## Katkıda Bulunma

1. Bu repository'yi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## Teşekkürler

- [Manim Community](https://github.com/ManimCommunity/manim) - Animasyon kütüphanesi
- [EB Garamond](https://github.com/octaviopardo/EBGaramond12) - Font
- Matematik ve teoloji alanlarındaki araştırmacılar

## İletişim

Sorularınız veya önerileriniz için:
- GitHub Issues kullanın
- Email: [email adresiniz]

---

Bu projeyi beğendiyseniz yıldız vermeyi unutmayın! 
