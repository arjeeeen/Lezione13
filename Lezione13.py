	# Van Zwam Arjen
print ('Ciao! Siamo qui per calcolare il perimetro di una figura a tuo piacimento!')
print ('Premi 1 per il QUADRATO')
print ('Premi 2 per il RETTANGOLO')
print ('Premi 3 per il CERCHIO')
print ('Scegli: ')
scelta = int(input('>>>'))
if scelta == 1:
	print ('Ottimo, hai scelto il QUADRATO!')
	lato = float (input('Inserisci il valore di un lato del quadrato e ti calcolerò il perimetro: '))
	print ('Il perimetro del quadrato che ha lato ', lato, 'è di: ', lato*4)
elif scelta == 2:
	print ('Ottimo, hai scelto il RETTANGOLO!')
	base = float (input('Inserisci il valore della base: '))
	altezza = float (input('Inserisci il valore dell altezza: '))
	print ('Il perimetro del rettangolo che ha base ', base, 'e altezza ', altezza, 'è di: ', base*2 + altezza*2)
elif scelta == 3:
	print ('Ottimo, hai scelto il CERCHIO!')
	raggio = float (input('Inserisci il valore del raggio: '))
	calcolo = (2*raggio)*3,14
	print ('Il perimetro del cerchio che ha il raggio di ', raggio, 'è di: ', calcolo)
else:
	print ('Devi inserire un valore valido!')