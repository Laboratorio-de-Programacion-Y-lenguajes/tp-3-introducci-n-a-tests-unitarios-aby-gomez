"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)

def test_div_resultado_decimal():
    assert div(1,2) == 0.5

@pytest.mark.parametrize("a,b,expected", [
    (-12, 4, -3),                    
    (12, -4, -3),
    (-12, -4, 3),

])

def test_div_negativos_parametrizado(a, b, expected):
#                          ↑ recibe esos valores
    assert div(a, b) == expected


def test_div_por_cero():
     with pytest.raises(ZeroDivisionError):
         div(10, 0)
