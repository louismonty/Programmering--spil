import math
from random import randint

højde = randint(1,42)

def gamestart():
    print("En bold bliver smidt ud fra Rundetårn i en højde af ",højde,"Meter")

    tid_gæt = float(input("Hvor lang tid tror du det tager i sekunder?: "))

    tid = math.sqrt((-højde)/(1/2*(-9.82)))
    print ("\nBolden rammer jorden efter ",tid, " sekunder")

    afvigelse = abs(tid-tid_gæt)
    print("\nDu gættede forkert med ",afvigelse," sekunder")

    procentvis_afvigelse = int((abs(tid - tid_gæt) / tid) *100)
    print("Din procentvise afvigelse var",procentvis_afvigelse,"%")
