'''
    This is a mini Akinator
    tries to guess the superhero of marvel
'''
# DATOS DE HEROES
datos =[
   {'NOMBRE':"SPIDERMAN",'MASCULINO':True, 'MASCARA':True, 'RelAnimal': True, 'VOLAR': False, 'CAPA': False, 'OBJETO': False}, 
   {'NOMBRE':"IRON-MAN ",'MASCULINO':True, 'MASCARA':True, 'RelAnimal': False, 'VOLAR': True, 'CAPA': False, 'OBJETO': True},   
   {'NOMBRE':"CAPITANA MARVEL",'MASCULINO':False, 'MASCARA':False, 'RelAnimal': False, 'VOLAR': True, 'CAPA': False, 'OBJETO': False},
   {'NOMBRE':"VIUDA NEGRA",'MASCULINO':False, 'MASCARA':False, 'RelAnimal': True, 'VOLAR': False, 'CAPA': False, 'OBJETO': False},
   {'NOMBRE':"THOR",'MASCULINO':True, 'MASCARA':False, 'RelAnimal': False, 'VOLAR': True, 'CAPA': True, 'OBJETO': True},
   {'NOMBRE':"CAPITAN AMERICA",'MASCULINO':True, 'MASCARA':True, 'RelAnimal': False, 'VOLAR': False, 'CAPA': False, 'OBJETO': True}, 
   {'NOMBRE':"DOCTOR STRANGE",'MASCULINO':True, 'MASCARA':False, 'RelAnimal': False, 'VOLAR': True, 'CAPA': True, 'OBJETO': False},
   {'NOMBRE':"HULK",'MASCULINO':True, 'MASCARA':False, 'RelAnimal': False, 'VOLAR': False, 'CAPA': False, 'OBJETO': False},
   {'NOMBRE':"ANT-MAN",'MASCULINO':True, 'MASCARA':True, 'RelAnimal': True, 'VOLAR': True, 'CAPA': False, 'OBJETO': True},
   {'NOMBRE':"OJO DE HALCON",'MASCULINO':True, 'MASCARA':True, 'RelAnimal': True, 'VOLAR': True, 'CAPA': False, 'OBJETO': True}
]

# NOMBRE DE ATRIBUTOS DE DICCIONARIO 
keys = ['NAME', 'MASCULINO', 'MASCARA', 'RelAnimal', 'VOLAR', 'CAPA', 'OBJETO']

# lsta de preguntas que se realizan, basado en orden de atributos del diccionario
preguntas = [
    "",
    "¿TU SUPERHEROE ES DEL GENERO MASCULINO? ",
    "¿TU SUPERHEROE UTILIZA MASCARA?",
    "¿TU SUPERHEROE ESTA RELACIONADO CON ALGUN ANIMAL?",
    "¿TU SUPERHEROE PUEDE VOLAR?",
    "¿TU SUPERHEROE UTILIZA CAPA?",
    "¿TU SUPERHEROE UTILIZA ALGUN OBJETO?"
]

# esta funcion hace un filtro de los datos, elimina los diccionarios 
#   que no tienen coincidencias
def seleccionar(clave,valor):
    sel = [] # lista auxiliar para almacenar los datos filtrados
    # print("seleccionando .... ", clave , " -> ", valor)
    for i in datos:
        if i[clave] == valor:
            #print(i[clave]," -> ", valor)
            sel.append(i)
    # Limpiamos la lsita 
    datos.clear()
    # agregamos los datos seleccionados
    datos.extend(sel)

# esta funcion pide una respuesta SI - NO, 
# de insertarse lo contrarrio los hace saber y vuelve a pedir la respuesta 
def respuesta():
    answer = False # respuesta negativa por default
    while True:  # ciclo infinito
        res = input() # pedimos respuesta 
        if res.upper() == "SI":
            answer = True # se establece respuesta positiva
            break # sale del bucle
        elif res.upper() == "NO":
            answer = False # se establece respuesta negativa 
            break # sale del bucle 
        else:
            print("inserta opcion valida SI/NO")
    return answer # se retorna respuesta negativa 

print("PIENSA EN UN SUPER HEROE DE LA SAGA MARVEL...")

# recorremos la lista de preguntas, nos se cuenta ka primer pregunta 
for i in range(1,5):
    # realizamos la pregunta de acuerdo al indice
    print(preguntas[i],end=" ")
    if respuesta(): # pedimos respuesta
        seleccionar(keys[i],True) # realizamos la seleccion de acuerdo a los atributos 
    else:
        seleccionar(keys[i],False) # realizamos la seleccion de acuerdo a los atributos 
        

if datos: # SI EXISTEN DATOS (LISTA NO VACIA)
    for i in datos: # puede existir mas de un personaje parecido
        print("TU PERSONAJE ES ",i.get("NOMBRE"))
else:
    print("NO HAY COINCIDENCIAS DE SUPR HEROES!!! :C")









