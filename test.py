from time import *
from gmail_api import *

name = "Panchito"
body = f"""
<html>
<h1> HOLA </h1>
<p>
Hola {name}:\n\nProbando
</p>
</html>
"""
testMessage = create_message('francisco@liberti.cl', 'francisco.vergara.12@sansano.usm.cl', 'Probando', body)
testSend = send_message(service,'me', testMessage)
sleep(1)
testDelete = delete_message(service,'me',testSend['id'])
print("Mensaje enviado a " + name + " y eliminado de la bandeja de salida.")