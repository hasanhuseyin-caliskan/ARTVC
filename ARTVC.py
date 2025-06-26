import os   # işletim sistemi kütüphanesini çağırdık
import time # zaman kütüphanesini çağırdık
import math # matematik kütüphanesini çağırdık
def menu(): # ana menüyü fonksiyon olarak tanımladık
    print ('ARTVC'.center(80)) # DOS işletim sistemi ekranı 80 kolon olduğu için yazıyı 80 kolona göre ortaladık
    print ('Ammo Range Time Velocity Calculator'.center(80))
    print ('Mühimmat Mesafe/Zaman/Hız Hesaplayıcı\n'.center(80))
    print ('************************'.center(80))
    print ('*   A N A  M E N Ü     *'.center(80))
    print ('************************'.center(80))
    print ('* 1. YATAY ATIŞ        *'.center(80))
    print ('* 2. EĞİK ATIŞ         *'.center(80))
    print ('* 3. DÜŞEY YUKARI ATIŞ *'.center(80))
    print ('* 4. DÜŞEY AŞAĞI ATIŞ  *'.center(80))
    print ('*                      *'.center(80))
    print ('* 0. ÇIKIŞ             *'.center(80))
    print ('************************'.center(80))
    
def yatay_atis():   # yatay atış için fonksiyon tanımladık
    os.system('cls')# OS kütüphanesiyle CLS komutunu çağırdık ve ekranı temizledik
    print ('*********************************************'.center(80))
    print ('*          Yatay atış hesaplamaları         *'.center(80))
    print ('*********************************************'.center(80))
    print ('*     Sürtünme/Rüzgar gibi dış etkenler     *'.center(80))
    print ('*         önemsiz kabul edilmiştir.         *'.center(80))
    print ('*********************************************'.center(80))
    print ('*              T A N I M L A R              *'.center(80))
    print ('*********************************************'.center(80))
    print ('* İLK HIZ : Atış hızını m/s                 *'.center(80))
    print ('* YÜKSEKLİK : Atış yüksekliğini m           *'.center(80))
    print ('*********************************************'.center(80))
    try:
        h = float(input("Yüksekliği girin (m):")) # h değişkeninine float tipinde yükseklik değerinin girilmesini istedik
        v = float(input("Başlangıç hızını girin(m/s)")) # v değişkeninine float tipinde başlangıç hızı değerinin girilmesini istedik
        g = 9.81 # g değişkeninine yer çekimi ivmesini tanımladık
        t = (2 * h / g) ** 0.5 # t değişkeninde uçuş süresini hesapladık
        x = v * t # x değişkeninde nesne konumunu hesapladık
        c = (t ** 2 + v ** 2) ** 0.5 # c değişkeninde çarpma hızını hesapladık
        print("Düşme süresi:", t)
        print("Nesnenin konumu:", x)
        print("Çarpma hızı:", c) # hesaplanan değerleri ekrana yazdırdık
        skontrol(yatay_atis) # skontrol fonksiyonunu yatay_atis parametresi ile çağırdık
        
    except:
        print('Girilen değerler geçersiz tekrar deneyiniz') # girilen değerlerde hata olması durumunda uyarı mesajı gösterdik
        time.sleep(1) # TIME kütüphanesiyle kullanıcının hata mesajını rahat okuyabilmesi için 1 saniyelik beleme süresi ekledik
        yatay_atis() # yatay_atis fonksiyonunu çağırdık

def egik_atis(): # eğik atış için fonksiyon tanımladık
    os.system('cls')
    print ('*********************************************'.center(80))
    print ('*          Eğik atış hesaplamaları          *'.center(80))
    print ('*********************************************'.center(80))
    print ('*     Sürtünme/Rüzgar gibi dış etkenler     *'.center(80))
    print ('*         önemsiz kabul edilmiştir.         *'.center(80))
    print ('*********************************************'.center(80))
    print ('*              T A N I M L A R              *'.center(80))
    print ('*********************************************'.center(80))
    print ('* İLK HIZ : Atış hızını m/s                 *'.center(80))
    print ('* ATIŞ AÇISI : Yatayla Atış açısını derece  *'.center(80))
    print ('*********************************************'.center(80))
    try:
        atisAcisi=float( input("Atış açısını giriniz: "))
        atisHizi=float(input("Atış hızını giriniz (m/s): "))
        if atisAcisi <0 or atisAcisi >90:
            print( "Atış açısı 0 dereceden küçük ve 90 dereceden büyük olamaz!")
            time.sleep(1)
            egik_atis()      
        if atisHizi<0:
            print( "Atış hızı 0'dan küçük olamaz!")
            time.sleep(1)
            egik_atis()
        else:
            yercekimi =9.81
            sinusAcisi =math.sin((atisAcisi*math.pi)/180) # math kütüphanesi ile açının sinüs değerini hesapladık
            #y yönü
            cosinusAcisi =math.cos((atisAcisi*math.pi)/180) # math kütüphanesi ile açının cosinus değerini hesapladık
            #x yönü
            yukselmeHizi=atisHizi*sinusAcisi
            yatayHizi=atisHizi*cosinusAcisi
            maksYukselmeSuresi=yukselmeHizi/yercekimi
            maksYukseklik=(yukselmeHizi/2)*maksYukselmeSuresi
            toplamUcusSuresi=maksYukselmeSuresi*2
            hedefMesafe=yatayHizi*toplamUcusSuresi
        print(f"Sinüs Değeri: {sinusAcisi: .2f} \nKosinüs Değeri: { cosinusAcisi:.2f}") # f parametresi ile değeri formatladık ondalık hanenin 2 basamaklı gösterimini sağladık
        print(f"Yükselme Hızı: {yukselmeHizi:.2f} m/s")
        print(f"Yatay Hızı: {yatayHizi:.2f} m/s")
        print(f"Maksimum Yükselme Süresi: {maksYukselmeSuresi: .2f} saniye")
        print(f"Toplam Uçuş Süresi: {toplamUcusSuresi: .2f} saniye")
        print(f"Maksimum Yükseklik: {maksYukseklik:.2f} metre")
        print(f"Hedef Mesafesi: {hedefMesafe:.2f} metre")
        skontrol(egik_atis)
    except ValueError: # ValueError hatasında yapılacak işlemleri tanımladık
        print( "Sayısal değer giriniz!")
        time.sleep(1)
        egik_atis()

def dusey_yukari(): # düşey yukarı atış için fonksiyon tanımladık
    os.system('cls')
    print ('*********************************************'.center(80))
    print ('*      Düşey yukarı atış hesaplamaları      *'.center(80))
    print ('*********************************************'.center(80))
    print ('*     Sürtünme/Rüzgar gibi dış etkenler     *'.center(80))
    print ('*         önemsiz kabul edilmiştir.         *'.center(80))
    print ('*********************************************'.center(80))
    print ('*              T A N I M L A R              *'.center(80))
    print ('*********************************************'.center(80))
    print ('* İLK HIZ : Atış hızını m/s                 *'.center(80))
    print ('*********************************************'.center(80))
    try:
        v = float(input("Başlangıç hızını girin(m/s)"))
        g = 9.81
        t = round(v/g,2) # round komutu ile ondalık hane sayısını 2 basamaklı olacak şekilde yuvarladık
        print("Düşüşe başlama süresi:", t)
        skontrol(dusey_yukari)
        
    except:
        print('Girilen değerler geçersiz tekrar deneyiniz')
        time.sleep(1)
        dusey_yukari()

def dusey_asagi(): # düşey aşağı atış için fonksiyon tanımladık
    os.system('cls')
    print ('*********************************************'.center(80))
    print ('*       Düşey aşağı atış hesaplamaları      *'.center(80))
    print ('*********************************************'.center(80))
    print ('*     Sürtünme/Rüzgar gibi dış etkenler     *'.center(80))
    print ('*         önemsiz kabul edilmiştir.         *'.center(80))
    print ('*********************************************'.center(80))
    print ('*              T A N I M L A R              *'.center(80))
    print ('*********************************************'.center(80))
    print ('* İLK HIZ : Atış hızını m/s                 *'.center(80))
    print ('* YÜKSEKLİK : Atış yüksekliğini m           *'.center(80))
    print ('*********************************************'.center(80))
    try:
        v = float(input("Başlangıç hızını girin(m/s)"))
        h = float(input("Atış yüksekliğini girin(m)"))
        g = 9.81
        tt = abs(((-1/2*g)-v)+h)
        t = round(math.sqrt(tt),2)
        print("Çarpma süresi:", t," saniye")
        print("Çarpma hızı:", round(t*v,2)," m/s")
        skontrol(dusey_asagi)
        
    except:
        print('Girilen değerler geçersiz tekrar deneyiniz')
        time.sleep(1)
        dusey_asagi()

def skontrol(neyi): # skontrol fonksiyonu ile hesaplamalardan sonra yeni hesaplama yapılmak istenip istenmediğini kontrol ettik
    try:
        btus = input('Yeni hesaplama için <Y>, ana menü için <ENTER> tuşuna basınız...')
        if btus == 'Y' or btus == 'y':
            neyi() 
        else:
            menu()
    except:
        print('Hatalı seçim yaptınız tekrar deneyiniz...')
        time.sleep(1)
        neyi() # skontrol fonksiyonunda parametre olarak girilen fonksiyonu çağırdık

while(True): # ana menu döngüsünü tanımladık
    os.system('cls')
    menu() # menu fonksiyonunu çağırdık
    secim = '' # secim değişkeninin ilk değerini boş olarak tanımladık
    try:
        secim = int(input('Seçiminiz : '))
    except:
        print ('Hatalı seçim yaptınız tekrar deneyiniz')
        time.sleep(1)
    if secim == 1: # secim değişkeninin aldığı değerlere göre çağıracağı fonksiyonları belirledik
        yatay_atis()
    elif secim == 2:
        egik_atis()
    elif secim == 3:
        dusey_yukari()
    elif secim == 4:
        dusey_asagi()
    elif secim == 0:
        print ('Programdan çıktınız')
        exit() # secim değişkeninin 0 olamsı durumunda programdan çıktık
    elif isinstance(secim, int) and secim > 4: # isinstance ile hem secim değişkeninin integer olup olmadığını hem de değerinin 4 den büyük girilmesi durumunu kontrol ettik
        print ('Hatalı seçim yaptınız tekrar deneyiniz')
        time.sleep(1)
