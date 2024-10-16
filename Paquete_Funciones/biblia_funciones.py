import random



# <------------------------------------- MENÚ --------------------------------------------- >


# mensaje_menu = "Seleccione la opción: \n\n[1] para ... \n[2] para ... \n[3] para ...\n"
# mensaje_menu += "[4] para ... \n[5] para... \n[6] para ... \n"
# mensaje_menu += "[7] para ... \n[8] para... \n\nSELECCIONE: "

# while True:
#     menu = int(input(mensaje_menu))

#     match menu:
#         case 1:
#             pass    
#         case 2:
#             pass    
#         case 3:
#             pass
#         case 4:
#             pass
#         case 5:
#             pass
#         case 6:
#             pass
#         case 7:
#             pass   
#         case 8:
#             break



# <------------------------------------- MATRICES ------------------------------------------>



# Inicializar matríz
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
            
    matriz = []
        
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
        
    return matriz



# CARGAR matriz SECUENCIALMENTE
def cargar_matriz_secuencialmente(matriz:list):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f" Fila: {i} Columna {j}:  ")) 



# CARGAR matriz ALEATORIAMENTE
def cargar_matriz_aleatoriamente(matriz:list):
    
    seguir = "S"
    while seguir == "S":
#        fila = get_int("Ingrese índice de fila: ", "Error. Intente nuevamente", minimo:int, maximo:int, reintentos:int)
#        columna = get_int("Ingrese índice de columna: ", "Error. Intente nuevamente", minimo:int, maximo:int, reintentos:int)
        dato = int(input("Ingrese el dato para guardar en matríz: "))
#        matriz[fila][columna] = dato
        seguir = input("Desea seguir cargando datos? S para continuar/ N para salir: ")



# IMPRIMIR Matriz
def imprimir_matriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " | ")
        print(" ")



# BUSCAR dato en matriz
def buscar_valor_entero(matriz:list, valor:int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz == valor:
                print(f"Se encontró el dato en fila {i} columna {j} !")



# Suma absolutamente TODOS los elementos de la matriz
def sumatoria_total(matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j]
    return total 


# Suma todos los elementos de la FILA
def sumatoria_fila(matriz:list):
    suma_total_filas = []
    for i in range(len(matriz)):
        sumatoria_elementos = 0
        for j in range(len(matriz[i])):
            sumatoria_elementos += matriz[i][j]
        suma_total_filas += [sumatoria_elementos]
    return suma_total_filas



# Suma todos los elementos de la COLUMNA
def sumatoria_columna(matriz:list):
    suma_total_columna = []
    
    for j in range(len(matriz)):
        sumatoria_elementos = 0
        for i in range(len(matriz)):
            sumatoria_elementos += matriz[i][j]
        suma_total_columna += [sumatoria_elementos]
    return suma_total_columna



# Verifica igualdad en la suma total de elementos de cada fila y retorna booleano 
def verificar_igualdad_suma_de_filas(matriz:list)-> bool:
    
    for i in range(len(matriz)):
        if matriz[i] != matriz[0]:
            return False 
    return True   



# Verifica igualdad en la suma total de elementos de cada COLUMNA y retorna booleano 
def verificar_igualdad_suma_de_columnas(matriz:list)-> bool:
    
    for j in range(len(matriz)):
        if matriz[j] != matriz[0]:
            return False 
    return True   



# Verifica si el cuadrado es mágico (si tanto filas como columnas son iguales)
def es_cuadrado(matriz:list, matriz_dos:list)-> bool:
    if matriz and matriz_dos == True:
        return True
    else:
        return False




#Verificar número repetido en matriz
def verificar_numero_repetido_en_matriz(matriz:list, numero:int)->bool:
    
    bandera_numero_repetido = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                bandera_numero_repetido = True
                break
        if bandera_numero_repetido == True:
            break
    return bandera_numero_repetido




#  <------------------------------------ GET Y VALIDATES ------------------------------------------->



def validate_number(number, min, max) :
    try:
        if min <= number <= max:
            return number
        
    except ValueError:
        return None
        

def validate_lenght(str,lenght):
    try:
        if len(str) <= lenght:
            return str
        
    except ValueError:
        return None
    


def get_int(mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int):
    
    for _ in range(reintentos):
        user_input = int(input(mensaje))
        numero = validate_number(user_input,minimo,maximo)
        if numero is not None:
            return numero
        else: 
            print(mensaje_error)
    return None



def get_float(mensaje:str,mensaje_error:str,minimo:float,maximo:float,reintentos:int):
    
    for _ in range(reintentos):
        user_input = float(input(mensaje))
        numero = validate_number(user_input,minimo,maximo)
        if numero is not None:
            return numero
        else: 
            print(mensaje_error)
    return None



def get_str(mensaje:str,mensaje_error:str, longitud:int) -> str|None: 
    user_input = str(input(mensaje))
    string = validate_lenght(user_input,longitud)
    if string is not None:
        return string
    else: 
        print(mensaje_error)
    
    return None

