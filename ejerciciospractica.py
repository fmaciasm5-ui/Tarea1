# 1. Validador de respuestas de encuesta (1 a 5)
# (Se parece al ejercicio 1: Validador de notas con promedio)
# Paso 1 - Entender el problema (EPS)
# Entrada: Respuestas sueltas o en lote; algunas fuera del rango 1 a 5.
# Proceso: Validar cada respuesta una por una; si es válida guardarla en la lista; al final sumar y dividir entre la cantidad.
# Salida: Lista de respuestas válidas y su promedio.
# Paso 2 - Bosquejo a mano
# Datos: 4, 5, 7, 0, 3, 5
# ¿4 es válida?  1 <= 4 <= 5 -> SÍ -> lista = [4]
# ¿5 es válida?  1 <= 5 <= 5 -> SÍ -> lista = [4, 5]
# ¿7 es válida?  1 <= 7 <= 5 -> NO -> se descarta
# ¿0 es válida?  1 <= 0 <= 5 -> NO -> se descarta
# ¿3 es válida?  1 <= 3 <= 5 -> SÍ -> lista = [4, 5, 3]
# ¿5 es válida?  1 <= 5 <= 5 -> SÍ -> lista = [4, 5, 3, 5]
# promedio = (4+5+3+5) / 4 = 17 / 4 = 4.25
# Paso 3 - Descubrir el patrón
# Lo que se repite: la prueba 1 <= valor <= 5 es siempre la misma, por eso vive en validar_respuesta.
# Lo que cambia: cuántas respuestas llegan de golpe; cargar_respuestas usa *args y llama a validar_respuesta una vez por cada valor, sin repetir el if.
# Extra: promedio() revisa si la lista está vacía para no dividir entre cero.
# Paso 4 - Código
class Encuesta:
    def __init__(self):
        self.respuestas = []

    def validar_respuesta(self, valor):
        return 1 <= valor <= 5          

    def cargar_respuestas(self, *args):
        for valor in args:             
            if self.validar_respuesta(valor):
                self.respuestas.append(valor)
        return self.respuestas

    def promedio(self):
        if len(self.respuestas) == 0:   
            return 0
        return sum(self.respuestas) / len(self.respuestas)

enc = Encuesta()
print(enc.cargar_respuestas(4, 5, 7, 0, 3, 5))
print(enc.promedio())
# Paso 5 - Prueba de escritorio
# Acción                          | self.respuestas | Salida
# enc = Encuesta()                | []              | —
# cargar_respuestas(4,5,7,0,3,5)  | [4, 5, 3, 5]    | [4, 5, 3, 5]
# promedio()                      | [4, 5, 3, 5]    | 4.25
# Para explicarlo: "Separé la regla de validar de la acción de cargar, así si la regla cambia (por ejemplo a 1-10) solo cambio una línea."


# 2. Control de visitantes únicos
# (Se parece al ejercicio 2: Contador de palabras únicas)
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombres de usuario que visitan una página; algunos vuelven a entrar.
# Proceso: Cada visita se agrega a un conjunto (sin repetidos) y a una lista (conserva todas las visitas en orden).
# Salida: Cantidad de visitantes únicos y total de visitas.
# Paso 2 - Bosquejo a mano
# Datos: "ana", "luis", "ana"
# registrar_visita("ana")  -> conjunto = {"ana"}          lista = ["ana"]
# registrar_visita("luis") -> conjunto = {"ana","luis"}   lista = ["ana","luis"]
# registrar_visita("ana")  -> conjunto igual (ya estaba)  lista = ["ana","luis","ana"]
# contar_unicos() = len(conjunto) = 2      total_visitas() = len(lista) = 3
# Paso 3 - Descubrir el patrón
# Lo que se repite: guardar una visita siempre es lo mismo (add + append), por eso registrar_multiples solo hace un bucle que llama a registrar_visita.
# Lo que cambia: cuántos usuarios llegan a la vez. El set resuelve "¿quiénes son distintos?" y la lista resuelve "¿cuántas veces entraron en total?".
# Paso 4 - Código
class RegistroVisitantes:
    def __init__(self):
        self.unicos = set()
        self.orden = []

    def registrar_visita(self, usuario):
        self.unicos.add(usuario)        
        self.orden.append(usuario)      

    def registrar_multiples(self, *usuarios):
        for usuario in usuarios:
            self.registrar_visita(usuario)

    def contar_unicos(self):
        return len(self.unicos)

    def total_visitas(self):
        return len(self.orden)

rv = RegistroVisitantes()
rv.registrar_multiples("ana", "luis", "ana", "marta", "luis", "ana")
print(f"Visitantes únicos: {rv.contar_unicos()}")
print(f"Total de visitas: {rv.total_visitas()}")
print(f"Orden de llegada: {rv.orden}")
# Paso 5 - Prueba de escritorio
# Usuario | self.unicos              | self.orden
# ana     | {ana}                    | [ana]
# luis    | {ana, luis}              | [ana, luis]
# ana     | {ana, luis}              | [ana, luis, ana]
# marta   | {ana, luis, marta}       | [ana, luis, ana, marta]
# luis    | {ana, luis, marta}       | [ana, luis, ana, marta, luis]
# ana     | {ana, luis, marta}       | [ana, luis, ana, marta, luis, ana]
# contar_unicos() -> 3      total_visitas() -> 6
# Para explicarlo: "Uso dos colecciones sobre el mismo dato porque cada una responde una pregunta distinta."


# 3. Cuenta de restaurante
# (Se parece al ejercicio 3: Gestor de compras con totales)
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre y precio de cada plato pedido.
# Proceso: Guardar cada par plato->precio en un diccionario; sumar los valores para el total; filtrar por rango de precio recorriendo items().
# Salida: Total de la cuenta y lista de platos dentro de un rango de precio.
# Paso 2 - Bosquejo a mano
# agregar_plato("sopa", 3.50)   -> dict = {"sopa": 3.50}
# agregar_plato("arroz", 5.00)  -> dict = {"sopa": 3.50, "arroz": 5.00}
# agregar_plato("jugo", 1.50)   -> dict = {..., "jugo": 1.50}
# agregar_plato("postre", 2.75) -> dict = {..., "postre": 2.75}
# total_cuenta() = 3.50 + 5.00 + 1.50 + 2.75 = 12.75
# platos_por_rango(2.00, 4.00):
#   "sopa"   -> 3.50 en [2.00, 4.00] -> SÍ
#   "arroz"  -> 5.00 en [2.00, 4.00] -> NO
#   "jugo"   -> 1.50 en [2.00, 4.00] -> NO
#   "postre" -> 2.75 en [2.00, 4.00] -> SÍ
#   -> ["sopa", "postre"]
# Paso 3 - Descubrir el patrón
# El diccionario es el almacén natural porque cada plato (clave única) tiene un precio (valor).
# total_cuenta y platos_por_rango no repiten la lógica de guardado: solo leen self.pedido de dos formas distintas (sumar vs. filtrar).
# Paso 4 - Código
class CuentaRestaurante:
    def __init__(self):
        self.pedido = {}

    def agregar_plato(self, nombre, precio):
        self.pedido[nombre] = precio

    def total_cuenta(self):
        return sum(self.pedido.values())

    def platos_por_rango(self, precio_min, precio_max):
        resultado = []
        for nombre, precio in self.pedido.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado

cr = CuentaRestaurante()
cr.agregar_plato("sopa", 3.50)
cr.agregar_plato("arroz", 5.00)
cr.agregar_plato("jugo", 1.50)
cr.agregar_plato("postre", 2.75)
print(f"Total: {cr.total_cuenta()}")
print(f"Entre 2.00 y 4.00: {cr.platos_por_rango(2.00, 4.00)}")
# Paso 5 - Prueba de escritorio
# Acción                       | self.pedido                                             | Salida
# cr = CuentaRestaurante()     | {}                                                      | —
# agregar_plato("sopa",3.50)   | {"sopa": 3.5}                                           | —
# agregar_plato("arroz",5.00)  | {"sopa": 3.5, "arroz": 5.0}                             | —
# agregar_plato("jugo",1.50)   | {"sopa": 3.5, "arroz": 5.0, "jugo": 1.5}                | —
# agregar_plato("postre",2.75) | {"sopa": 3.5, "arroz": 5.0, "jugo": 1.5, "postre": 2.75}| —
# total_cuenta()               | (igual)                                                 | 12.75
# platos_por_rango(2.00,4.00)  | (igual)                                                 | ["sopa", "postre"]


# 4. Inversor de palabras y detector de palíndromos
# (Se parece al ejercicio 4: Inversor de secuencias)
# Paso 1 - Entender el problema (EPS)
# Entrada: Una palabra, o varias palabras a la vez.
# Proceso: Recorrer la palabra de atrás hacia adelante con un índice manual, armando una palabra nueva; un palíndromo es la palabra que es igual a su inversa; para varias palabras, guardar cada resultado en un diccionario.
# Salida: Palabra invertida, True/False de palíndromo, o diccionario palabra->invertida.
# Paso 2 - Bosquejo a mano
# Datos: "casa" (largo = 4, índices 0,1,2,3)
# i = 3 -> palabra[3] = "a" -> invertida = "a"
# i = 2 -> palabra[2] = "s" -> invertida = "as"
# i = 1 -> palabra[1] = "a" -> invertida = "asa"
# i = 0 -> palabra[0] = "c" -> invertida = "asac"
# Resultado: "asac"    "casa" == "asac"? NO -> no es palíndromo
# Paso 3 - Descubrir el patrón
# Lo que se repite: recorrer de atrás hacia adelante con range(len(palabra)-1, -1, -1).
# Lo que cambia: qué se hace con la inversa. es_palindromo no vuelve a escribir el bucle, llama a invertir_palabra y solo compara. invertir_multiples la llama una vez por palabra.
# Aquí las claves del diccionario pueden ser las palabras directamente (un string sí puede ser clave; una lista no, por eso en tu ejercicio 4 usaste tuple()).
# Paso 4 - Código
class InversorPalabras:
    def invertir_palabra(self, palabra):
        invertida = ""
        for i in range(len(palabra) - 1, -1, -1):
            invertida = invertida + palabra[i]
        return invertida

    def es_palindromo(self, palabra):
        return palabra == self.invertir_palabra(palabra)

    def invertir_multiples(self, *palabras):
        resultado = {}
        for palabra in palabras:
            resultado[palabra] = self.invertir_palabra(palabra)
        return resultado

ip = InversorPalabras()
print(ip.invertir_palabra("casa"))
print(ip.es_palindromo("reconocer"), ip.es_palindromo("casa"))
print(ip.invertir_multiples("sol", "ojo"))
# Paso 5 - Prueba de escritorio
# i | palabra[i] | invertida
# 3 | a          | "a"
# 2 | s          | "as"
# 1 | a          | "asa"
# 0 | c          | "asac"
# es_palindromo("casa") -> "casa" == "asac" -> False


# 5. Clasificador de signos
# (Se parece al ejercicio 5: Detector de pares e impares)
# Paso 1 - Entender el problema (EPS)
# Entrada: Varios números en un solo lote.
# Proceso: Para cada número preguntar si es mayor, menor o igual a 0; según la respuesta, agregarlo a la lista correspondiente del diccionario.
# Salida: Diccionario clasificado y tupla con las tres cantidades.
# Paso 2 - Bosquejo a mano
# Datos: 5, -3, 0, 8, -1
# 5  > 0 -> positivo -> positivos=[5]
# -3 < 0 -> negativo -> negativos=[-3]
# 0      -> cero     -> ceros=[0]
# 8  > 0 -> positivo -> positivos=[5,8]
# -1 < 0 -> negativo -> negativos=[-3,-1]
# Resultado: {'positivos':[5,8], 'negativos':[-3,-1], 'ceros':[0]}
# cantidades() = (2, 2, 1)
# Paso 3 - Descubrir el patrón
# tipo_numero encapsula la única decisión que se repite; clasificar no repite los if, usa lo que devuelve tipo_numero como CLAVE del diccionario (resultado[tipo].append(numero)).
# Guardar el último resultado en un atributo permite que cantidades() no reciba los números otra vez.
# Paso 4 - Código
class ClasificadorSignos:
    def __init__(self):
        self.ultimo_resultado = {'positivos': [], 'negativos': [], 'ceros': []}

    def tipo_numero(self, numero):
        if numero > 0:
            return 'positivos'
        elif numero < 0:
            return 'negativos'
        else:
            return 'ceros'

    def clasificar(self, *numeros):
        resultado = {'positivos': [], 'negativos': [], 'ceros': []}
        for numero in numeros:
            tipo = self.tipo_numero(numero)
            resultado[tipo].append(numero)
        self.ultimo_resultado = resultado
        return resultado

    def cantidades(self):
        return (len(self.ultimo_resultado['positivos']),
                len(self.ultimo_resultado['negativos']),
                len(self.ultimo_resultado['ceros']))

cs = ClasificadorSignos()
print(cs.clasificar(5, -3, 0, 8, -1))
print(cs.cantidades())
# Paso 5 - Prueba de escritorio
# Número | tipo_numero() | positivos | negativos | ceros
# 5      | positivos     | [5]       | []        | []
# -3     | negativos     | [5]       | [-3]      | []
# 0      | ceros         | [5]       | [-3]      | [0]
# 8      | positivos     | [5, 8]    | [-3]      | [0]
# -1     | negativos     | [5, 8]    | [-3, -1]  | [0]
# cantidades() -> (2, 2, 1)


# 6. Estadísticas de ventas diarias
# (Se parece al ejercicio 6: Estadísticas de temperatura)
# Paso 1 - Entender el problema (EPS)
# Entrada: Ventas sueltas o en lote.
# Proceso: Guardar cada venta en una lista; usar min, max, sum y len sobre esa lista.
# Salida: Venta mínima, máxima, total y promedio.
# Paso 2 - Bosquejo a mano
# Datos: 120, 80, 150, 90
# lista = [120, 80, 150, 90]
# mínima   = 80
# máxima   = 150
# total    = 120+80+150+90 = 440
# promedio = 440 / 4 = 110.0
# Paso 3 - Descubrir el patrón
# registrar_venta hace una sola cosa (agregar a la lista); registrar_multiples solo la llama en un bucle.
# Las cuatro estadísticas reutilizan la misma lista self.ventas, mirándola de forma distinta.
# Paso 4 - Código
class GestorVentas:
    def __init__(self):
        self.ventas = []

    def registrar_venta(self, monto):
        self.ventas.append(monto)

    def registrar_multiples(self, *montos):
        for monto in montos:
            self.registrar_venta(monto)

    def venta_minima(self):
        return min(self.ventas)

    def venta_maxima(self):
        return max(self.ventas)

    def total(self):
        return sum(self.ventas)

    def promedio(self):
        return sum(self.ventas) / len(self.ventas)

gv = GestorVentas()
gv.registrar_multiples(120, 80, 150, 90)
print(f"Mínima: {gv.venta_minima()}  Máxima: {gv.venta_maxima()}")
print(f"Total: {gv.total()}  Promedio: {gv.promedio()}")
# Paso 5 - Prueba de escritorio
# Acción                          | self.ventas         | Salida
# gv = GestorVentas()             | []                  | —
# registrar_multiples(120,80,150,90) | [120, 80, 150, 90] | —
# venta_minima()                  | [120, 80, 150, 90]  | 80
# venta_maxima()                  | [120, 80, 150, 90]  | 150
# total()                         | [120, 80, 150, 90]  | 440
# promedio()                      | [120, 80, 150, 90]  | 110.0


# 7. Registro de puntos de jugadores
# (Se parece al ejercicio 7: Mapeador de edades)
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre y puntos de cada jugador.
# Proceso: Guardar en un diccionario nombre->puntos; filtrar recorriendo items(); promediar con sum/len sobre los valores.
# Salida: Lista de jugadores destacados y promedio de puntos.
# Paso 2 - Bosquejo a mano
# agregar_jugador("Leo", 25)  -> dict = {"Leo": 25}
# agregar_jugador("Sofi", 15) -> dict = {"Leo": 25, "Sofi": 15}
# agregar_jugador("Dani", 20) -> dict = {"Leo": 25, "Sofi": 15, "Dani": 20}
# jugadores_destacados(20):
#   "Leo"  -> 25 >= 20 -> SÍ
#   "Sofi" -> 15 >= 20 -> NO
#   "Dani" -> 20 >= 20 -> SÍ  (el igual también cuenta por el >=)
#   -> ["Leo", "Dani"]
# puntos_promedio() = (25+15+20) / 3 = 60 / 3 = 20.0
# Paso 3 - Descubrir el patrón
# El diccionario asocia cada nombre (clave única) con sus puntos (valor). jugadores_destacados no necesita otra estructura: recorre items() con un if y arma una lista con los nombres (las claves) que cumplen.
# Paso 4 - Código
class RegistroPuntos:
    def __init__(self):
        self.puntos = {}

    def agregar_jugador(self, nombre, puntos):
        self.puntos[nombre] = puntos

    def jugadores_destacados(self, puntos_minimos):
        resultado = []
        for nombre, punto in self.puntos.items():
            if punto >= puntos_minimos:
                resultado.append(nombre)
        return resultado

    def puntos_promedio(self):
        return sum(self.puntos.values()) / len(self.puntos)

rp = RegistroPuntos()
rp.agregar_jugador("Leo", 25)
rp.agregar_jugador("Sofi", 15)
rp.agregar_jugador("Dani", 20)
print(rp.jugadores_destacados(20))
print(rp.puntos_promedio())
# Paso 5 - Prueba de escritorio
# Acción                     | self.puntos                                | Salida
# rp = RegistroPuntos()      | {}                                         | —
# agregar_jugador("Leo",25)  | {"Leo": 25}                                | —
# agregar_jugador("Sofi",15) | {"Leo": 25, "Sofi": 15}                    | —
# agregar_jugador("Dani",20) | {"Leo": 25, "Sofi": 15, "Dani": 20}        | —
# jugadores_destacados(20)   | (igual)                                    | ["Leo", "Dani"]
# puntos_promedio()          | (igual)                                    | 20.0


# 8. Biblioteca de autores y libros
# (Se parece al ejercicio 8: Asignador de equipos)
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombres de autores y títulos de libros.
# Proceso: Crear la entrada del autor con lista vacía; agregar libros a esa lista; comparar longitudes de todas las listas para encontrar la mayor.
# Salida: Nombre del autor con más libros.
# Paso 2 - Bosquejo a mano
# crear_autor("Borges")                -> dict = {"Borges": []}
# agregar_libro("Borges","Ficciones")  -> dict = {"Borges": ["Ficciones"]}
# agregar_libro("Borges","El Aleph")   -> dict = {"Borges": ["Ficciones","El Aleph"]}
# crear_autor("Cortazar")              -> dict = {..., "Cortazar": []}
# agregar_libro("Cortazar","Rayuela")  -> dict = {..., "Cortazar": ["Rayuela"]}
# autor_con_mas_libros(): compara len(2) vs len(1) -> "Borges"
# Paso 3 - Descubrir el patrón
# Es un diccionario de listas (estructura anidada): cada clave apunta a su propia colección. agregar_libro no crea listas, reutiliza la que crear_autor dejó lista.
# En autor_con_mas_libros se usa ">" y no ">=": si hay empate se queda el primero que apareció.
# Paso 4 - Código
class Biblioteca:
    def __init__(self):
        self.autores = {}

    def crear_autor(self, nombre):
        self.autores[nombre] = []

    def agregar_libro(self, autor, libro):
        self.autores[autor].append(libro)

    def autor_con_mas_libros(self):
        mayor = ""
        cantidad_mayor = 0
        for autor, libros in self.autores.items():
            if len(libros) > cantidad_mayor:
                cantidad_mayor = len(libros)
                mayor = autor
        return mayor

bib = Biblioteca()
bib.crear_autor("Borges")
bib.agregar_libro("Borges", "Ficciones")
bib.agregar_libro("Borges", "El Aleph")
bib.crear_autor("Cortazar")
bib.agregar_libro("Cortazar", "Rayuela")
print(bib.autores)
print(bib.autor_con_mas_libros())
# Paso 5 - Prueba de escritorio
# Acción                              | self.autores
# bib = Biblioteca()                  | {}
# crear_autor("Borges")               | {"Borges": []}
# agregar_libro("Borges","Ficciones") | {"Borges": ["Ficciones"]}
# agregar_libro("Borges","El Aleph")  | {"Borges": ["Ficciones","El Aleph"]}
# crear_autor("Cortazar")             | {"Borges": [...2], "Cortazar": []}
# agregar_libro("Cortazar","Rayuela") | {"Borges": [...2], "Cortazar": ["Rayuela"]}
# autor_con_mas_libros()              | Borges (2) vs Cortazar (1) -> "Borges"


# 9. Analizador de contraseñas
# (Se parece al ejercicio 9: Validador de caracteres)
# Paso 1 - Entender el problema (EPS)
# Entrada: Una contraseña (texto).
# Proceso: Recorrer carácter por carácter; clasificar cada uno como mayúscula, minúscula, dígito o especial (reutilizando es_especial); de paso, guardar la contraseña más larga analizada.
# Salida: Diccionario con los cuatro conteos y True/False de si es segura.
# Paso 2 - Bosquejo a mano
# Texto: "Hola#2026"
# H -> mayúscula -> mayusculas=1
# o -> minúscula -> minusculas=1
# l -> minúscula -> minusculas=2
# a -> minúscula -> minusculas=3
# # -> especial   -> especiales=1
# 2 -> dígito     -> digitos=1
# 0 -> dígito     -> digitos=2
# 2 -> dígito     -> digitos=3
# 6 -> dígito     -> digitos=4
# Resultado: {'mayusculas':1, 'minusculas':3, 'digitos':4, 'especiales':1}
# Paso 3 - Descubrir el patrón
# es_especial encapsula la pregunta "no es letra ni número"; contar_tipos no vuelve a escribirla, solo la llama dentro del elif. es_segura no repite el bucle: llama a contar_tipos y solo compara los conteos.
# Guardar la clave más larga es un efecto secundario que se actualiza en cada análisis.
# Paso 4 - Código
class AnalizadorClave:
    def __init__(self):
        self.clave_mas_larga = ""

    def es_especial(self, caracter):
        return not caracter.isalnum()   # ni letra ni número

    def contar_tipos(self, clave):
        mayusculas = 0
        minusculas = 0
        digitos = 0
        especiales = 0
        if len(clave) > len(self.clave_mas_larga):
            self.clave_mas_larga = clave

        for caracter in clave:
            if caracter.isupper():
                mayusculas = mayusculas + 1
            elif caracter.islower():
                minusculas = minusculas + 1
            elif caracter.isdigit():
                digitos = digitos + 1
            elif self.es_especial(caracter):
                especiales = especiales + 1

        return {'mayusculas': mayusculas, 'minusculas': minusculas,
                'digitos': digitos, 'especiales': especiales}

    def es_segura(self, clave):
        conteo = self.contar_tipos(clave)
        return (len(clave) >= 8 and conteo['mayusculas'] > 0
                and conteo['digitos'] > 0 and conteo['especiales'] > 0)

ac = AnalizadorClave()
print(ac.contar_tipos("Hola#2026"))
print(ac.es_segura("Hola#2026"), ac.es_segura("hola"))
print(f"Clave más larga analizada: {ac.clave_mas_larga}")
# Paso 5 - Prueba de escritorio
# Carácter | Tipo       | mayusculas | minusculas | digitos | especiales
# H        | mayúscula  | 1          | 0          | 0       | 0
# o        | minúscula  | 1          | 1          | 0       | 0
# l        | minúscula  | 1          | 2          | 0       | 0
# a        | minúscula  | 1          | 3          | 0       | 0
# #        | especial   | 1          | 3          | 0       | 1
# 2        | dígito     | 1          | 3          | 1       | 1
# 0        | dígito     | 1          | 3          | 2       | 1
# 2        | dígito     | 1          | 3          | 3       | 1
# 6        | dígito     | 1          | 3          | 4       | 1
# es_segura("Hola#2026") -> largo 9 >= 8 y tiene mayúscula, dígito y especial -> True


# 10. Registro de pedidos con estado
# (Se parece al ejercicio 10: Gestor de tareas con prioridad)
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre del cliente y estado de su pedido.
# Proceso: Guardar cada pedido como tupla (cliente, estado) dentro de una lista; filtrar por el segundo elemento para los pendientes; eliminar un pedido buscándolo por el primer elemento.
# Salida: Lista de pedidos pendientes y True/False al eliminar.
# Paso 2 - Bosquejo a mano
# agregar_pedido("Ana","pendiente")    -> lista = [("Ana","pendiente")]
# agregar_pedido("Luis","entregado")   -> lista = [("Ana","pendiente"), ("Luis","entregado")]
# agregar_pedido("Marta","pendiente")  -> lista = [..., ("Marta","pendiente")]
# pedidos_pendientes():
#   ("Ana","pendiente")   -> estado == "pendiente" -> SÍ
#   ("Luis","entregado")  -> NO
#   ("Marta","pendiente") -> SÍ
#   -> [("Ana","pendiente"), ("Marta","pendiente")]
# eliminar_pedido("Luis") -> lo encuentra en la posición 1, lo quita, retorna True
# Paso 3 - Descubrir el patrón
# Cada pedido es una tupla porque cliente y estado viajan siempre juntos: tupla[0] es el cliente y tupla[1] el estado.
# pedidos_pendientes y eliminar_pedido no repiten la forma de guardar, solo recorren la misma lista con distinto criterio.
# En eliminar_pedido se hace return justo después de remove: así nunca seguimos recorriendo una lista que acabamos de modificar.
# Paso 4 - Código
class RegistroPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, cliente, estado):
        self.pedidos.append((cliente, estado))

    def pedidos_pendientes(self):
        resultado = []
        for pedido in self.pedidos:
            if pedido[1] == "pendiente":
                resultado.append(pedido)
        return resultado

    def eliminar_pedido(self, cliente):
        for pedido in self.pedidos:
            if pedido[0] == cliente:
                self.pedidos.remove(pedido)
                return True
        return False

rped = RegistroPedidos()
rped.agregar_pedido("Ana", "pendiente")
rped.agregar_pedido("Luis", "entregado")
rped.agregar_pedido("Marta", "pendiente")
print(rped.pedidos_pendientes())
print(rped.eliminar_pedido("Luis"))
print(rped.pedidos)
# Paso 5 - Prueba de escritorio
# Acción                            | self.pedidos                                              | Salida
# rped = RegistroPedidos()          | []                                                        | —
# agregar_pedido("Ana","pendiente") | [("Ana","pendiente")]                                     | —
# agregar_pedido("Luis","entregado")| [("Ana","pendiente"),("Luis","entregado")]                | —
# agregar_pedido("Marta","pendiente")| [("Ana",..),("Luis",..),("Marta","pendiente")]           | —
# pedidos_pendientes()              | (igual)                                                   | [("Ana","pendiente"),("Marta","pendiente")]
# eliminar_pedido("Luis")           | [("Ana","pendiente"),("Marta","pendiente")]               | True


# 11. Contador de votos
# (Se parece al ejercicio 11: Contador de frecuencia)
# Paso 1 - Entender el problema (EPS)
# Entrada: Votos sueltos o en lote (un candidato puede repetirse).
# Proceso: Por cada voto, aumentar en 1 el contador de ese candidato en el diccionario (o crearlo con 0+1 si es su primer voto); comparar los contadores para hallar el máximo.
# Salida: Candidato ganador y votos de un candidato específico.
# Paso 2 - Bosquejo a mano
# votar("Ana")   -> dict = {"Ana": 1}
# votar("Luis")  -> dict = {"Ana": 1, "Luis": 1}
# votar("Ana")   -> dict = {"Ana": 2, "Luis": 1}
# votar("Marta") -> dict = {"Ana": 2, "Luis": 1, "Marta": 1}
# votar("Ana")   -> dict = {"Ana": 3, "Luis": 1, "Marta": 1}
# ganador() -> compara 3 vs 1 vs 1 -> "Ana"
# votos_de("Luis") -> 1        votos_de("Pedro") -> 0 (nunca votaron por él)
# Paso 3 - Descubrir el patrón
# El diccionario es un "contador": la clave es el candidato y el valor cuántas veces apareció.
# self.votos.get(candidato, 0) + 1 evita el if "¿ya existe la clave?": si no existe, get devuelve 0 y el primer voto queda en 1.
# Paso 4 - Código
class UrnaVotos:
    def __init__(self):
        self.votos = {}

    def votar(self, candidato):
        self.votos[candidato] = self.votos.get(candidato, 0) + 1

    def votar_multiples(self, *candidatos):
        for candidato in candidatos:
            self.votar(candidato)

    def ganador(self):
        mayor = None
        cantidad_mayor = 0
        for candidato, cantidad in self.votos.items():
            if cantidad > cantidad_mayor:
                cantidad_mayor = cantidad
                mayor = candidato
        return mayor

    def votos_de(self, candidato):
        return self.votos.get(candidato, 0)

urna = UrnaVotos()
urna.votar_multiples("Ana", "Luis", "Ana", "Marta", "Ana", "Luis")
print(urna.votos)
print(urna.ganador())
print(urna.votos_de("Luis"), urna.votos_de("Pedro"))
# Paso 5 - Prueba de escritorio
# Voto  | self.votos
# Ana   | {"Ana": 1}
# Luis  | {"Ana": 1, "Luis": 1}
# Ana   | {"Ana": 2, "Luis": 1}
# Marta | {"Ana": 2, "Luis": 1, "Marta": 1}
# Ana   | {"Ana": 3, "Luis": 1, "Marta": 1}
# Luis  | {"Ana": 3, "Luis": 2, "Marta": 1}
# ganador() -> "Ana"      votos_de("Luis") -> 2      votos_de("Pedro") -> 0


# 12. Selector de páginas a imprimir
# (Se parece al ejercicio 12: Selector de rango con tuplas)
# Paso 1 - Entender el problema (EPS)
# Entrada: Uno o varios rangos de páginas (inicio, fin), que pueden solaparse.
# Proceso: Convertir cada rango en una tupla de números; juntar todo en un conjunto para que una página no se imprima dos veces; ordenar para presentar como lista.
# Salida: Lista de páginas únicas y cuántas son.
# Paso 2 - Bosquejo a mano
# crear_rango(1,5)  -> (1, 2, 3, 4, 5)
# crear_rango(4,8)  -> (4, 5, 6, 7, 8)
# crear_rango(10,12)-> (10, 11, 12)
# conjunto = {}
# update((1..5))   -> {1,2,3,4,5}
# update((4..8))   -> {1,2,3,4,5,6,7,8}       (4 y 5 no se duplican)
# update((10..12)) -> {1,2,3,4,5,6,7,8,10,11,12}
# sorted(conjunto) = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
# total_paginas = len(lista) = 11
# Paso 3 - Descubrir el patrón
# crear_rango resuelve un solo rango (range(inicio, fin + 1) porque el fin también se imprime).
# paginas_a_imprimir no repite esa fórmula: la llama una vez por cada tupla recibida vía *rangos y el set evita duplicados. total_paginas reutiliza paginas_a_imprimir y solo cuenta.
# Paso 4 - Código
class SelectorPaginas:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def paginas_a_imprimir(self, *rangos):
        combinadas = set()
        for inicio, fin in rangos:      # desempaqueta cada tupla (inicio, fin)
            combinadas.update(self.crear_rango(inicio, fin))
        return sorted(combinadas)

    def total_paginas(self, *rangos):
        return len(self.paginas_a_imprimir(*rangos))

sp = SelectorPaginas()
print(sp.crear_rango(1, 5))
print(sp.paginas_a_imprimir((1, 5), (4, 8), (10, 12)))
print(sp.total_paginas((1, 5), (4, 8), (10, 12)))
# Paso 5 - Prueba de escritorio
# Acción                        | combinadas (set)                 | Salida
# combinadas = set()            | set()                            | —
# update(crear_rango(1,5))      | {1, 2, 3, 4, 5}                  | —
# update(crear_rango(4,8))      | {1, 2, 3, 4, 5, 6, 7, 8}         | —
# update(crear_rango(10,12))    | {1, 2, ..., 8, 10, 11, 12}       | —
# sorted(combinadas)            | (igual)                          | [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
# total_paginas(...)            | (igual)                          | 11


# 13. Sumador de listas posición a posición
# (Se parece al ejercicio 13: Combinador de listas)
# Paso 1 - Entender el problema (EPS)
# Entrada: Dos o más listas de números, posiblemente de distinto largo.
# Proceso: Recorrer con un índice común; en cada posición sumar el valor de lista1 con el de lista2 (si una lista ya se acabó, aporta 0); para más de dos listas, ir sumando el resultado acumulado con la siguiente.
# Salida: Una lista con las sumas.
# Paso 2 - Bosquejo a mano
# lista1 = [1, 2, 3]   lista2 = [10, 20]   -> largo = max(3, 2) = 3
# i=0: 1 + 10 = 11 -> resultado=[11]
# i=1: 2 + 20 = 22 -> resultado=[11, 22]
# i=2: 3 + 0  = 3  -> resultado=[11, 22, 3]   (lista2 ya no tiene posición 2, cuenta como 0)
# Resultado: [11, 22, 3]
# Paso 3 - Descubrir el patrón
# sumar resuelve el caso de dos listas con un solo bucle por índice, cuidando el largo distinto con if i < len(lista).
# sumar_multiples no reinventa la lógica: acumula el resultado parcial y lo vuelve a sumar con la siguiente lista, reutilizando sumar una y otra vez.
# Paso 4 - Código
class SumadorListas:
    def sumar(self, lista1, lista2):
        resultado = []
        largo = max(len(lista1), len(lista2))
        for i in range(largo):
            valor1 = 0
            valor2 = 0
            if i < len(lista1):
                valor1 = lista1[i]
            if i < len(lista2):
                valor2 = lista2[i]
            resultado.append(valor1 + valor2)
        return resultado

    def sumar_multiples(self, *listas):
        resultado = list(listas[0])
        for siguiente in listas[1:]:
            resultado = self.sumar(resultado, siguiente)
        return resultado

sl = SumadorListas()
print(sl.sumar([1, 2, 3], [10, 20]))
print(sl.sumar_multiples([1, 2], [3, 4], [5, 6]))
# Paso 5 - Prueba de escritorio
# i | valor1 (lista1[i]) | valor2 (lista2[i]) | resultado
# 0 | 1                  | 10                 | [11]
# 1 | 2                  | 20                 | [11, 22]
# 2 | 3                  | 0 (no existe)      | [11, 22, 3]
# sumar_multiples([1,2],[3,4],[5,6]):
#   resultado = [1, 2]
#   sumar([1,2],[3,4]) -> [4, 6]
#   sumar([4,6],[5,6]) -> [9, 12]


# 14. Registro de ciudades y temperaturas
# (Se parece al ejercicio 14: Mapeo de estudiantes a notas)
# Paso 1 - Entender el problema (EPS)
# Entrada: Nombre de ciudad y su temperatura.
# Proceso: Guardar en un diccionario ciudad->temperatura; filtrar recorriendo items() las ciudades calurosas; recorrer también para quedarse con la más fría actualizando un récord.
# Salida: Lista de ciudades calurosas y tupla (ciudad, temperatura) de la más fría.
# Paso 2 - Bosquejo a mano
# registrar("Lima", 22)     -> dict = {"Lima": 22}
# registrar("Bogotá", 14)   -> dict = {"Lima": 22, "Bogotá": 14}
# registrar("Panamá", 31)   -> dict = {..., "Panamá": 31}
# registrar("Santiago", 18) -> dict = {..., "Santiago": 18}
# ciudades_calurosas(20): Lima 22>=20 SÍ, Bogotá 14 NO, Panamá 31 SÍ, Santiago 18 NO -> ["Lima", "Panamá"]
# ciudad_mas_fria(): 22 -> 14 (menor) -> 31 no -> 18 no -> ("Bogotá", 14)
# Paso 3 - Descubrir el patrón
# Lo que se repite: recorrer con for ciudad, temp in self.temperaturas.items().
# Lo que cambia: qué se hace en cada vuelta. ciudades_calurosas acumula todas las que cumplen; ciudad_mas_fria solo se queda con la mejor actualizando un récord.
# Se empieza el récord en None (y no en 0) porque una temperatura puede ser negativa; con 0 una ciudad a -5 nunca sería "menor" que el valor inicial correcto.
# Paso 4 - Código
class RegistroClima:
    def __init__(self):
        self.temperaturas = {}

    def registrar(self, ciudad, temperatura):
        self.temperaturas[ciudad] = temperatura

    def ciudades_calurosas(self, temp_minima):
        calurosas = []
        for ciudad, temp in self.temperaturas.items():
            if temp >= temp_minima:
                calurosas.append(ciudad)
        return calurosas

    def ciudad_mas_fria(self):
        fria = None
        temp_menor = None
        for ciudad, temp in self.temperaturas.items():
            if temp_menor is None or temp < temp_menor:
                temp_menor = temp
                fria = ciudad
        return (fria, temp_menor)

rc = RegistroClima()
rc.registrar("Lima", 22)
rc.registrar("Bogotá", 14)
rc.registrar("Panamá", 31)
rc.registrar("Santiago", 18)
print(rc.temperaturas)
print(rc.ciudades_calurosas(20))
print(rc.ciudad_mas_fria())
# Paso 5 - Prueba de escritorio
# Ciudad   | temp | ¿temp_menor es None o temp < temp_menor? | fria     | temp_menor
# Lima     | 22   | SÍ (es None)                             | Lima     | 22
# Bogotá   | 14   | SÍ (14 < 22)                             | Bogotá   | 14
# Panamá   | 31   | NO (31 < 14 es falso)                    | Bogotá   | 14
# Santiago | 18   | NO (18 < 14 es falso)                    | Bogotá   | 14
# ciudad_mas_fria() -> ("Bogotá", 14)


# 15. Divisores y números primos
# (Se parece al ejercicio 15: Divisores de un número)
# Paso 1 - Entender el problema (EPS)
# Entrada: Un número, o un rango de números.
# Proceso: Probar cada número desde 1 hasta el número mismo y guardar los que dividen exacto (resto 0); un primo es el que tiene exactamente 2 divisores (1 y él mismo).
# Salida: Tupla de divisores, True/False de primo, o lista de primos en un rango.
# Paso 2 - Bosquejo a mano
# numero = 7
# i=1 -> 7%1=0 -> divisores=[1]
# i=2 -> 7%2=1 -> no
# i=3 -> 7%3=1 -> no
# i=4 -> 7%4=3 -> no
# i=5 -> 7%5=2 -> no
# i=6 -> 7%6=1 -> no
# i=7 -> 7%7=0 -> divisores=[1,7]
# Resultado: (1, 7) -> tiene 2 divisores -> es primo
# Para 9: (1, 3, 9) -> 3 divisores -> NO es primo
# Paso 3 - Descubrir el patrón
# encontrar_divisores es el método base que se reutiliza: es_primo lo llama y solo cambia qué hace con el resultado (contar y comparar con 2); primos_entre llama a es_primo una vez por cada número del rango.
# El 1 tiene un solo divisor (1), por eso es_primo(1) da False sin necesitar un caso especial.
# Paso 4 - Código
class AnalizadorDivisores:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)

    def es_primo(self, numero):
        return len(self.encontrar_divisores(numero)) == 2

    def primos_entre(self, inicio, fin):
        primos = []
        for numero in range(inicio, fin + 1):
            if self.es_primo(numero):
                primos.append(numero)
        return primos

ad = AnalizadorDivisores()
print(ad.encontrar_divisores(7))
print(ad.es_primo(7), ad.es_primo(9))
print(ad.primos_entre(1, 20))
# Paso 5 - Prueba de escritorio (para numero = 9)
# i | 9 % i | ¿Divide? | divisores
# 1 | 0     | SÍ       | [1]
# 2 | 1     | NO       | [1]
# 3 | 0     | SÍ       | [1, 3]
# 4 | 1     | NO       | [1, 3]
# 5 | 4     | NO       | [1, 3]
# 6 | 3     | NO       | [1, 3]
# 7 | 2     | NO       | [1, 3]
# 8 | 1     | NO       | [1, 3]
# 9 | 0     | SÍ       | [1, 3, 9]  -> 3 divisores -> es_primo(9) = False


# 16. Codificador César con dígitos
# (Se parece al ejercicio 16: Codificador/Decodificador)
# Paso 1 - Entender el problema (EPS)
# Entrada: Una frase y un desplazamiento.
# Proceso: Para cada carácter, convertirlo a su posición dentro de su grupo (letras: 0-25, dígitos: 0-9), sumarle el desplazamiento, usar % para que "dé la vuelta" y convertir de regreso con chr. Lo que no es letra ni dígito no se toca. Para decodificar se usa el mismo cálculo con desplazamiento negativo.
# Salida: Frase codificada o decodificada; el historial queda guardado en un diccionario.
# Paso 2 - Bosquejo a mano
# frase = "Hola 7", desplazamiento = 3
# H -> mayúscula, posición 7  -> (7+3)%26 = 10 -> 'K'
# o -> minúscula, posición 14 -> (14+3)%26 = 17 -> 'r'
# l -> minúscula, posición 11 -> (11+3)%26 = 14 -> 'o'
# a -> minúscula, posición 0  -> (0+3)%26 = 3   -> 'd'
# (espacio) -> no es letra ni dígito -> se queda igual
# 7 -> dígito, posición 7 -> (7+3)%10 = 0 -> '0'
# Resultado: "Krod 0"
# Vuelta al inicio: "xyz" con 3 -> x=23 -> 26%26=0 -> 'a'; y -> 'b'; z -> 'c'  => "abc"
# Paso 3 - Descubrir el patrón
# codificar_caracter resuelve la fórmula para UN carácter: solo cambian la base (ord('a'), ord('A') u ord('0')) y el módulo (26 o 10); la fórmula (ord(c) - base + desplazamiento) % modulo + base es siempre la misma.
# codificar_frase y decodificar_frase no repiten esa fórmula, solo recorren la frase llamando a codificar_caracter. Decodificar = codificar con -desplazamiento (en Python (0 - 3) % 26 da 23, o sea nunca sale negativo).
# Paso 4 - Código
class CodificadorMixto:
    def __init__(self):
        self.historial = {}

    def codificar_caracter(self, caracter, desplazamiento):
        if caracter in "abcdefghijklmnopqrstuvwxyz":
            base = ord('a')
            modulo = 26
        elif caracter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            base = ord('A')
            modulo = 26
        elif caracter in "0123456789":
            base = ord('0')
            modulo = 10
        else:
            return caracter
        return chr((ord(caracter) - base + desplazamiento) % modulo + base)

    def codificar_frase(self, frase, desplazamiento):
        resultado = ""
        for caracter in frase:
            resultado = resultado + self.codificar_caracter(caracter, desplazamiento)
        self.historial[frase] = resultado
        return resultado

    def decodificar_frase(self, frase, desplazamiento):
        resultado = ""
        for caracter in frase:
            resultado = resultado + self.codificar_caracter(caracter, -desplazamiento)
        return resultado

cm = CodificadorMixto()
print(cm.codificar_frase("Hola 7", 3))
print(cm.decodificar_frase("Krod 0", 3))
print(cm.codificar_frase("xyz", 3))
print(cm.historial)
# Paso 5 - Prueba de escritorio
# Carácter | base    | módulo | (ord - base + 3) % módulo | Resultado
# H        | 'A'(65) | 26     | (72-65+3)%26 = 10         | K
# o        | 'a'(97) | 26     | (111-97+3)%26 = 17        | r
# l        | 'a'(97) | 26     | (108-97+3)%26 = 14        | o
# a        | 'a'(97) | 26     | (97-97+3)%26 = 3          | d
# espacio  | —       | —      | no se modifica            | espacio
# 7        | '0'(48) | 10     | (55-48+3)%10 = 0          | 0


# 17. Agrupador de notas por letra
# (Se parece al ejercicio 17: Grupo de edades)
# Paso 1 - Entender el problema (EPS)
# Entrada: Notas sueltas o en lote (0 a 100).
# Proceso: Clasificar cada nota con una cadena de if/elif según rangos; agregarla a la lista de su letra dentro de un diccionario.
# Salida: Diccionario agrupado por letra, y promedio de una letra.
# Paso 2 - Bosquejo a mano
# Rangos usados: A 90-100, B 80-89, C 70-79, D 0-69
# nota=95 -> 95>=90 -> "A"
# nota=85 -> 85>=90 NO, 85>=80 SÍ -> "B"
# nota=72 -> >=90 NO, >=80 NO, >=70 SÍ -> "C"
# nota=60 -> ninguna anterior -> "D"
# nota=91 -> 91>=90 -> "A"
# Resultado: {'A':[95, 91], 'B':[85], 'C':[72], 'D':[60]}
# Paso 3 - Descubrir el patrón
# clasificar_nota concentra la única decisión que se repite (a qué letra pertenece una nota). El orden de los if importa: se pregunta de la nota más alta a la más baja para que cada if solo tenga que revisar un límite.
# agrupar_por_letra no repite esos if: llama a clasificar_nota y usa la letra como clave del diccionario. promedio_letra reutiliza agrupar_por_letra y devuelve 0 si ese grupo está vacío.
# Paso 4 - Código
class AgrupadorNotas:
    def clasificar_nota(self, nota):
        if nota >= 90:
            return "A"
        elif nota >= 80:
            return "B"
        elif nota >= 70:
            return "C"
        else:
            return "D"

    def agrupar_por_letra(self, *notas):
        grupos = {"A": [], "B": [], "C": [], "D": []}
        for nota in notas:
            letra = self.clasificar_nota(nota)
            grupos[letra].append(nota)
        return grupos

    def promedio_letra(self, letra, *notas):
        grupos = self.agrupar_por_letra(*notas)
        lista = grupos.get(letra, [])
        if len(lista) == 0:
            return 0
        return sum(lista) / len(lista)

an = AgrupadorNotas()
print(an.agrupar_por_letra(95, 85, 72, 60, 91))
print(an.promedio_letra("A", 95, 85, 72, 60, 91))
# Paso 5 - Prueba de escritorio
# Nota | clasificar_nota() | grupos
# 95   | A                 | {'A':[95], 'B':[], 'C':[], 'D':[]}
# 85   | B                 | {'A':[95], 'B':[85], 'C':[], 'D':[]}
# 72   | C                 | {'A':[95], 'B':[85], 'C':[72], 'D':[]}
# 60   | D                 | {'A':[95], 'B':[85], 'C':[72], 'D':[60]}
# 91   | A                 | {'A':[95, 91], 'B':[85], 'C':[72], 'D':[60]}
# promedio_letra("A") -> (95 + 91) / 2 = 93.0


# 18. Distancia Manhattan y rutas
# (Se parece al ejercicio 18: Matriz de distancias)
# Paso 1 - Entender el problema (EPS)
# Entrada: Puntos como tuplas (x, y).
# Proceso: Aplicar la fórmula Manhattan |x2-x1| + |y2-y1| (cuántas cuadras hay que caminar); guardar cada resultado en una lista; comparar distancias para hallar el punto más lejano; sumar distancias entre puntos consecutivos para una ruta.
# Salida: Distancia numérica, punto más lejano y longitud total de una ruta.
# Paso 2 - Bosquejo a mano
# p1=(0,0), p2=(3,4)
# dx = |3-0| = 3
# dy = |4-0| = 4
# distancia = 3 + 4 = 7
# Ruta (0,0) -> (2,3) -> (5,3):
#   tramo 1: |2-0| + |3-0| = 5
#   tramo 2: |5-2| + |3-3| = 3
#   total = 8
# Paso 3 - Descubrir el patrón
# distancia_manhattan resuelve el cálculo para UN par de puntos y guarda el resultado en el historial. punto_mas_lejano y distancia_ruta no repiten la fórmula: la llaman en un bucle.
# En distancia_ruta se recorre con índice i y se usa puntos[i] y puntos[i+1] (el punto actual y el siguiente); por eso el range llega solo hasta len(puntos) - 1.
# Paso 4 - Código
class CalculadorManhattan:
    def __init__(self):
        self.historial = []

    def distancia_manhattan(self, p1, p2):
        distancia = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        self.historial.append(distancia)
        return distancia

    def punto_mas_lejano(self, referencia, *puntos):
        lejano = None
        distancia_mayor = None
        for punto in puntos:
            distancia = self.distancia_manhattan(referencia, punto)
            if distancia_mayor is None or distancia > distancia_mayor:
                distancia_mayor = distancia
                lejano = punto
        return lejano

    def distancia_ruta(self, *puntos):
        total = 0
        for i in range(len(puntos) - 1):
            total = total + self.distancia_manhattan(puntos[i], puntos[i + 1])
        return total

cman = CalculadorManhattan()
print(cman.distancia_manhattan((0, 0), (3, 4)))
print(cman.punto_mas_lejano((0, 0), (1, 1), (5, 2), (-3, -3)))
print(cman.distancia_ruta((0, 0), (2, 3), (5, 3)))
print(cman.historial)
# Paso 5 - Prueba de escritorio
# Acción                                   | distancia | self.historial
# distancia_manhattan((0,0),(3,4))         | 7         | [7]
# punto_mas_lejano: comparar (1,1)         | 2         | [7, 2]
# punto_mas_lejano: comparar (5,2)         | 7         | [7, 2, 7]   (7 > 2, nuevo más lejano)
# punto_mas_lejano: comparar (-3,-3)       | 6         | [7, 2, 7, 6] (6 > 7 es falso) -> gana (5,2)
# distancia_ruta: tramo (0,0)->(2,3)       | 5         | [7, 2, 7, 6, 5]
# distancia_ruta: tramo (2,3)->(5,3)       | 3         | [7, 2, 7, 6, 5, 3]  -> total 8


# 19. Cuentas de ahorro
# (Se parece al ejercicio 19: Inventario de productos)
# Paso 1 - Entender el problema (EPS)
# Entrada: Cliente y monto a depositar o retirar.
# Proceso: Sumar o restar sobre el saldo guardado en el diccionario, validando que el monto sea positivo y que no se retire más de lo que hay; filtrar el diccionario buscando saldos bajo un mínimo.
# Salida: True/False según si la operación fue posible, y lista de clientes con saldo bajo.
# Paso 2 - Bosquejo a mano
# depositar("Ana", 100) -> dict = {"Ana": 100} -> True
# retirar("Ana", 40):
#   ¿100 >= 40? SÍ -> dict = {"Ana": 60} -> True
# retirar("Ana", 100):
#   ¿60 >= 100? NO -> no se modifica -> False
# clientes_saldo_bajo(80):
#   "Ana" -> 60 < 80 -> SÍ -> ["Ana"]
# Paso 3 - Descubrir el patrón
# retirar valida ANTES de modificar (if saldo >= monto) para no dejar saldos negativos: ese if es lo que cambia respecto a restar directamente.
# depositar usa get(cliente, 0) + monto, el mismo truco del contador: si el cliente es nuevo, parte de 0.
# clientes_saldo_bajo reutiliza el mismo diccionario con un filtro de items().
# Paso 4 - Código
class Banco:
    def __init__(self):
        self.cuentas = {}

    def depositar(self, cliente, monto):
        if monto <= 0:
            return False
        self.cuentas[cliente] = self.cuentas.get(cliente, 0) + monto
        return True

    def retirar(self, cliente, monto):
        if monto > 0 and self.cuentas.get(cliente, 0) >= monto:
            self.cuentas[cliente] -= monto
            return True
        return False

    def clientes_saldo_bajo(self, minimo):
        resultado = []
        for cliente, saldo in self.cuentas.items():
            if saldo < minimo:
                resultado.append(cliente)
        return resultado

banco = Banco()
print(banco.depositar("Ana", 100))
print(banco.retirar("Ana", 40))
print(banco.retirar("Ana", 100))
print(banco.cuentas)
print(banco.clientes_saldo_bajo(80))
# Paso 5 - Prueba de escritorio
# Acción                    | self.cuentas | Salida
# banco = Banco()           | {}           | —
# depositar("Ana",100)      | {"Ana": 100} | True
# retirar("Ana",40)         | {"Ana": 60}  | True
# retirar("Ana",100)        | {"Ana": 60}  | False (60 no es >= 100)
# clientes_saldo_bajo(50)   | {"Ana": 60}  | [] (60 no es < 50)
# clientes_saldo_bajo(80)   | {"Ana": 60}  | ["Ana"] (60 sí es < 80)


# 20. Analizador de correos electrónicos
# (Se parece al ejercicio 20: Analizador de patrones en textos)
# Paso 1 - Entender el problema (EPS)
# Entrada: Correos electrónicos (uno o varios) y, opcionalmente, un sufijo de búsqueda.
# Proceso: Guardar los correos en una lista del objeto; filtrar con endswith el sufijo; separar con split("@") para obtener el dominio y agrupar en un diccionario; convertir los dominios en un set para quedarse con los únicos.
# Salida: Lista filtrada, diccionario agrupado por dominio, o conjunto de dominios únicos.
# Paso 2 - Bosquejo a mano
# correos = ["ana@gmail.com", "luis@hotmail.com", "marta@gmail.com"]
# "ana@gmail.com".split("@")   -> ["ana", "gmail.com"]   -> dominio = posición 1 = "gmail.com"
# "ana@gmail.com"     -> dominio "gmail.com"  -> grupos = {"gmail.com": ["ana@gmail.com"]}
# "luis@hotmail.com"  -> dominio "hotmail.com"-> grupos = {"gmail.com": [ana], "hotmail.com": [luis]}
# "marta@gmail.com"   -> dominio "gmail.com"  -> grupos = {"gmail.com": [ana, marta], "hotmail.com": [luis]}
# terminan_en("@gmail.com") -> ["ana@gmail.com", "marta@gmail.com"]
# Paso 3 - Descubrir el patrón
# Los tres métodos parten de la misma lista self.correos, que llena agregar_correos: nadie vuelve a pedir los datos ni los guarda de nuevo, cada método solo los mira de una forma distinta (filtrar, agrupar, quitar repetidos).
# En agrupar_por_dominio se pregunta "if dominio not in resultado" para crear la lista vacía la primera vez y luego se hace append.
# Se busca el sufijo "@gmail.com" (con la arroba) y no "gmail.com" para no confundir con dominios como "fakegmail.com".
# Paso 4 - Código
class AnalizadorCorreos:
    def __init__(self):
        self.correos = []

    def agregar_correos(self, *correos):
        for correo in correos:
            self.correos.append(correo)

    def terminan_en(self, sufijo):
        resultado = []
        for correo in self.correos:
            if correo.endswith(sufijo):
                resultado.append(correo)
        return resultado

    def agrupar_por_dominio(self):
        resultado = {}
        for correo in self.correos:
            dominio = correo.split("@")[1]
            if dominio not in resultado:
                resultado[dominio] = []
            resultado[dominio].append(correo)
        return resultado

    def dominios_unicos(self):
        dominios = []
        for correo in self.correos:
            dominios.append(correo.split("@")[1])
        return set(dominios)

acorr = AnalizadorCorreos()
acorr.agregar_correos("ana@gmail.com", "luis@hotmail.com", "marta@gmail.com", "pedro@empresa.com")
print(acorr.terminan_en("@gmail.com"))
print(acorr.agrupar_por_dominio())
print(sorted(acorr.dominios_unicos()))
# Paso 5 - Prueba de escritorio
# Correo              | split("@")               | dominio       | grupos
# ana@gmail.com       | ["ana","gmail.com"]      | gmail.com     | {'gmail.com': ['ana@gmail.com']}
# luis@hotmail.com    | ["luis","hotmail.com"]   | hotmail.com   | {'gmail.com': [ana], 'hotmail.com': [luis]}
# marta@gmail.com     | ["marta","gmail.com"]    | gmail.com     | {'gmail.com': [ana, marta], 'hotmail.com': [luis]}
# pedro@empresa.com   | ["pedro","empresa.com"]  | empresa.com   | {'gmail.com': [ana, marta], 'hotmail.com': [luis], 'empresa.com': [pedro]}
# dominios_unicos()   -> {'gmail.com', 'hotmail.com', 'empresa.com'}  (sorted: empresa, gmail, hotmail)