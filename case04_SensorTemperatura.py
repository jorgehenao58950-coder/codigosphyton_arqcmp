Vs = 20 # voltios
Rs = 75 # ohmios
Ro = 100 # ohmios
k = 0.5 # adimencional
done = 1 #valor centinela

while done:

	Vm = float (input("ingrese el valor mostrado en el multimetro; °"))

	if Vm >= 12.0 and Vm  <= 18.0: # si Vm esta entre 12 y 18. entonces
		T = (Rs/K) * (Vm/ (Vs/Vm)) - (Ro/K) # formula de la temperatura de la camara
		print ("la temperatura de la camara es:",T)
		done: 0 # desactivar centinela
	else
		print("voltaje incorrecto, ingrese un nuevo el valor:")
