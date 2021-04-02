import datetime

while True:
    birthday = input('Cocugunuzun hangi y�lda dogdugunu GG AA YYYY �eklinde giriniz: ')

    if (len(birthday) < 10 or len(birthday) > 10): #tarihi dogru girmesi icin uzunluk kontrol�
        print("Ge�erli bir tarih giriniz.")
        continue

    numbers = "0123456789 " #harf engeli yapmak icin rakamlar ve bosluk
    control = True #true false degiskeni yaptim cunku for dongusunu break ile kapatt�g�mda kodlara devam ediyor

    for i in birthday: #birthday inputunu d�ng�ye aliyor
        if (i not in numbers): #yazili olan tarihte numbersin icindeki yazilanlardan farkli bir sey varmi diye kontrol ediyor.
            print("Cocugunuzun dogum tarihi sadece say� i�erebilir.")
            control = False #eger tarihte numbersin icindekilerden farkli bir harfi isaret vs varsa false oluyor.
            break

    if (control == False): # tarihte farkli bir sey olduysa donguyu tekrar d�nd�r�r.
        continue

    day1, mounth1, year1 = birthday.split() #gun ay yili ayri ayri almak icin liste olusturuyoruz.
    current_day = datetime.datetime.now() #g�ncel zaman
    a_current_day = datetime.datetime.strftime(current_day, "%d %m %Y") #g�ncel zamani g�n ay yil seklinde aliyoruz.
    day2, mounth2, year2 = a_current_day.split() # g�n ay yil seklinde aldigimiz g�ncel zamani listeye aliyoruz.
    age = int(year2) - int(year1) #
    day = int(day1)               # engelleme yapmak icin eklentiler.
    mounth = int(mounth1)         #

    #gerekli engellemeler.
    if (age < 0):
        print("Ge�erli bir tarih giriniz.")
        continue
    elif (day > 31 or day == 0):
        print("Ge�erli bir tarih giriniz.")
        continue
    elif (mounth > 12 or mounth == 0):
        print("Ge�erli bir tarih giriniz.")
        continue

    #program tam dogru asi vermesi icin g�n hesabi yapmak daha mantikli oldugu icin ve daha kolaylik sagliyacagi g�n hesabi ile yaptim.
    d_birthday = datetime.datetime(int(year1), int(mounth1), int(day1)) #cocugun dogum tarihini datetime modulune kay�t ettirdik.
    l_day = current_day - d_birthday #guncel zamandan dogum tarihin datetime li sekilde cikardik gun hesabi yapmak icin.
    
    #burada ise kontroller mevcut. tablodaki tarihlere gore gun hesabi yapip yapildi. l_day.days yapark ise sonucun sadece gununu aldik.
    if (l_day.days >= 0 and l_day.days < 30):
        print("Cocugunuzun Hep-B I a��s� olmas� gerekmektedir.")
        continue
    elif (l_day.days >= 30 and l_day.days < 60):
        print("Cocugunuzun Hep-B II a��s� olmas� gerekmektedir.")
        continue
    elif (l_day.days >= 60 and l_day.days < 120):
        print("Cocugunuzun BCG I, KPA I ve DaBT-IPA-Hib I a��lar�n� olmas� gerekmektedir.")
        continue
    elif (l_day.days >= 120 and l_day.days < 180):
        print("Cocugunuzun KPA II ve DaBT-IPA-Hib II a��lar�n� olmas� gerekmektedir.")
        continue
    elif (l_day.days >= 180 and l_day.days < 360):
        print("Cocugunuzun Hep-B III, DaBT-IPA-Hib III ve OPA I a��lar�n� olmas� gerekmektedir.")
        continue

    #sucicegi icin datetime kayit ettik gun hesabi icin guncel zamandan cikardik.
    wf = datetime.datetime(2012, 1, 1)
    wf_day = current_day - wf

    #su cicegi icin ayri kontrol koyduk.
    if (l_day.days >= wf_day.days and l_day.days >= 360 and l_day.days < 540):
        print("Cocugunuzun KPA R, Sucicegi I ve KKK I a��lar�n� olmas� gerekmektedir.")
        continue
    elif (l_day.days >= 360 and l_day.days < 540):
        print("Cocugunuzun KPA R ve KKK I a��lar�n� olmas� gerekmektedir.")
        continue

    #Hep-A asisi icin datetime kayit ettik gun hesabi icin guncel zamandan cikardik.
    ha = datetime.datetime(2011, 3, 1)
    ha_day = current_day - ha

    #Hep-A icin kontrol koyduk ve devam ettik.
    if (l_day.days <= ha_day.days and l_day.days >= 540 and l_day.days < 720):
        print("Cocugunuzun DaBT-IPA-Hib R, OPA II ve Hep-A I a��lar�n� olmas� gerekmektedir.")
        continue
    elif (l_day.days >= 540 and l_day.days < 720):
        print("Cocugunuzun DaBT-IPA-Hib R ve OPA II a��lar�n� olmas� gerekmektedir.")
        continue      
    elif (l_day.days <= ha_day.days and l_day.days >= 720 and l_day.days < 1440):
        print("Cocugunuzun Hep-A II a��s� olmas� gerekmektedir.")
        continue

    #KKK ve DaBT-IPA R asisi icin datetime kayit ettik gun hesabi icin guncel zamandan cikardik.
    da = datetime.datetime(2016, 7, 1)
    da_day = current_day - da

    da_year = int(l_day.days / 365) #cocugun 13. yasini gun bolu 365 yaparak tespit edicez gun hesabi yerine daha kolaylik sagliyor ve ondalik sayi vermemesi icin int icine aldik.

    #KKK ve DaBT-IPA R asisi icin ve 13 yasinda vurulmas� icin kontrol koydurduk.
    if (l_day.days <= da_day.days and l_day.days >= 1440 and da_year < 13):
        print("Cocugunuzun KKK ve DaBT-IPA R a��s� olmas� gerekmektedir.")
        continue
    elif (da_year == 13):
        print("Cocugunuzun Td R a��s� olmas� gerekmektedir.")
        continue
    
    print("Cocugunuzun olmasi gereken asi bulunamamistir.") #tarih hicbir seye uymuyorsa hata verip dongu yine basa doner.