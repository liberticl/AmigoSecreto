#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas
import base64
from time import *
from gmail_api import *

##############################################################################################
##	La finalidad de este código es proveer las funciones necesarias para					##
##	descifrar el amigo secreto y enviarlo por correo electrónico al grupo					##
##																							##
##	1. Quien manipula el código no debe saber quien le toca a los demás.					##
##	2. Ni uno de los nombres de la dupla puede quedar en evidencia							##
##############################################################################################

####################### Getting Info ##############################

real_names = {"ñija":"Daniela Valencia","eli":"Elisa Santibañez","dani":"Daniela Lizama","tania":"Tania Orellana","bryan":"Bryan Salazar","isa":"Isabel Contreras","seba":"Sebastián Lizama","leo":"Leonardo Escobar","yo":"Francisco Vergara"}

# Importa los jugadores con su respectivo numero
# Notar que tambien corrige errores de exportación en formato 'byte'
def import_dict(dict_to_imp):
	data = {}
	to_import = open(dict_to_imp,"r")
	for line in to_import:
		line = line[:-2]
		splitted = line.split(",")
		if(len(splitted) == 2):
			data[int(splitted[0])] = splitted[1][2:]
		else:
			data = -1
	to_import.close()
	return data

# Importa las tuplas con resultados.
def import_tuple(to_imp):
	data = {}
	to_import = open(to_imp,"r")
	for line in to_import:
		line = line
		splitted = line.replace('\n','').split(",")
		if(len(splitted) == 2):
			data[splitted[0]] = splitted[1]
		else:
			data = -1
	to_import.close()
	return data

# Obtención de base de datos de correos.
def get_database(file):
	table = pandas.read_csv(file)
	dict_one = table.to_dict()
	database = dict()
	#print(len(table))
	for i in range(len(table)):
		name = dict_one['nombre'][i]
		mail = dict_one['mail'][i]
		database[name] = mail
	#print(len(database))
	return database

# Extracción del nombre.
def one_word(word):
	if ' ' not in word:
		return word
	else:
		splitted = word.split(" ")
		one_word = splitted[0]
	return one_word

####################### Getting Info ##############################

####################### Decryption Functions ######################

# Decodificación de nombres en base64
def decode64(encoded):
	decoded_name = base64.b64decode(encoded)
	return decoded_name

# Decodificación de diccionario
def decode_dict(encoded_dict):
	new_dict = {}
	for key,encoded in encoded_dict.items():
		new_dict[key] = decode64(encoded)
	return new_dict

####################### Decryption Functions ######################

####################### Game Functions ############################

# Traduce todos los diccionarios hasta descifrar el resultado final.
def final_result(real_names,players_dict,result):
	new_dict = {}
	for n0,n1 in result.items():
		name = players[int(n0)]
		new_name = real_names[decode64(name)]
		secret = players[int(n1)]
		new_secret = real_names[decode64(secret)]
		new_dict[new_name] = new_secret
	return new_dict

####################### Game Functions ############################

################################## MAIN CODE ###################################

# Obteniendo datos de jugadores
players = import_dict("players.csv")
players_dict = decode_dict(players)

# Obteniendo datos de resultados
result = import_tuple("result.csv")
result = final_result(real_names,players_dict,result)

# Obteniendo correos electrónicos
db = get_database('stgo0.csv')
msje = open('mensaje.txt')

txt = ''
for line in msje:
	txt = txt + line	

msje.close()

n = 0
for name,mail in db.items():
	body = 'Hola '+one_word(str(name))+':\n\n'+txt+result[name]
	testMessage = create_message('valpotech@gmail.com', mail, 'Amigo Secreto 2020', body)
	testSend = send_message(service,'me', testMessage)
	n += 1
	print("Mensaje enviado")
	sleep(3)

#print "Se han intentado enviar "str(n)" correos electrónicos con éxito"


################################## MAIN CODE ###################################


