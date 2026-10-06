import random

def leer_sensor(id_sensor: str) -> float:
    """Simula la lectura de un sensor de voltaje."""
    voltaje_base = 220.0
    ruido = random.uniform(-2.5, 2.5)
    return voltaje_base + ruido