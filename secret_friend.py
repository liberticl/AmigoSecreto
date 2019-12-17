#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint,randrange # Para  sortear el amigo secreto
from math import factorial # Para condicionar cantidad de restricciones (básico)
import base64

##############################################################################################
##	La finalidad de este código es proveer las funciones necesarias para					##
##	escoger las distintas duplas de un amigo secreto considerando lo siguiente:				##
##																							##
##	1. Quien manipula el código no debe saber quien le toca a los demás revisarlo.			##
##	2. Una persona no se puede tener como amigo secreto a sí misma.							##
##	3. Se pueden agregar las restricciones necesarias para que ciertos pares no se den.		##
##	4. Todos tendrán una persona a quien regalar y recibirán sólo un regalo.				##
##	5. Los pares finales no serán inversos, para continuidad en el juego.					##
##############################################################################################



####################### Numeric Functions #########################

# Creación de listas con n cantidad de jugadores
def create_list(n):
	new_list = []
	for i in range(n):
		new_list.append(i)
	return new_list

# Crea una lista con todos los pares posibles, sin considerar aquellos en que ambos elementos son iguales
# La lista posee una sublista para cada uno de los jugadores (lista de listas)
def create_comb(list_in):
	comb_list = []
	for i in list_in:
		new_list = []
		for j in list_in:
			if(i != j):
				new_list.append((i,j))
		comb_list.append(new_list)
	return comb_list

# Aplicación de restricciones dadas por el usuario
def restrictions(comb_list,rest_list):
	new_comb_list = comb_list
	for element in new_comb_list:
		for restriction in rest_list:
			if restriction in element:
				element.remove(restriction)
				# Revisión de que la restricción no genera una lista vacía
				if(len(element) == 0):
					new_comb_list.remove(element)
	return new_comb_list

# Revisión de que el número de jugadores coincida con la cantidad de listas de combinaciones
def check_players(n,player_list):
	if(n == len(player_list)):
		all_players_in = True
	else:
		all_players_in = False
	return all_players_in

# Revisión de que nadie deba hacer o reciba dos regalos
def check_uniques(n,result):
	x = set()
	y = set()
	unique_x = False
	unique_y = False
	for pair in result:
		x.add(pair[0])
		y.add(pair[1])
	if(check_players(n,list(x))):
		unique_x = True		
	if(check_players(n,list(y))):
		unique_y = True
	return (unique_x and unique_y)

# Ruleta para definir pares de amigo secreto
def roulette(n,comb_list):
	# Parte 1: Se detecta la existencia de una lista vacía y se pide cambiar las restricciones
	if(not check_players(n,comb_list)):
		print("Favor revisar las restricciones.\nUna o más pueden dejar a alguien sin amigo secreto.")
		return -1

	# Parte 2: se escogerá una dupla por lista de combinaciones.
	result = []
	for element in comb_list:
		rand = randint(0,len(element)-1)
		result.append(element[rand])

	# Parte 3: Revisar que los resultados no sean indeseados
	for pair_1 in result:
		for pair_2 in result:
			if(pair_1 != pair_2):
				# Revisión y corrección de resultados inversos
				if(pair_1 == pair_2[::-1]):
					pos = pair_1[0]
					result.remove(pair_1)
					rand = randint(0,len(comb_list[pos])-1)
					result.append(comb_list[pos][rand])

	# Parte 4: Revisar que todos tengan un amigo secreto y reciban regalo
	if(not check_players(n,result)):
		print("Un jugador no tiene amigo secreto.")
		return -1

	return result

# Se usa el algoritmo de Sattolo para generar una lista con orden aleatorio
def reorder(items):
	i = len(items)
	while(i > 1):
		i = i - 1
		j = randrange(i)  # 0 <= j <= i-1
		items[j], items[i] = items[i], items[j]
	return items

####################### Numeric Functions #########################

####################### Input Functions ###########################

# Se pide la cantidad de jugadores. Sólo pueden ser números enteros mayor que 2
def get_players_number():
	flag = False
	while(not flag):
		n = input("Ingrese número de jugadores: ")
		try:
			n = int(n)
			if(n > 2):
				flag = True
			else:
				print("El número debe ser mayor que 2.\n")
		except ValueError:
			print("Favor ingresar un número entero mayor que 2.\n")
	return n

# Se solicita el nombre de todos los jugadores. Depende directamente de la cantidad.
def get_players_names(n):
	flag = False
	players = []
	while(not flag):
		player_name = input("Ingrese el nombre de un jugador y presione 'Enter': ").lower()
		if(player_name not in players):
			players.append(player_name)
			if(n == len(players)):
				flag = True
		else:
			print("El jugador ingresado ya se encuentra en la lista.\n")
	return players

# Solicitud de restricciones. 
def get_restrictions(n,players_names):
	print("\nIngrese las restricciones considerando el siguiente esquema:")
	print("'Amigo_1 no le debe regalar a Amigo_2' se escribe como 'Amigo_1,Amigo_2'")
	print("Para finalizar el ingreso de restricciones, ingrese un punto ('.')\n")
	
	restriction_names = []
	rest_number = 0
	max_rest = n**2 - n - 1 #Cantidad de combinaciones menos las de tipo (i,i). Queda al menos una por jugador
	while(True):
		if(rest_number >= max_rest):
			print("No se pueden agregar más restricciones por limitaciones matemáticas!\n")
			break
		rest = input("Ingrese una restricción: ")
		if(rest == "."):
			break
		if("," in rest):
			splitted = rest.split(",")
			if(len(splitted) != 2):
				print("Ingrese de nuevo la restricción, con el formato correcto.\n")
				continue
			elif(splitted[0] not in players_names or splitted[1] not in players_names):
				print("Ingrese de nuevo la restricción, uno de los amigos no está en el listado.\n")
				continue
			else:
				pair = (splitted[0],splitted[1])
				if(pair not in restriction_names):
					restriction_names.append(pair)
					rest_number += 1
				else:
					print("Esta restricción ya fue ingresada.\n")
		else:
			print("Ingrese de nuevo la restricción, con el formato correcto.\n")
			continue
	return restriction_names

####################### Input Functions ###########################

####################### Output Functions ###########################

def export_dict(dict_to_exp):
	to_export = open("players.csv","w")
	for num,name in players_dict.items():
		to_export.write(str(num)+","+str(name)+"\n")
	to_export.close()	

def export_tuple(to_exp):
	to_export = open("result.csv","w")
	for name,secret in to_exp:
		to_export.write(str(name)+","+str(secret)+"\n")
	to_export.close()	

####################### Output Functions ###########################

####################### Encryption Functions ######################

# Codificación de nombres en base64
def names_encode(name_list):
	encoded_name_list = []
	for name in name_list:
		encoded_name_list.append(base64.b64encode(name.encode('utf-8')))
	return encoded_name_list

# Codificación de restricciones en base64
def rest_encode(rest_list):
	encoded_rest = []
	for element in rest_list:
		name_1,name_2 = element
		new_tuple = (base64.b64encode(name_1.encode('utf-8')),base64.b64encode(name_2.encode('utf-8')))
		encoded_rest.append(new_tuple)
	return encoded_rest

####################### Encryption Functions ######################

####################### NameNumber Functions ######################

# Asigna un número aleatorio a cada jugador.
def player_to_number(num_list,player_list):
	shuffle = reorder(num_list)
	players = {}
	for i in shuffle:
		players[i] = player_list[i]
	return players

# Encuentra el numero que corresponde a un jugador específico.
def find_player_number(player_to_find,players):
	for num,name in players.items():
		if(player_to_find == name):
			return num
	return -1

# Transforma las tuplas de jugadores en tuplas con los números correspondientes
def rest_to_number(players,rest_list):
	rest_num = []
	for pair in rest_list:
		name_1,name_2 = pair
		num_1 = find_player_number(name_1,players)
		num_2 = find_player_number(name_2,players)
		new_tuple = (num_1,num_2)
		rest_num.append(new_tuple)
	return rest_num

####################### NameNumber Functions ######################


################################## MAIN CODE ###################################

# Obtención de datos
n = get_players_number()
players_names = get_players_names(n)
restriction_names = get_restrictions(n,players_names)

# Codificación de datos
players_encoded = names_encode(players_names)
restriction_encoded = rest_encode(restriction_names)

# Creación de listas
players_numbers = create_list(n)
possible_combinations = create_comb(players_numbers)

# Nombres a números
players_dict = player_to_number(players_numbers,players_encoded)
restriction_numbers = rest_to_number(players_dict,restriction_encoded)
	
export_dict(players_dict)

# Restricción de las combinaciones
possible_combinations = restrictions(possible_combinations,restriction_numbers)

# Lanzamiento de la ruleta!
while(True):
	res = roulette(n,possible_combinations)
	if(res != -1):
		if(check_uniques(n,res)):
			break

# Resultados
export_tuple(res)
for i in res:
	print(i)

################################## MAIN CODE ###################################
