import asyncio
import numpy as np
import math
from geooperation_api.models import Point

class GeometricOperation:

     @staticmethod
     def cizgiUzunlukBulAsync(point1:Point,point2:Point) -> float:
          "İki nokta arasi cizgi uzunlugunu bulmak icin fonksiyon"
          print(point1.X,"---",point1.Y)
          print(point2.X,"---",point2.Y)
          toplam=((point2.X-point1.X)**2)+((point2.Y-point1.Y)**2)
          uzunluk=math.sqrt(toplam)
          return uzunluk

     @staticmethod
     def merkezveYaricapBul(p1:Point,p2:Point,p3:Point) -> tuple[Point,float]:
          "üc noktası biline cemberin merkez ve yaricapını bulma fonksiyonu noktalar x,y,z olmalı z=1 olmalı"
          a1=-(p1.X**2)-(p1.Y**2)
          a2=-(p2.X**2)-(p2.Y**2)
          a3=-(p3.X**2)-(p3.Y**2)
          matris=np.array([
               [p1.X,p1.Y,p1.Z],
               [p2.X,p2.Y,p2.Z],
               [p3.X,p3.Y,p3.Z]
          ])
          matris1=np.array([
               [a1,p1.Y,p1.Z],
               [a2,p2.Y,p2.Z],
               [a3,p3.Y,p3.Z]
          ])
          matris2=np.array([
               [p1.X,a1,p1.Z],
               [p2.X,a2,p2.Z],
               [p3.X,a3,p3.Z]
          ])
          matris3=np.array([
               [p1.X,p1.Y,a1],
               [p2.X,p2.Y,a2],
               [p3.X,p3.Y,a3]
          ])
          det=np.linalg.det(matris)
          det1=np.linalg.det(matris1)
          det2=np.linalg.det(matris2)
          det3=np.linalg.det(matris3)

          D=det1/det
          E=det2/det
          F=det3/det
          Merkez=Point(-D/2,-E/2)
          Yaricap=(math.sqrt((D**2)+(E**2)-(4*F)))*0.5
          if(math.isnan(Yaricap) or math.isnan(Merkez.X) or math.isnan(Merkez.Y) or math.isnan(Merkez.Z)):
               return Point(None,None,None),None
          else:return Merkez,Yaricap

     @staticmethod
     def dogruEgimBulma(p1:Point,p2:Point) -> float:
          "Dogrunun egimini bulmak icin fonksyion"
          x1,y1,x2,y2=p1.X,p1.Y,p2.X,p2.Y
          try:
               egim=(y2-y1)/(x2-x1)
          except Exception as ex:
               print("egim 0/a veya a/0 oldugundan sonsuz deger donduruldu")
               "math.inf"
               return math.inf
          else:
               return egim

     @staticmethod
     def dogruAciBulma(egim:float) -> float:
          "egimi bilinen dogrunun acısını bulmak icin fonksiyon"
          aci=math.atan(egim)
          derece = GeometricOperation.radyaniDereceyeCevirme(aci)
          return derece

     @staticmethod
     def dogruAciBul(p1:Point,p2:Point) -> float:
          "iki noktası bilinen dogrunun acısını bulmak icin fonksiyon"
          egim=GeometricOperation.dogruEgimBulma(p1,p2)
          aci=GeometricOperation.dogruAciBulma(egim)
          return aci

     @staticmethod
     def acidanEgimBulma(aci:float) -> float:
          "Acidan Egim bulma Radyan"
          aciDerece=GeometricOperation.dereceyiRadyanaCevirmeAsync(aci)
          egim=math.tan(aciDerece)
          return egim

     @staticmethod
     def radyaniDereceyeCevirme(radyan:float) -> float:
          derece = radyan * (180 / math.pi)
          return derece

     @staticmethod
     def dereceyiRadyanaCevirmeAsync(derece:float) -> float:
          radyan = derece * (math.pi / 180)
          return radyan

     @staticmethod
     def cizgiOrtaNokta(p1:Point,p2:Point) -> Point:
          "iki nokta arası orta noktayi bulmak icin fonksiyon"
          x=(p1.X+p2.X)/2
          y=(p1.Y+p2.Y)/2
          ortaNokta=Point(x,y)
          return ortaNokta

     @staticmethod
     def pointMatrisDonustur(point:Point) -> list[float]:
          "QPointF veya QPoint matris listeye cevirme [x,y,z] z=1"
          matris=[point.X,point.Y,point.Z]
          return matris

     @staticmethod
     def ikiDogruArasiAciBulma(egim1:float,egim2:float) -> float:
          "Kesişen İki Dogru Arasi Aci Bulma Formülü"
          tanjant=(egim1-egim2)/(1+(egim1*egim2))
          aci=GeometricOperation.dogruAciBulma(tanjant)
          return aci

     @staticmethod
     def IkiNoktaninIcCarpimi(p1:Point,p2:Point)-> float:
          "İki Noktanın İc Carpim Bulmak icin Fonksiyon"
          return p1.X*p2.Y-p1.Y*p2.X

     @staticmethod
     def IkıNoktaninFarki(p1:Point,p2:Point) -> Point:
          "İki Noktanın Farkını Bulmak icin Fonksiyon"
          nokta=Point(p1.X-p2.X,p1.Y-p2.Y,p1.Z-p2.Z)
          return nokta

     #validation yapılmalı
     @staticmethod
     def NoktaDogrununNeresindeBul(p1:Point,p2:Point,p3:Point) -> str:
          "P3,P1 ve P2 noktalarından olusan dogrunun neresinde sag-sol-üzerindemi"
          k=GeometricOperation.IkıNoktaninFarki(p3,p1)
          l=GeometricOperation.IkıNoktaninFarki(p2,p1)
          kontrol=GeometricOperation.IkiNoktaninIcCarpimi(k,l)
          if kontrol>0:
               return "right"
          elif kontrol<0:
               return "left"
          else:
               return "on"

     #validation yapılmalı
     @staticmethod
     def ikiDogrununKesisimNoktasiBulma(p1:Point,p2:Point,p3:Point,p4:Point) -> Point:
          a=((p4.Y-p3.Y)*(p3.X-p1.X))-((p3.Y-p1.Y)*(p4.X-p3.X))
          b=((p4.Y-p3.Y)*(p2.X-p1.X))-((p2.Y-p1.Y)*(p4.X-p3.X))
          T=a/b
          p5x=p1.X+(p2.X-p1.X)*T
          p5y=p1.Y+(p2.Y-p1.Y)*T
          nokta=Point(p5x,p5y)
          return nokta

     ## Buna Bak
     @staticmethod
     def ikinciDerecedenDenklemCozumu(a,b,c):
          d=(b**2)-(4*a*c)
          if d<0:
               print("kök yok")
          if d==0:
               print("kökler cakısık")
               x=-b/(2*a)
               return x,x
          if d>0:
               x=(-b-math.sqrt(d))/(2*a)
               y=(-b+math.sqrt(d))/(2*a)
               return x,y

     ## bunada bak
     @staticmethod
     def ikiParalelDogru(p1:Point,p2:Point,mesafe:float) -> Point:
          egim=GeometricOperation.dogruEgimBulma(p1,p2)
          a=egim
          b=-1
          x1,y1,x3,y3=p1.X,p1.Y,float,float
          c1=-y1-(egim*x1)
          deger=mesafe*(math.sqrt(a**2+b**2))
          c2=deger+c1

          #c2=-y3-(egim*x3)
          p3=Point(x3,y3)
          return p3

     @staticmethod
     def uzunlukNoktalariniBul(nokta:Point,uzunluk:float,egim:float) -> tuple[Point,Point]:
          "Baslagic Noktasina Aynı Dogru Uzerindeki Eşit Uzunluktaki iki Noktayi Bulur"

          noktaA=Point()
          noktaB=Point()

          if egim==0:
               noktaA.X=nokta.X+uzunluk
               noktaA.Y=nokta.Y

               noktaB.X=nokta.X-uzunluk
               noktaB.Y=nokta.Y

          elif math.isinf(egim):
               noktaA.X=nokta.X
               noktaA.Y=nokta.Y+uzunluk

               noktaB.X=nokta.X
               noktaB.Y=nokta.Y-uzunluk

          else:
               dx=uzunluk/math.sqrt(1+(egim*egim))
               dy=egim*dx

               noktaA.X=nokta.X+dx
               noktaA.Y=nokta.Y+dy

               noktaB.X=nokta.X-dx
               noktaB.Y=nokta.Y-dy
          return noktaA,noktaB

     @staticmethod
     def uzunluktakiNoktayiBul(bnokta:Point,fareKonumu:Point,uzunluk:float) -> Point:
          "Mousenin Konumuna Gore Belli Uzunluktali Mesafedeki Noktayi Bulur"

          egim=GeometricOperation.dogruEgimBulma(bnokta, fareKonumu)

          a=GeometricOperation.uzunlukNoktalariniBul(bnokta, uzunluk,egim)
          b=GeometricOperation.uzunlukNoktalariniBul(bnokta, uzunluk,-egim)

          noktalar=GeometricOperation.NoktaDogrununNeresindeBul(bnokta, b[1], a[0])
          fareKonumuNoktasi=GeometricOperation.NoktaDogrununNeresindeBul(bnokta, b[1], fareKonumu)

          if noktalar=="üzerinde":
               xfark=fareKonumu.X-bnokta.X
               yfark=fareKonumu.Y-bnokta.Y
               if xfark<0 or yfark<0:
                    return a[1]
               else:
                    return a[0]
          elif noktalar==fareKonumuNoktasi:
               return a[0]
          else:
               return a[1]

     @staticmethod
     def ikiNoktaXYFark(p1:Point,p2:Point) -> tuple[float,float]:
          "P2 ve P1 x ve y leri arasindaki farki hesaplar x,y dondurur"
          x=p2.X-p1.X
          y=p2.Y-p1.Y
          return x,y

     @staticmethod
     def noktaHangiBolgedeBul(origin:Point,p1:Point) -> int:
          "Origin noktasi koordinat sistemin 0,0 kabul edilerek p1 noktasının hangi bölgede oldugnu bulur"
          originx,originy=origin.X,origin.Y
          p1x,p1y=p1.X,p1.Y
          if p1x>originx and p1y>originy:
               return 1
          elif p1x<originx and p1y>originy:
               return 2
          elif p1x<originx and p1y<originy:
               return 3
          elif p1x>originx and p1y<originy:
               return 4
          else:
               #üzerinde
               return 5
          
     

     @staticmethod
     def enyakinNoktayiBul(p:Point,pointList:list[Point]) -> Point:
          liste=list(map(lambda x:GeometricOperation.cizgiUzunlukBulAsync(p,x),pointList))
          return pointList[liste.index(min(liste))]
     

     @staticmethod
     def baslagicBitisAcisiBul(merkez:Point,p1: Point,p2: Point,p3: Point) -> list[float,float]:
          baslangicAci=GeometricOperation.dogruAciBul(merkez,p1)

          if p1.X>merkez.X:
               if p1.Y>merkez.Y:
                    baslangicAci=baslangicAci
               else:
                    baslangicAci=baslangicAci
          else:
               if p1.Y>merkez.Y:
                    baslangicAci=baslangicAci+180
               else:
                    baslangicAci=baslangicAci-180
          
          p3Aci=GeometricOperation.dogruAciBul(merkez,p3)
          if p3.X>merkez.X:
               if p3.Y>merkez.Y:
                    p3Aci=p3Aci
               else:
                    p3Aci=p3Aci+360
          else:
               if p3.Y>merkez.Y:
                    p3Aci=p3Aci+180
               else:
                    p3Aci=p3Aci+180

          
          konum=GeometricOperation.NoktaDogrununNeresindeBul(p1,p3,p2)

          if konum=="right":
               bitisAci=p3Aci-baslangicAci
          elif konum=="left":
               bitisAci=-(360-(p3Aci-baslangicAci))
          else:
               bitisAci=p3Aci-baslangicAci

          return [-baslangicAci*16,-bitisAci*16]
     

     @staticmethod
     def findStartAndStopAngleTwoPoint(center: Point,p1: Point,p2: Point):
          startAngle=GeometricOperation.dogruAciBul(center,p1)

          if p1.X>center.X:
               if p1.Y>center.Y:
                    startAngle=startAngle
               else:
                    startAngle=startAngle
          else:
               if p1.Y>center.Y:
                    startAngle=startAngle+180
               else:
                    startAngle=startAngle-180

          p2Aci=GeometricOperation.dogruAciBul(center,p2)

          if p2.X>center.X:
               if p2.Y>center.Y:
                    p2Aci=p2Aci
               else:
                    p2Aci=p2Aci+360
          else:
               if p2.Y>center.Y:
                    p2Aci=p2Aci+180
               else:
                    p2Aci=p2Aci+180

          return [-startAngle*16,-(p2Aci-startAngle)*16]
     

     

     
          
