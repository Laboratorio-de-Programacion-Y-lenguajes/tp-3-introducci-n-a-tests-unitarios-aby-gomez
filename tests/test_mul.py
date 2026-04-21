"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

def test_mul_por_cero():
    assert mul(5,0) == 0.0

def test_mul_negativos():
    assert mul(-5,-4) == 20.0

def test_mul_positivo_y_negativo():
    assert mul(-5,2) == -10.0

def test_mul_por_uno():
    assert mul(1,2) == 2.0

def test_mul_decimales():
    assert mul(1.5,2.1) == pytest.approx(3.15)