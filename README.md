## Amigo Secreto Python

Este repositorio consta de 2 secciones:

1. Sorteo del amigo secreto.
2. Notificación a los participantes.

** Sorteo del Amigo Secreto **

El único archivo de esta sección es *secret_friend.py* y contiene todo lo necesario para generar el sorteo.
El procedimiento de uso es:

1. Indicar cantidad de jugadores
2. Indicar alias de cada jugador
3. Indicar restricciones según indica el programa
4. Se codifican los datos indicados en base64
5. Se asigna un número a cada jugador
6. Se genera el total de combinaciones posibles excluyendo pares (i,i)
7. El listado de combinaciones posibles pasa de números a alias.
8. Se aplica el listado de restricciones a las combinaciones posibles.
9. Lanzamiento de la ruleta
10. Antes de entregar un resultado, se verifica que se cumplan los requisitos y que en los cambios no surjan duplicados
11. Se exporta el resultado codificado en forma de tuplas numéricas

Cabe destacar que el sorteo considera que quien ejecuta el programa es un jugador, por eso se codifica la información.
Por otro lado, el nivel de seguridad es bajo, por ende, si se desea descubrir el detalle de amigos secretos, basta revisar dónde decodificar.

*Como idea a futuro, es posible indicar el nombre real de un jugador y un alias para que no sea necesario hacer un archivo aparte con esta información*

** Notificación a los participantes **

Se utiliza la API de Gmail para enviar correos electrónicos automáticamente. 
Para más información, revisar el link oficial (puede contener actualizaciones) de [API Gmail](https://developers.google.com/gmail/api).

Para esto se cuenta con los archivos *quickstart.py*, *gmail_api.py* y *mails.py*. Estas se encargan de obtener las credenciales para la API, proveer de las funciones necesarias y enviar los correos necesarios, respectivamente.
Para lo último se tiene considerado lo siguiente:

- Existe un archivo *mensaje.txt* con el texto del correo electrónico.
- Existe un archivo *players.csv* con la información de los participantes.
- Existe un archivo *result.csv* con el resultado obtenido en el sorteo de amigo secreto.
- Existe un archivo *stgo0.csv* con la información (nombre y correo) de cada participante.