#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gmail_api import *
from getting_data import *

db = get_database('planilla_2017.csv')
msje = open('mensaje.txt')

txt = ''
for line in msje:
	txt = txt + line	

msje.close()

n = 0
for name,mail in db.items():
	body = 'Hola '+str(name)+':\n\n'+txt
	testMessage = CreateMessage('andeschileong@gmail.com', mail, 'Bici-Refugio 2018', body)
	testSend = SendMessage(service, 'andeschileong@gmail.com', testMessage)
	n += 1

print "Se han intentado enviar "str(n)" correos electrónicos con éxito"

