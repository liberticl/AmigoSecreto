#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint,randrange # Para  sortear el amigo secreto
from math import factorial # Para condicionar cantidad de restricciones (básico)
import base64
import pandas as pd
import sys
import re

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

# Se lee el archivo con los datos de los jugadores y se revisa que sean más de 2.
def get_players_data():
	data = pd.read_csv('stgo2022/stgo0.csv',encoding='utf-8',low_memory=False)
	n = len(data)
	if(n > 2):
		flag = True
	else:
		print("El número debe ser mayor que 2.\n")
		sys.exit(-1)
	return data

# Se solicita el nombre de todos los jugadores. Depende directamente de la cantidad.
def get_players_names(players_data):
	return players_data["NOMBRE_PARTICIPANTE"].values.tolist()

# Solicitud de restricciones. 
def get_restrictions(players_data):
	rest = list()
	players = get_players_names(players_data)

	# Generando tuplas de restricciones
	for i in players_data.index:
		try:
			this_rest = players_data.loc[i,"RESTRICCIONES_DE_REGALO"].split(',').strip()
			for restriction in this_rest:
				if(restriction not in players):
					print("Una de las restricciones asociadas a",players_data.loc[i,"NOMBRE_PARTICIPANTE"],"no existe en la lista de jugadores!")
					sys.exit(-1)
				rest.append((players_data.loc[i,"NOMBRE_PARTICIPANTE"],restriction))
		except AttributeError:
			pass

	# Verificación de cantidad de restricciones matemáticamente posibles
	rest_number = len(rest)
	max_rest = n**2 - n - 1 #Cantidad de combinaciones menos las de tipo (i,i). Queda al menos una por jugador

	if(rest_number >= max_rest):
		print("No se pueden agregar más restricciones por limitaciones matemáticas!\n")
		sys.exit(-1)

	return rest

####################### Input Functions ###########################

####################### Output Functions ###########################

def export_dict(dict_to_exp):
	to_export = open("stgo2022/players.csv","w")
	for num,name in players_dict.items():
		to_export.write(str(num)+","+str(name)+"\n")
	to_export.close()	

def export_tuple(to_exp):
	to_export = open("stgo2022/result.csv","w")
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
players_info = get_players_data()
n = len(players_info)
players_names = get_players_names(players_info)
restriction_names = get_restrictions(players_info)

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
