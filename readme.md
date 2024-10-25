# Dezvoltarea unei soluții de eye-tracking

Eye tracking-ul poate fi descris ca o tehnică de înregistrare a mișcării ochilor și a locației privirii de-a lungul timpului pentru a observa alocarea atenției vizuale. Această tehnică utilizează procesarea imaginilor și (sau) algoritmi de învățare automată pentru a detecta ochii umani și a identifica prezența și mișcarea ochilor unei persoane într-un videoclip în timp real. Un număr tot mai mare de tehnici non-invazive de urmărire a ochilor au fost dezvoltate pentru a înlocui tehnicile mai vechi care necesită contact direct cu corneea ochiului uman. Sistemul accesibil de eye-tracking câștigă popularitate față de sistemele costisitoare și nepractice de eye-tracking care se bazează pe un dispozitiv special de urmărire a privirii.

Interesul pentru aplicațiile de detectare a ochilor a crescut considerabil. Foarte multe metode de detectare a ochilor sunt utilizate în diferite aplicații, cum ar fi neuroștiința, psihologia, tehnologiile asistive pentru a comunica cu pacienții cu dizabilități, jocuri pe calculator, tehnologii de monitorizare pentru conducătorii auto împotriva oboselii (în transportul comercial și public), în industria publicității, identificarea persoanei bazat pe recunoașterea feței și detectarea ochilor (iris) și în diferite aplicații militare.

Scurt istoric:

![Enter image alt description](Images/1PT_Image_1.png)

Eye tracking-ul este prima și importantă sarcină a sistemului de urmărire a ochilor.Ea captează ochii unui individ folosind un senzor infraroșu sau o cameră cu scopul de a identifica irisul și de a estima locația pupilei într-o imagine a unui ochi și. După finalizarea detectării ochilor, sarcinile de predicție a stării ochilor și (sau) privirea ochilor sunt apoi implementate pentru a urmări mișcarea ochilor. În general, precizia urmăririi ochilor se referă la contrastul dintre direcția măsurată a privirii și direcția reală a privirii pentru un individ. Rezultatele pot varia de pe ecran, în funcție de condițiile externe, cum ar fi iluminarea, calitatea senzorului și caracteristicile individuale ale ochiului, de exemplu forma ochiului.

Pașii de dezvoltare pentru algoritmul de eye tracking:

![Enter image alt description](Images/jQG_Image_2.png)

| Nr. | Autor(i) / An | Titlul articolului / proiectului | Aplicație / Domeniu  | Tehnologii utilizate  | Metodologie / Abordare  | Rezultate   | Limitări   | Comentarii suplimentare  |
|---|---|---|---|---|---|---|---|---|
| 1 | Siti Nuradlin Syahirah Sheikh Anwar, Azrina Abd Aziz, Syed Hasan Adil | Development of Real-Time Eye Tracking Algorithm  | Eye detection | OpenCV | Eye tracking bazat pe detectarea fetei | 90% Precizie in detectarea pozitiei ochilor si 100% detectarea ochilor | Eye detection fail pentru persoanele care poarta ochelari si apare glare-ul |  |
| 2 | Radu Gabriel Bozomitu,
Alexandru Păsărică, Daniela Tărniceriu
,Cristian Rotariu  | Development of an Eye Tracking-Based Human-Computer Interface for Real-Time Applications | Eye detection | Algoritmi: least-squares fitting of ellipse (LSFE),
circular Hough transform (CHT) | Identificarea celui mai potrivit algoritm de detectare a pupilei | Rata de detectie de 84% la 50 pixeli | Algoritmul Starburst are precizie mica |  |
| 3 |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |

**Bibliografie:**

**[https://www.mdpi.com/1424-8220/19/16/3630](https://www.mdpi.com/1424-8220/19/16/3630)**

**[https://ieeexplore.ieee.org/document/9676406](https://ieeexplore.ieee.org/document/9676406)**
