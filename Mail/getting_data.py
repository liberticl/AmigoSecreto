#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

def one_word(word):
	if ' ' not in word:
		return word
	else:
		splitted = word.split(" ")
		one_word = splitted[0]
	return one_word

import pandas

def get_database(file):
	table = pandas.read_csv(file)
	dict_one = table.to_dict()
	database = dict()
	print len(table)
	for i in range(len(table)):
		key = dict_one['nombre'][i]
		name = one_word(key).capitalize()
		mail = dict_one['mail'][i]
		database[name] = mail
	print len(database)
	return database


