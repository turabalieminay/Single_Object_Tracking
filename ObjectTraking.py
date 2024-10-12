import cv2
import sys   #SİSTEM KÜTÜPHANESİNİ ALGORİTMADAN ÇIKIŞ YAPMAK İÇİN 
from random import randint #RANDOM KÜTÜPHANESİNİDE RASTGELE DEĞERLER ÜRETMEK İÇİN KULLANIYORUZ 


#print(cv2.__version__)

#NESNE TESPİTİNDE HANGİ NESNE TAKİBİ ALGORİTMASINI SEÇEÇCİĞİMİZ BİLMEMİZ İÇİN UFAK Bİ YAPI TASARLIYORUZ BU YAPI SAYESİNDE İSTEDİĞMİZ ALGORİTMALARA TEK Bİ TUŞLA ULAŞBİLECEĞİZ 

trackers = ["BOOSTING", "MIL", "KCF", "CSRT", "TLD", "MEDIANFLOW", "MOSSE"]

i = randint(0,6)
tracker_algorithm = trackers[i]

if tracker_algorithm == "BOOSTING":
    tracker = cv2.legacy.TrackerBoosting_create()
    print(tracker)
    
elif tracker_algorithm == "MIL":
    tracker = cv2.legacy.TrackerMIL_create()
    print(tracker)
    
elif tracker_algorithm == "KCF":
    tracker = cv2.legacy.TrackerKCF_create()    
    print(tracker)
    
elif tracker_algorithm == "CSRT":
    tracker = cv2.legacy.TrackerCSRT_create()
    print(tracker)
    
elif tracker_algorithm == "TLD":
    tracker = cv2.legacy.TrackerTLD_create()
    print(tracker)
    
elif tracker_algorithm == "MEDİANFLOW":
    tracker = cv2.legacy.TrackerMedianFlow_create()    
    print(tracker)
    
elif tracker_algorithm == "MOSSE":
    tracker = cv2.legacy.TrackerMOSSE_create()     
    print(tracker)
    
else:
    print("[ERROR].. number out of index !")    
    

#NESNE TAKİBİ İŞLEMLERİNE BAŞLIYORUZ 

cap = cv2.VideoCapture(0)   #BURADA CAP KOMUTUT VİDEONUN OKUNMAYA BAŞLADIĞNI BELİRTİR 

ret, frame = cap.read()  #BURADAKİ KOMUT İSE VİDEONUN İLK KARESİNİN OKUNMASI İÇİN YAZILIR FRAME İLK KAREYİ KAYDEDER RET İSE KAYDIN OLUP OLMADIĞINI BELİRTİR YANİ 1 VRYA 0 DĞEERİ DÖNDÜRÜRR 
    
box = cv2.selectROI(frame)  #BURADAKİ SELECT ROI KOMUTU SAYESİNDE FRAME VİDEOSU ÜZERİNDE SEÇMEK İSTEDİĞİMİZ YERİ SEÇİYORUZ VE BUDA BİZE BİR KOORDİNAT DÖNDÜRÜYOR 
print("[INFO]... Box Coordinates: ", box)


ret = tracker.init(frame, box) #BURASI SAYESİNDEDE TRACKER KOMUTUNU BAŞLATIYORUM VE FRAME ÜZERİNDE ÇALIŞACAĞIMI VE MODELİNDE BOX İLE ÇALIŞTIRALACAĞINI BELİRİTİYORUM
print("[INFO]... Return: ",ret)


color = (randint(0,255), randint(0, 255), randint(0,255))
print("[INFO].. Color that genetad with randint method: ",color)


while True:
    ret, frame = cap.read()
    
    #KONTROL BLOĞU 
    if ret == False:
        print("[ERROR] something went wrong when loading")

    elif ret == None:
        print("[ERROR] wrong path")
        
    #--------------------------------------------------#
    ret, box = tracker.update(frame)
    if ret == True:
        (x,y,w,h) = [int(i) for i in box ]
        loc = (x,y,w,h)
        print(" Location that calculated: ",loc)
        #--------------------------------------------------#
        #BULDUĞUMUZ KOORDİNATLARA DİKDÖRTGENLERİ ÇİZDİRİYORUZ 
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2, 1)
        cv2.putText(frame, str(tracker), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2)
    
    #--------------------------------------------------#    
    else:    
        cv2.putText(frame, "...[ERROR]...", (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2)    
    
    cv2.imshow("Single Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release() 
cv2.destroyAllWindows()


















    