# Desafío 2 - Con control de lista

def preparar_pizza():
    """Función para preparar pizza"""
    return "🍕"

def preparar_hamburguesa():
    """Función para preparar hamburguesa"""
    return "🍔"

def preparar_hotdog():
    """Función para preparar hotdog"""
    return "🌭"

def calcular_bonus(numero_porciones):
    """
    Devuelve una lista con el bonus. Si numero_porciones > 2, retorna ["coca gratis"], sino lista vacía.
    Usamos lista para tener control total sobre el bonus.
    """
    return ["coca gratis"] if numero_porciones > 2 else []

def ordenar_alimento(funcion_preparar_alimento, numero_porciones):
    """
    Usa comprensión de listas para controlar la creación de porciones.
    Devuelve 2 listas: porciones_alimentos y bonus
    """
    # Control de lista: generamos las porciones con list comprehension
    porciones_alimentos = [funcion_preparar_alimento() for _ in range(numero_porciones)]
    
    # Control de lista: el bonus también es una lista
    bonus = calcular_bonus(numero_porciones)
    
    return porciones_alimentos, bonus

# Pruebas con control de lista para cada grupo
pedidos = [
    {"alimento": preparar_pizza, "cantidad": 4, "grupo": "Grupo 1 - Pizza"},
    {"alimento": preparar_hamburguesa, "cantidad": 2, "grupo": "Grupo 2 - Hamburguesa"},
    {"alimento": preparar_hotdog, "cantidad": 1, "grupo": "Grupo 3 - Hotdog"}
]

# Control de lista: procesamos todos los pedidos con comprensión de listas
resultados = [
    {
        "grupo": pedido["grupo"],
        "orden": ordenar_alimento(pedido["alimento"], pedido["cantidad"])[0],
        "bonus": ordenar_alimento(pedido["alimento"], pedido["cantidad"])[1]
    }
    for pedido in pedidos
]

# Control de lista: imprimimos usando iteración sobre la lista de resultados
for resultado in resultados:
    print(f"\n=== {resultado['grupo']} ===")
    print(f"Orden: {resultado['orden']}")
    print(f"Bonus: {resultado['bonus']}")