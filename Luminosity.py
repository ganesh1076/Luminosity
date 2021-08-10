import numpy as np

m=float(input('apparent Mag of a star: '))
mas=float(input('parallaxes in milliarcsec: '))
emas=float(input('error in parallex: '))
Av=float(input('Av: '))
BCv=float(input('(Consider it as 0 for late B to late A type stars)B.C.:'))
#Mv absolute Mag
Mv=m -Av + 5*(np.log10(mas/1000) + 1)
print('Mv', Mv)
#Mbol is absolute bolometric magnitude
#Mbol0 absolute bolometric magnitude of the Sun
Mbol0=4.74


Mbol=Mv + BCv - Mbol0
print('Mbol', Mbol)

L_by_L0=-0.4*Mbol

print('Luminousity is', L_by_L0)




lum_er=(-2/mas)*emas

print('Error in luminosity is : ', lum_er)
