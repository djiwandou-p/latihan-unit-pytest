from src.bagi import bagi
import pytest

def test_bagi_angka_positif_benar():
    """Test that divide returns the correct result when given two numbers."""
    assert bagi(1, 2) == 0.5