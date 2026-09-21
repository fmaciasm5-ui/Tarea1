# 1. Validador de notas con promedio
# Paso 1 — Entender el problema (EPS)
# Entrada: Notas sueltas o en lote, algunas fuera de rango.
# Proceso: Validar cada nota una por una; si es válida, agregarla a la lista interna; al final, sumar y dividir entre la cantidad para el promedio.
# Salida: Lista de notas válidas y el promedio de esas notas.
# Paso 2 - Bosquejo a mano
# Datos: 85, 92, 110, -5, 78, 88
# ¿85 es válida?   0 ≤ 85 ≤ 100  -> SÍ  -> lista = [85]
# ¿92 es válida?   0 ≤ 92 ≤ 100  -> SÍ  -> lista = [85, 92]
# ¿110 es válida?  0 ≤ 110 ≤ 100 -> NO  -> se descarta
# ¿-5 es válida?   0 ≤ -5 ≤ 100  -> NO  -> se descarta
# ¿78 es válida?   0 ≤ 78 ≤ 100  -> SÍ  -> lista = [85, 92, 78]
# ¿88 es válida?   0 ≤ 88 ≤ 100  -> SÍ  -> lista = [85, 92, 78, 88]
#promedio = (85+92+78+88) / 4 = 343 / 4 = 85.75
# Paso 3 - Descubrir el patron
# Lo que se repite: la validación (0 ≤ nota ≤ 100) es siempre la misma prueba, por eso vive en su propio método validar_nota.
# Lo que cambia: la cantidad de notas que llegan de una sola vez — por eso cargar_notas usa *args y llama a validar_nota una vez por cada elemento, en lugar de repetir el if muchas veces.
# Paso 4 - Codigo
class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        if nota >=0 and nota <= 100:
            return True
        else:
            return False
        #return 0 <= nota <= 100
    
    def cargar_notas(self,*args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-60,80,40,200))
print(cal.promedio())
# Paso 5 - Prueba de escritorio
# Acción	                         self.notas	             Salida
# c = Calificador()	                 []	                     —
# cargar_notas(85,92,110,78,-5,88)	 [85, 92, 78, 88]	     [85, 92, 78, 88]
# promedio()	                     [85, 92, 78, 88]	     85.75

# 2. Contador de palabras unicas
# Paso 1 - Entender el problema (EPS)
# Entrada: Palabras sueltas o en lote, algunas repetidas.
# Proceso: Cada palabra se agrega a un conjunto (elimina duplicados automáticamente) y a una lista (conserva el orden de llegada).
# Salida: Cantidad de palabras únicas.
# Paso 2 - Bosquejo a mano
# Datos: "hola", "mundo", "hola"
# agregar_palabra("hola")  -> conjunto = {"hola"}          lista = ["hola"]
# agregar_palabra("mundo") -> conjunto = {"hola","mundo"}  lista = ["hola","mundo"]
# agregar_palabra("hola")  -> conjunto sigue igual (ya estaba) lista = ["hola","mundo","hola"]
# contar_palabras() = len(conjunto) = 2
# Paso 3 - Descubrir el patron 
# Lo que se repite: la acción de "guardar una palabra" es siempre la misma, por eso agregar_multiples no reescribe la lógica, solo hace un bucle que llama a agregar_palabra.
# Lo que cambia: cuántas palabras llegan de una vez. El conjunto resuelve la unicidad; la lista resuelve el orden — son dos colecciones para dos necesidades distintas sobre el mismo dato.
# Paso 4 - Codigo

class AnalizadorTexto:
    def __init__(self):
        self.unicas = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        self.unicas.add(palabra)
        self.orden.append(palabra)

    def contar_palabra(self):
        return len(self.unicas)
    
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola", "mundo", "como estas")
print(f"Palabras unicas: {at.contar_palabra()}")
print(f"Orden de llegada: {at.orden}")
# Paso 5 — Prueba de escritorio
# Acción	                                     self.unicas	     self.orden
# at = AnalizadorTexto()	                     set()	             []
# agregar_multiples("hola","mundo","hola")	     {"hola","mundo"}	 ["hola","mundo","hola"]
# contar_palabras()	                             {"hola","mundo"}	 → 2

# 3. Gestor de compras con totales
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre y precio de cada artículo.
# Proceso: Guardar cada par nombre→precio en un diccionario; sumar los valores para el total; filtrar por rango de precio recorriendo items().
# Salida: Total del carrito y lista de artículos filtrados.
# Paso 2 - Bosquejo a mano
# agregar_articulo("pan", 2.50)   -> dict = {"pan": 2.50}
# agregar_articulo("leche", 3.00) -> dict = {"pan": 2.50, "leche": 3.00}
# total_carrito() = 2.50 + 3.00 = 5.50
# articulos_por_rango(2.00, 3.00):
# "pan"   -> 2.50 está en [2.00, 3.00] -> SÍ
# "leche" -> 3.00 está en [2.00, 3.00] -> SÍ
# -> ["pan", "leche"]
# Paso 3 - Descubrir el patron 
# El diccionario es el "almacén" natural cuando cada dato tiene una clave única 
# (el nombre del artículo) asociada a un valor (el precio). 
# total_carrito y articulos_por_rango no repiten la lógica de guardado: 
# solo leen lo que ya está en self.articulos de dos formas distintas (sumar vs. filtrar).
# Paso 4 - Codigo
class CarroCompras():
    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio
    
    def total_carrito(self):
        return sum(self.articulos.values())
    
    def articulos_por_rango(self, precio_min, precio_max):
        return [nombre for nombre, precio in self.articulos.items()
                if precio_min <= precio <= precio_max]

c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
print(f"Total: {c.total_carrito()}")
print(f"Entre 2.00 y 3.00: {c.articulos_por_rango(2.00, 3.00)}")
# Paso 5 _ Prueba de escritorio 
# Acción	                        self.articulos	                 Salida
# c = CarroCompras()	            {}	                             —
# agregar_articulo("pan",2.50)	    {"pan": 2.50}	                 —
# agregar_articulo("leche",3.00)	{"pan": 2.50, "leche": 3.00}	 —
# total_carrito()	                {"pan": 2.50, "leche": 3.00}	 5.50

# 4. Inversor de secuencias
# Paso 1 - Entender el problema (EPS)
# Entrada: Una lista, o varias listas a la vez.
# Proceso: Recorrer la lista de atrás hacia adelante con un índice manual, construyendo una lista nueva; para varias listas, repetir el proceso y guardar cada resultado en un diccionario (usando tuplas como clave, porque una lista no puede ser clave de diccionario).
# Salida: Lista invertida, o diccionario con varias listas invertidas.
# Paso 2 — Bosquejo a mano
# Datos: [1, 2, 3]   (largo = 3, índices válidos 0,1,2)
# i = 2 -> lista[2] = 3 -> invertida = [3]
# i = 1 -> lista[1] = 2 -> invertida = [3, 2]
# i = 0 -> lista[0] = 1 -> invertida = [3, 2, 1]
# Resultado: [3, 2, 1] 
# Paso 3 — Descubrir el patrón
# Lo que se repite: recorrer una lista de atrás hacia adelante siempre usa el mismo truco de índices (range(len(lista)-1, -1, -1)). 
# Lo que cambia: cuántas listas llegan; invertir_multiples no vuelve a escribir el bucle de inversión, solo llama a invertir_lista una vez por cada lista recibida.
# Paso 4 - Codigo
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
            resultado[tuple(lista)] = self.invertir_lista(lista)
        return resultado

inv = InversorSecuencia()
print(inv.invertir_lista([1, 2, 3]))
print(inv.invertir_multiples([1, 2, 3], [4, 5]))
# Paso 5 — Prueba de escritorio
# i	   lista[i]	  invertida
# 2	   3	      [3]
# 1	   2	      [3, 2]
# 0	   1	      [3, 2, 1]

# 5. Detector de números pares e impares
# Paso 1 - Entender el problema (EPS) 
# Entrada: Varios números en un solo lote.
# Proceso: Para cada número, preguntar si es par con el operador %; según la respuesta, agregarlo a la lista correspondiente dentro del diccionario.
# Salida: Diccionario clasificado y tupla con las cantidades.
# Paso 2 — Bosquejo a mano
# Datos: 1, 2, 3, 4, 5
# 1 % 2 = 1 -> impar -> impares=[1]
# 2 % 2 = 0 -> par   -> pares=[2]
# 3 % 2 = 1 -> impar -> impares=[1,3]
# 4 % 2 = 0 -> par   -> pares=[2,4]
# 5 % 2 = 1 -> impar -> impares=[1,3,5]
# Resultado: {'pares':[2,4], 'impares':[1,3,5]}
# cantidad_pares_impares() = (2, 3)
# Paso 3 - Buscar el patron 
# es_par encapsula la única pregunta que se repite (numero % 2 == 0); separar no vuelve a escribir esa condición, solo la usa dentro de un if/else para decidir en qué lista del diccionario cae cada número. 
# Guardar el último resultado en un atributo permite que cantidad_pares_impares no tenga que recibir los números de nuevo.
# Paso 4 - Codigo
class AnalizadorNumeros:
    def __init__(self):
        self.ultimo_resultado = {'pares': [], 'impares': []}

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        resultado = {'pares': [], 'impares': []}
        for numero in numeros:
            if self.es_par(numero):
                resultado['pares'].append(numero)
            else:
                resultado['impares'].append(numero)
        self.ultimo_resultado = resultado
        return resultado

    def cantidad_pares_impares(self):
        return (len(self.ultimo_resultado['pares']),
                len(self.ultimo_resultado['impares']))

an = AnalizadorNumeros()
print(an.separar(1, 2, 3, 4, 5))
print(an.cantidad_pares_impares())
# Paso 5 - Prueba de escritorio
# Número	es_par()	pares	impares
# 1	False	[]	[1]
# 2	True	[2]	[1]
# 3	False	[2]	[1, 3]
# 4	True	[2, 4]	[1, 3]
# 5	False	[2, 4]	[1, 3, 5]

# 6. Estadísticas de temperatura
# Paso 1 - Entender el problema (EPS)
# Entrada: Temperaturas sueltas o en lote.
# Proceso: Guardar cada temperatura en una lista; usar las funciones nativas min, max, sum/len sobre esa lista para las estadísticas.
# Salida: Mínima, máxima y promedio de las temperaturas registradas.
# Paso 2 - Bosquejo a mano
# Datos: 20, 25, 18, 30
# lista = [20, 25, 18, 30]
# mínima  = 18
# máxima  = 30
# promedio = (20+25+18+30)/4 = 93/4 = 23.25
# Paso 3 - Buscar el patron
# registrar_temperatura hace una sola cosa (agregar a la lista); registrar_multiples no repite esa lógica, solo hace un bucle que la llama una vez por cada valor recibido. 
# Las tres estadísticas reutilizan la misma lista self.temperaturas, cada una mirándola de una forma distinta.
# Paso 4 - Codigo
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)
    
    def maxima(self):
        return max(self.temperaturas)
    
    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)
    
    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

gt = GestorTemperatura()
gt.registrar_multiples(20,25,18,30)
print(gt.promedio())
print(f"Mínima: {gt.minima()}  Máxima: {gt.maxima()}")
# Paso 5 - Prueba de escritorio
#Acción	                            self.temperaturas	Salida
# gt = GestorTemperatura()	        []	                —
# registrar_multiples(20,25,18,30)	[20, 25, 18, 30]	—
# minima()	                        [20, 25, 18, 30]	18
# maxima()	                        [20, 25, 18, 30]	30
# promedio()	                    [20, 25, 18, 30]	23.25

# 7. Mapeador de edades
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre y edad de cada persona.
# Proceso: Guardar en un diccionario nombre→edad; filtrar recorriendo items(); promediar con sum/len sobre los valores.
# Salida: Lista de nombres filtrados y promedio de edad.
# Paso 2 - Bosquejo a mano
# agregar_persona("Ana", 28) -> dict = {"Ana": 28}
# agregar_persona("Bob", 17) -> dict = {"Ana": 28, "Bob": 17}
# personas_mayores(18):
#   "Ana" -> 28 >= 18 -> SÍ
#   "Bob" -> 17 >= 18 -> NO
#   -> ["Ana"]
# Paso 3 - Buscar el patron
# El diccionario asocia cada nombre (clave única) con su edad (valor); personas_mayores no necesita una nueva estructura, solo recorre items() con un if y arma una lista con los nombres que cumplen la condición.
# Paso 4 - Codigo
class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado
    
    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)

gp = GestorPersonas()
gp.agregar_persona("Ana", 28)
gp.agregar_persona("Bob", 17)
print(gp.personas_mayores(18))
print(gp.edad_promedio())
# Paso 5 - Prueba de escritorio
# Acción	                 self.personas	          Salida
# gp = GestorPersonas()	     {}	                      —
# agregar_persona("Ana",28)	 {"Ana": 28}	          —
# agregar_persona("Bob",17)	 {"Ana": 28, "Bob": 17}	  —
# personas_mayores(18)	     {"Ana": 28, "Bob": 17}	  ["Ana"]

# 8. Asignador de equipos
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombres de equipos y jugadores.
# Proceso: Crear la entrada del equipo con lista vacía; agregar jugadores a esa lista; comparar longitudes de todas las listas para encontrar la mayor.
# Salida: Nombre del equipo con más integrantes.
# Paso 2 - Bosquejo a mano
# crear_equipo("A")            -> dict = {"A": []}
# agregar_jugador("A","Juan")  -> dict = {"A": ["Juan"]}
# agregar_jugador("A","Pedro") -> dict = {"A": ["Juan","Pedro"]}
# Si además hubiera crear_equipo("B") con un solo jugador,
# equipo_mayor_integrantes() compararía len(["Juan","Pedro"])=2 vs len(["X"])=1
# -> "A" gana
# Paso 3 - Buscar el patron
# Este es un diccionario de listas (estructura anidada): cada clave (equipo) apunta a una colección propia (sus jugadores). agregar_jugador no crea listas nuevas cada vez, reutiliza la que crear_equipo ya dejó lista.
# Paso 4 - Codigo
class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = ""
        cantidad_mayor = 0
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > cantidad_mayor:
                cantidad_mayor = len(jugadores)
                mayor = equipo
        return mayor

eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A", "Juan")
eq.agregar_jugador("A", "Pedro")
eq.crear_equipo("B")
eq.agregar_jugador("B", "Luis")
print(eq.equipos)
print(eq.equipo_mayor_integrantes())
# Paso 5 - Prueba de escritorio
# Acción	self.equipos
# eq = Equipos()	              {}
# crear_equipo("A")	              {"A": []}
# agregar_jugador("A","Juan")	  {"A": ["Juan"]}
# agregar_jugador("A","Pedro")	  {"A": ["Juan","Pedro"]}
# crear_equipo("B"); 
# agregar_jugador("B","Luis")	  {"A": ["Juan","Pedro"], "B": ["Luis"]}
# equipo_mayor_integrantes()	  → "A"

# 9. Validador de caracteres
# Paso 1 - Entender el problema (EPS)
# Entrada: Un texto con letras y/o dígitos.
# Proceso: Recorrer carácter por carácter; si es letra, preguntar si es vocal (reutilizando solo_vocales) para clasificarla; si es dígito, contarlo aparte; de paso, comparar el largo del texto contra el más largo guardado.
# Salida: Diccionario con los tres conteos.
# Paso 2 - Bosquejo a mano
# Texto: "Hola123"
# H -> letra, no vocal -> consonantes=1
# o -> letra, vocal     -> vocales=1
# l -> letra, no vocal -> consonantes=2
# a -> letra, vocal     -> vocales=2
# 1 -> dígito           -> digitos=1
# 2 -> dígito           -> digitos=2
# 3 -> dígito           -> digitos=3
# Resultado: {'vocales':2, 'consonantes':2, 'digitos':3}
# Paso 3 - Buscar el patron
# solo_vocales encapsula la única pregunta que se repite letra por letra; contar_por_tipo no vuelve a escribir la lista de vocales adentro de un if gigante, solo llama a solo_vocales dentro del bucle. 
# Guardar el texto más largo es un efecto secundario que se actualiza cada vez que se analiza un texto nuevo, sin necesitar un método aparte.
# Paso 4 - Codigo
class AnalizadorString():
    def __init__(self):
        self.texto_mas_largo = " "
    
    def solo_vocales(self, letra):
        if letra in "aeiouAEIOU":
            return True
        else:
            return False
    
    def contar_por_tipo(self,texto):
        vocales = 0
        consonantes = 0
        digitos = 0
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        
        for letra in texto:
            if self.solo_vocales(letra):
                vocales = vocales + 1
            elif letra.isdigit():
                digitos = digitos + 1
            elif letra.isalpha():
                consonantes = consonantes + 1

        return {'vocales': vocales, 'consonantes': consonantes, 'digitos': digitos}

astr = AnalizadorString()
print(astr.contar_por_tipo("Hola123"))
print(f"Texto más largo analizado: {astr.texto_mas_largo}")
# Paso 5 - Prueba de escritorio
# Carácter	Tipo	    vocales	consonantes	digitos
# H	        consonante	0	    1	        0
# o	        vocal	    1	    1	        0
# l	        consonante	1	    2	        0
# a	        vocal	    2	    2	        0
# 1	        dígito	    2	    2	        1
# 2	        dígito	    2	    2	        2
# 3 	    dígito	    2	    2	        3

# 10. Gestor de tareas con prioridad
# Paso 1 - Entender el problema (EPS)
# Entrada: Descripción y prioridad de cada tarea.
# Proceso: Guardar cada tarea como una tupla (descripción, prioridad) dentro de una lista; filtrar por el segundo elemento de la tupla para las prioritarias; reconstruir la lista sin la tarea eliminada.
# Salida: Lista de tareas de prioridad alta.
# Paso 2 - Bosquejo a mano
# agregar_tarea("Estudiar","alta") -> lista = [("Estudiar","alta")]
# agregar_tarea("Leer","baja")     -> lista = [("Estudiar","alta"), ("Leer","baja")]
# tareas_prioritarias():
# ("Estudiar","alta") -> prioridad == "alta" -> SÍ
# ("Leer","baja")     -> prioridad == "alta" -> NO
# -> [("Estudiar","alta")]
# Paso 3 - Buscar el patron
# Cada tarea es una tupla porque sus dos datos (descripción y prioridad) viajan siempre juntos y no necesitan cambiar de forma independiente — por eso tupla y no lista. tareas_prioritarias y eliminar_completada no repiten la forma de guardar tareas, solo recorren la misma lista con un filtro distinto cada vez.
# Paso 4 - Codigo
class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for tarea in self.tareas:
            if tarea [1] == "alta":
                resultado.append(tarea)

        return resultado
    
    def eliminar_completada(self, descripcion):
        for tarea in self.tareas:

            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                return True
            
        return False

t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
print(t.tareas_prioritarias())
t.eliminar_completada("Leer")
print(t.tareas)
# Paso 5 - Prueba de escritorio
# Acción	                         self.tareas	                        Salida
# t = Tareas()	                     []	                                    —
# agregar_tarea("Estudiar","alta")   [("Estudiar","alta")]	                —
# agregar_tarea("Leer","baja")	     [("Estudiar","alta"),("Leer","baja")]	—
# tareas_prioritarias()	             [("Estudiar","alta"),("Leer","baja")]	[("Estudiar","alta")]
# eliminar_completada("Leer")	     [("Estudiar","alta")]	                —

# 11. Contador de frecuencia
# Paso 1 - Entender el problema (EPS)
# Entrada: Elementos sueltos o en lote (pueden repetirse).
# Proceso: Por cada elemento, aumentar en 1 su contador dentro del diccionario (o crearlo en 0+1 si es la primera vez); comparar los contadores para hallar el máximo.
# Salida: Elemento más frecuente y su conteo.
# Paso 2 - Bosquejo a mano
# agregar_elemento("a") -> dict = {"a": 1}
# agregar_elemento("b") -> dict = {"a": 1, "b": 1}
# agregar_elemento("a") -> dict = {"a": 2, "b": 1}
# elemento_mas_frecuente() -> compara 2 vs 1 -> "a"
# frecuencia_elemento("a") -> 2
# Paso 3 - Buscar el patron
# El diccionario funciona como "contador": la clave es el elemento y el valor es cuántas veces se ha visto. 
# self.frecuencias.get(elemento, 0) + 1 es el truco que evita un if elemento in diccionario explícito.
# Este patrón (diccionario-contador) es de los más comunes en programación con colecciones.
# Paso 4 - Codigo
class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
         self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        mayor = None
        cantidad_mayor = 0
        for elemento, cantidad in self.frecuencias.items():
            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                mayor = elemento

        return mayor

    def frecuencia_elemento(self, elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0

cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))
# Paso 5 - Prueba de escritorio
# Acción	                     self.frecuencias	Salida
# cf = ContadorFrecuencia()	     {}	                —
# agregar_elemento("a")	         {"a": 1}	        —
# agregar_elemento("b")	         {"a": 1, "b": 1}	—
# agregar_elemento("a")	         {"a": 2, "b": 1}	—
# elemento_mas_frecuente()	     {"a": 2, "b": 1}	"a"

# 12. Selector de rango con tuplas
# Paso 1 - Entender el problema (EPS)
# Entrada: Pares (inicio, fin) para uno o varios rangos.
# Proceso: Convertir cada rango en una tupla de números; juntar todas las tuplas dentro de un conjunto para eliminar los que se repiten entre rangos; ordenar el resultado para presentarlo como lista.
# Salida: Lista de números únicos combinando todos los rangos.
# Paso 2 - Bosquejo a mano
# crear_rango(1,3) -> (1, 2, 3)
# crear_rango(2,4) -> (2, 3, 4)
# conjunto = {} 
# update((1,2,3)) -> {1,2,3}
# update((2,3,4)) -> {1,2,3,4}   (el 2 y el 3 no se duplican)
# sorted(conjunto) = [1, 2, 3, 4]
# Paso 3 - Buscar el patron
# crear_rango resuelve un solo rango; 
# elementos_en_multiples_rangos no repite esa fórmula, 
# solo la llama una vez por cada tupla (inicio,fin) recibida vía *rangos, 
# y usa un conjunto (set().update(...))para que los rangos que se solapan 
# no dupliquen números en el resultado final.
# Paso 4 - Codigo
class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        combinados = set()
        for inicio, fin in rangos:
            combinados.update(self.crear_rango(inicio, fin))
        return sorted(combinados)

sr = SelectorRango()
print(sr.crear_rango(1, 3))
print(sr.elementos_en_multiples_rangos((1, 3), (2, 4)))
# Paso 5 - Prueba de escritorio
# Acción	                            combinados (set)	Salida
# combinados = set()	                set()	            —
# update(crear_rango(1,3)) = (1,2,3)	{1, 2, 3}	        —
# update(crear_rango(2,4)) = (2,3,4)	{1, 2, 3, 4}	    —
# sorted(combinados)	                {1, 2, 3, 4}	    [1, 2, 3, 4]

# 13. Combinador de listas
# Paso 1 - Entender el problema (EPS)
# Entrada: Dos o más listas.
# Proceso: Recorrer con un índice común a ambas listas, tomando primero el elemento de la lista1 y luego el de la lista2 en cada posición; para más de dos listas, ir intercalando el resultado acumulado con la siguiente.
# Salida: Lista con los elementos alternados.
# Paso 2 - Bosquejo a mano
# lista1 = [1, 2]   lista2 = [3, 4]
# i=0: tomar lista1[0]=1 -> resultado=[1]; tomar lista2[0]=3 -> resultado=[1,3]
# i=1: tomar lista1[1]=2 -> resultado=[1,3,2]; tomar lista2[1]=4 -> resultado=[1,3,2,4]
# Resultado: [1, 3, 2, 4]
# Paso 3 - Buscar el patron
# intercalar resuelve el caso de dos listas con un solo bucle por índice
# (cuidando que las listas puedan tener distinto largo). 
# intercalar_multiples no reinventa esa lógica: va acumulando el resultado parcial 
# y lo vuelve a intercalar con la siguiente lista, reutilizando intercalar una y otra vez.
# Paso 4 - Codigo
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):    
        resultado = list(listas[0])
        for siguiente in listas[1:]:
            resultado = self.intercalar(resultado, siguiente)
        return resultado

cl = CombinadorListas()
print(cl.intercalar([1, 2], [3, 4]))
print(cl.intercalar_multiples([1, 2], [3, 4], [5, 6]))
# Paso 5 - Prueba de escritorio
# i	  lista1[i]	  lista2[i]	  resultado
# 0	  1	          3	          [1, 3]
# 1	  2	          4	          [1, 3, 2, 4]

# 14. Mapeo de estudiantes a notas
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre de estudiante y su nota.
# Proceso: Guardar en un diccionario nombre→nota; filtrar recorriendo items() para los aprobados; usar max(..., key=...) sobre las claves para encontrar al mejor.
# Salida: Lista de aprobados y tupla (nombre, nota) del mejor.
# Paso 2 - Bosquejo a mano
# registrar("Ana", 95) -> dict = {"Ana": 95}
# registrar("Bob", 70) -> dict = {"Ana": 95, "Bob": 70}
# mejor_estudiante():
# comparar 95 vs 70 -> "Ana" tiene la mayor
# -> ("Ana", 95)
# Paso 3 - Buscar el patron
# lo que se repite es recorrer el diccionario con for estudiante, nota in self.notas.items(); 
# lo que cambia es qué se hace con cada vuelta 
# estudiantes_aprobados filtra y acumula todos los que cumplen en una lista, 
# mientras mejor_estudiante compara y se queda solo con el mejor actualizando un récord.
# Paso 4 - Codigo
class RegistroNotas:
    def __init__(self):
        self.notas = {}

    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        est_aprobados = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                est_aprobados.append(estudiante)

        return est_aprobados

    def mejor_estudiante(self):
        mejor_nombre = ""
        mejor_nota = 0
        for estudiante, nota in self.notas.items():
            if nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante

        return (mejor_nombre, mejor_nota)

rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.registrar("Luis", 88)
print(rn.notas)
print(rn.estudiantes_aprobados(70))
print(rn.mejor_estudiante())
# Paso 5 - Prueba de escritorio
# Acción	            self.notas	            Salida
# rn = RegistroNotas()	{}	                    —
# registrar("Ana",95)	{"Ana": 95}         	—
# registrar("Bob",70)	{"Ana": 95, "Bob": 70}	—
# mejor_estudiante()	{"Ana": 95, "Bob": 70}  ("Ana", 95)

# 15. Divisores de un número
# Paso 1 - Entender el problema (EPS)
# Entrada: Uno o varios números.
# Proceso: Probar cada número desde 1 hasta el número mismo, y si divide exactamente (resto 0), guardarlo; para números perfectos, sumar todos los divisores excepto el propio número y compararla con él.
# Salida: Tupla de divisores, booleano de perfecto, o diccionario para varios números.
# Paso 2 - Bosquejo a mano
# numero = 12
# i=1  -> 12%1=0  -> divisores=[1]
# i=2  -> 12%2=0  -> divisores=[1,2]
# i=3  -> 12%3=0  -> divisores=[1,2,3]
# i=4  -> 12%4=0  -> divisores=[1,2,3,4]
# i=6  -> 12%6=0  -> divisores=[1,2,3,4,6]
# i=12 -> 12%12=0 -> divisores=[1,2,3,4,6,12]
# (el resto de i no dividen exacto)
# Resultado: (1, 2, 3, 4, 6, 12)
# Para es_perfecto(6): divisores propios = 1+2+3 = 6 -> True (6 es perfecto)
# Paso 3 - Buscar el patron
# encontrar_divisores es el método base que se reutiliza dos veces: 
# es_perfecto lo llama y solo cambia qué hace con el resultado (sumar y comparar), 
# y encontrar_multiples_divisores lo llama una vez por cada número recibido con *args, 
# guardando cada tupla en un diccionario.
# Paso 4 - Codigo
class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma_propios = sum(d for d in divisores if d != numero)
        return suma_propios == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for numero in numeros:
            resultado[numero] = self.encontrar_divisores(numero)
        return resultado

df = DivisorFinder()
print(df.encontrar_divisores(12))
print(df.es_perfecto(6), df.es_perfecto(12))
print(df.encontrar_multiples_divisores(6, 12))
# Paso 5 - Prueba de escritorio
# i	12 % i	¿Divide?	divisores
# 1	0	SÍ	[1]
# 2	0	SÍ	[1, 2]
# 3	0	SÍ	[1, 2, 3]
# 4	0	SÍ	[1, 2, 3, 4]
# 6	0	SÍ	[1, 2, 3, 4, 6]
# 12	0	SÍ	[1, 2, 3, 4, 6, 12]

# 16. Codificador/Decodificador
# Paso 1 - Entender el problema (EPS)
# Entrada: Letra o palabra, y un desplazamiento (1 a 25).
# Proceso: Convertir la letra a su posición en el alfabeto (ord(letra) - ord('a')), sumarle el desplazamiento, aplicar % 26 para que "dé la vuelta" al llegar a la 'z', y convertir de regreso a letra con chr.
# Salida: Letra o palabra codificada; el historial queda guardado en un diccionario.
# Paso 2 - Bosquejo a mano
# palabra = "hola", desplazamiento = 3   (alfabeto: a=0, b=1, ..., z=25)
# h -> posición 7  -> (7+3)%26=10  -> letra 10 = 'k'
# o -> posición 14 -> (14+3)%26=17 -> letra 17 = 'r'
# l -> posición 11 -> (11+3)%26=14 -> letra 14 = 'o'
# a -> posición 0  -> (0+3)%26=3   -> letra 3  = 'd'
# Resultado real: "krod"
# Paso 3 - Buscar el patron
# codificar_letra resuelve la fórmula matemática para una sola letra (incluyendo mayúsculas, con letra.isupper() para elegir la base correcta); 
# codificar_palabra no repite esa fórmula, solo recorre la palabra letra por letra llamando a codificar_letra, 
# y de paso guarda el resultado en el diccionario de historial.
# Paso 4 - Codigo
class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        base = ord('A') if letra.isupper() else ord('a')
        return chr((ord(letra) - base + desplazamiento) % 26 + base)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = "".join(
            self.codificar_letra(letra, desplazamiento) for letra in palabra
        )
        self.historial[palabra] = resultado
        return resultado

cc = CodificadorCesar()
print(cc.codificar_palabra("hola", 3))
print(cc.historial)
# Paso 5 - Prueba de escritorio
# Letra 	Posición	(pos+3)%26	 Letra resultado
# h	        7	         10	         k
# o	        14	         17	         r
# l	        11	         14	         o
# a	        0	         3	         d

# 17. Grupo de edades
# Paso 1 - Entender el problema (EPS)
# Entrada: Edades sueltas o en lote.
# Proceso: Clasificar cada edad con una cadena de if/elif según rangos; agregarla a la lista de su categoría dentro de un diccionario.
# Salida: Diccionario agrupado por categoría, y promedio de una categoría.
# Paso 2 - Bosquejo a mano
# Rangos usados: niño 0-11, adolescente 12-17, adulto 18-64, mayor 65+
# edad=5  -> 5<=11        -> "niño"
# edad=15 -> 12<=15<=17   -> "adolescente"
# edad=30 -> 18<=30<=64   -> "adulto"
# edad=70 -> 70>64        -> "mayor"
# Resultado: {'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}
# Paso 3 - Buscar el patron
# clasificar_edad concentra la única decisión que se repite (a qué categoría pertenece una edad); agrupar_por_categoria no repite esos if, solo llama a clasificar_edad por cada edad recibida y usa el resultado como clave para saber en qué lista del diccionario debe agregarla.
# Paso 4 - Codigo
class AgrupadorEdades:
    def clasificar_edad(self, edad):
        if edad <= 11:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        grupos = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            grupos[categoria].append(edad)
        return grupos
    
    def edad_promedio_categoria(self, categoria, *edades):
        grupos = self.agrupar_por_categoria(*edades)
        lista = grupos.get(categoria, [])
        return sum(lista) / len(lista) if lista else 0

ae = AgrupadorEdades()
print(ae.agrupar_por_categoria(5, 15, 30, 70))
print(ae.edad_promedio_categoria("adulto", 5, 15, 30, 70, 40))
# Paso 5 - Prueba de escritorio
# Edad	clasificar_edad()	grupos
# 5	niño	{'niño':[5]}
# 15	adolescente	{'niño':[5], 'adolescente':[15]}
# 30	adulto	{..., 'adulto':[30]}
# 70	mayor	{..., 'mayor':[70]}

# 18. Matriz de distancias
# Paso 1 - Entender el problema (EPS)
# Entrada: Puntos como tuplas (x, y).
# Proceso: Aplicar la fórmula de distancia euclidiana √((x2-x1)²+(y2-y1)²); guardar cada resultado en una lista; comparar las distancias a varios puntos para encontrar el mínimo.
# Salida: Distancia numérica y el punto más cercano.
# Paso 2 - Bosquejo a mano
# p1=(0,0), p2=(3,4)
# dx = 3-0 = 3
# dy = 4-0 = 4
# distancia = sqrt(3² + 4²) = sqrt(9+16) = sqrt(25) = 5.0
# Paso 3 - Buscar el patron
# distancia_euclidiana resuelve el cálculo para un solo par de puntos (y de paso lo guarda en self.distancias_calculadas, así el historial crece solo con el uso normal del método). punto_mas_cercano no repite la fórmula: usa min(puntos, key=...) para comparar, y esa función key es justamente una llamada a distancia_euclidiana por cada punto candidato.
# Paso 4 - Codigo
class CalculadorDistancia:
    def __init__(self):
        self.distancias_calculadas = []

    def distancia_euclidiana(self, p1, p2):
        distancia = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        self.distancias_calculadas.append(distancia)
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        punto_cercano = None
        distancia_menor = None
        for punto in puntos:
            distancia = self.distancia_euclidiana(referencia, punto)
            if distancia_menor is None or distancia < distancia_menor:
                distancia_menor = distancia
                punto_cercano = punto

        return punto_cercano

cd = CalculadorDistancia()
print(cd.distancia_euclidiana((0, 0), (3, 4)))
print(cd.distancias_calculadas)
# Paso 5 - Prueba de escritorio
# Acción	distancia	self.distancias_calculadas
# distancia_euclidiana((0,0),(3,4))	5.0	[5.0]
# comparar (10,10) al recorrer min()	√200 ≈ 14.14	[5.0, 14.14]
# comparar (1,1)	√2 ≈ 1.41	[5.0, 14.14, 1.41]
# comparar (5,5)	√50 ≈ 7.07	[5.0, 14.14, 1.41, 7.07]

# 19. Inventario de productos
# Paso 1 - Entender el problema (EPS)
# Entrada: Producto y cantidad a agregar o restar.
# Proceso: Sumar o restar sobre el valor guardado en el diccionario, validando que no se reste más de lo que hay; filtrar el diccionario buscando cantidades por debajo de un mínimo.
# Salida: True/False según si la resta fue posible, y lista de productos con poco stock.
# Paso 2 - Bosquejo a mano
# agregar_stock("pan", 50) -> dict = {"pan": 50}
# restar_stock("pan", 30):
# ¿50 >= 30? SÍ -> dict = {"pan": 20} -> retorna True
# productos_bajo_stock(25):
# "pan" -> 20 < 25 -> SÍ -> ["pan"]
# Paso 3 - Buscar el patron
# restar_stock valida antes de modificar (if self.stock.get(producto,0) >= cantidad), evitando dejar cantidades negativas — ese if es la parte que "cambia" el comportamiento normal de restar directamente. productos_bajo_stock reutiliza el mismo diccionario con un filtro de items(), igual que en otros ejercicios con diccionarios.
# Paso 4 - Codigo
class Inventario:
    def __init__(self):
        self.stock = {} 

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        resultado = []
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)

        return resultado

inv = Inventario()
inv.agregar_stock("pan", 50)
print(inv.restar_stock("pan", 30))
print(inv.stock)
print(inv.productos_bajo_stock(25))
# Paso 5 - Prueba de escritorio
# Acción	self.stock	Salida
# inv = Inventario()	{}	—
# agregar_stock("pan",50)	{"pan": 50}	—
# restar_stock("pan",30)	{"pan": 20}	True
# productos_bajo_stock(15)	{"pan": 20}	[] (20 no es < 15)
# productos_bajo_stock(25)	{"pan": 20}	["pan"] (20 sí es < 25)

# 20. Analizador de patrones en textos
# Paso 1 - Entender el problema (EPS)
# Entrada: Texto y, opcionalmente, un patrón de búsqueda.
# Proceso: Separar el texto en palabras con split(); filtrar con startswith para el patrón; agrupar por len(palabra) en un diccionario; acumular todas las palabras vistas para poder sacar las únicas con un conjunto.
# Salida: Lista filtrada, diccionario agrupado, o conjunto de palabras únicas.
# Paso 2 - Bosquejo a mano
# texto = "el gato está aquí"
# split() -> ["el", "gato", "está", "aquí"]
# "el"   -> longitud 2 -> grupos={2:["el"]}
# "gato" -> longitud 4 -> grupos={2:["el"], 4:["gato"]}
# "está" -> longitud 4 -> ¡ojo! "está" tiene tilde, son 4 caracteres -> longitud 4
# "aquí" -> longitud 4 -> igual, 4 caracteres
# (ver nota más abajo sobre la longitud real de estas palabras)
# Paso 3 - Buscar el patron
# split() es el punto de partida común a los tres métodos: siempre convierte el texto en una lista de palabras antes de procesarlas. agrupar_por_longitud usa dict.setdefault(longitud, []).append(palabra) para no tener que comprobar "¿ya existe esta clave?" a mano. palabras_unicas no vuelve a hacer split() cada vez: reutiliza una lista acumulada (self.todas_las_palabras) que los otros métodos van llenando, y al final la convierte en set().
# Paso 4 - Codigo
class AnalizadorPatrones:
    def __init__(self):
        self.texto = []

    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        resultado = []
        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)
        return resultado

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        resultado = {}

        for palabra in palabras:
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado

    def palabras_unicas(self):
        palabras = self.texto.split()
        unicas = set(palabras)

        return unicas

analizador = AnalizadorPatrones()
resultado = analizador.encontrar_palabras(input("Dame una oracion: "), input("Dame el patron: "))
res = analizador.agrupar_por_longitud(input("Dame otra oracion: "))
print(resultado)
print(res)
# Paso 5 - Prueba de escritorio
# Palabra	len(palabra)	grupos
# el	2	{2: ['el']}
# gato	4	{2: ['el'], 4: ['gato']}
# está	4	{2: ['el'], 4: ['gato', 'está']}
# aquí	4	{2: ['el'], 4: ['gato', 'está', 'aquí']}

