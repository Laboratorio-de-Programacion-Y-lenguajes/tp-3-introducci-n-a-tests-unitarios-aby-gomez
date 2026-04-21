"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])

def test_mean_lista_unico_elemento():
    
    assert mean([6]) == 6.0

@pytest.mark.parametrize("values,expected", [
    ([-12, 4], -4.0),                    
    ([12, -4], 4.0),
    ([-12, -4], -8.0),

])

def test_mean_lista_numeros_negativos(values,expected):
    
    assert mean(values) == expected


def test_lista_con_decimales():
    
    assert mean([1.5,2.3]) == pytest.approx(1.9)

def test_lista_vacia():
    with pytest.raises(ValueError):
        mean([])