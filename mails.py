#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas
import base64
from time import *

if __name__ == "__main__":
	from gmail_api import *

##############################################################################################
##	La finalidad de este código es proveer las funciones necesarias para					##
##	descifrar el amigo secreto y enviarlo por correo electrónico al grupo					##
##																							##
##	1. Quien manipula el código no debe saber quien le toca a los demás.					##
##	2. Ni uno de los nombres de la dupla puede quedar en evidencia							##
##############################################################################################

####################### Getting Info ##############################

real_names = {"ñija":"Daniela Valencia","eli":"Elisa Santibañez","dani":"Daniela Lizama","tania":"Tania Orellana","isa":"Isabel Contreras","seba":"Sebastián Lizama","leo":"Leonardo Escobar","yo":"Francisco Vergara"}

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
		name = dict_one['NOMBRE_PARTICIPANTE'][i]
		mail = dict_one['EMAIL_PARTICIPANTE'][i]
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
def final_result(real_names,result):
	new_dict = {}
	for n0,n1 in result.items():
		name = base64.b64decode(players[int(n0)]).decode('utf-8')
		secret = base64.b64decode(players[int(n1)]).decode('utf-8')
		new_dict[name] = secret
	return new_dict

####################### Game Functions ############################

################################## MAIN CODE ###################################

# Obteniendo datos de jugadores
players = import_dict("stgo2021/players.csv")
players_dict = decode_dict(players)

# Obteniendo datos de resultados
import sys
result = import_tuple("stgo2021/result.csv")
result = final_result(real_names,result)

# Obteniendo correos electrónicos
db = get_database('stgo2021/stgo0.csv')

#n = 0
for name,mail in db.items():
	body = f"""
		<h1 style="text-align: center;">Hola {one_word(str(name))}!</h1>

		<p style="text-align: center;">Un a&ntilde;o m&aacute;s utilizamos la aplicaci&oacute;n de Amigo Secreto Virtual que nos acompa&ntilde;a por 3ra vez consecutiva (ya que el papel y la memoria nos fall&oacute; esta vez jajaja).</p>

		<p style="text-align: center;"><strong>Te recuerdo que la ruleta gira s&oacute;lo una vez y los resultados del juego se guardan en archivos con valores encriptados.&nbsp;</strong></p>

		<p style="text-align: center;">Además, recuerda que definimos un <b>monto máximo de $20.000.-</b> por regalo!</p>

		<p style="text-align: center;"><br>Ahora s&iacute;, a lo importante</p>

		<div style="background-color: #31aac177 ; margin: 0 auto; border-radius: 25px; border: 1px solid skyblue; width: 80%;"> 
		<h4 style="text-align: center;">TU AMIGO SECRETO ES:<br></h4>
		<h2 style="text-align: center;"><strong>{result[name].upper()}</strong></h2>
		</div>

		<p style="text-align: center;"><small><br><br><br>Este a&ntilde;o se hicieron modificaciones menores en la aplicaci&oacute;n (nada que modifique el funcionamiento). Y se mejor&oacute; la seguridad, pensando en que me sea m&aacute;s dificil si intento averiguar qui&eacute;n es tu amigo secreto (porque me gusta el webeo nom&aacute;s).</small></p>
		<p style="text-align: center;"><small style="text-align: center;"><br>Este juego ha sido desarrollado con la tecnolog&iacute;a de</small></p>
		<p style = "text-align: center;"><a href="https://github.com/liberticl/AmigoSecreto"><img src="https://drive.google.com/uc?export=view&id=1rQgbfjTID6tR0YxEZOcrTdKd3faMZnOX" style="width: 25%;"></a></p>
		"""

	testMessage = create_message('francisco@liberti.cl', mail, 'Amigo Secreto 2021', body)
	testSend = send_message(service,'me', testMessage)
	sleep(1)
	testDelete = delete_message(service,'me',testSend['id'])
	print("Mensaje enviado a " + name + " y eliminado de la bandeja de salida.")

################################## MAIN CODE ###################################


