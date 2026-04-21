"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
def test_sub_mayor_primero():
    assert sub(1, 2) == -1

def test_sub_dos_negativos():
    assert sub(-1, -2) == 1

def test_sub_con_cero():
    assert sub(-1, 0) == -1

def test_sub_dos_decimales():
    assert sub(-1.5, -3.2) == pytest.approx(1.7)

