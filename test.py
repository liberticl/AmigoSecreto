from time import *
from gmail_api import *

participante = "Participante"
secreto = "un secreto"
body = f"""
<h1 style="text-align: center;">Hola {participante}!</h1>

<p style="text-align: center;">Un a&ntilde;o m&aacute;s utilizamos la aplicaci&oacute;n de Amigo Secreto Virtual que nos acompa&ntilde;a por 3ra vez consecutiva (ya que el papel y la memoria nos fall&oacute; esta vez jajaja).</p>

<p style="text-align: center;"><strong>Te recuerdo que la ruleta gira s&oacute;lo una vez y los resultados del juego se guardan en archivos con valores encriptados.&nbsp;</strong></p>

<p style="text-align: center;"><br>Ahora s&iacute;, a lo importante</p>

<div style="background-color: #31aac177 ; margin: 0 auto; border-radius: 25px; border: 1px solid skyblue; width: 80%;"> 
<h4 style="text-align: center;">TU AMIGO SECRETO ES:<br></h4>
<h2 style="text-align: center;"><strong>{secreto.upper()}</strong></h2>
</div>

<p style="text-align: center;"><small><br><br><br>Este a&ntilde;o se hicieron modificaciones menores en la aplicaci&oacute;n (nada que modifique el funcionamiento). Y se mejor&oacute; la seguridad, pensando en que me sea m&aacute;s dificil si intento averiguar qui&eacute;n es tu amigo secreto (porque me gusta el webeo nom&aacute;s).</small></p>
<p style="text-align: center;"><small style="text-align: center;">Este juego ha sido desarrollado con la tecnolog&iacute;a de</small></p>
<p style = "text-align: center;"><img src="https://drive.google.com/uc?export=view&id=1rQgbfjTID6tR0YxEZOcrTdKd3faMZnOX" style="width: 40%;"></p>

"""

testMessage = create_message('francisco@liberti.cl', 'francisco.vergara.12@sansano.usm.cl', 'Probando', body)
testSend = send_message(service,'me', testMessage)
sleep(1)
testDelete = delete_message(service,'me',testSend['id'])
print("Mensaje enviado a " + participante + " y eliminado de la bandeja de salida.")