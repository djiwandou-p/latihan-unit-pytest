from src.naik import naik
def test_naik_salah():
    assert not naik(3) == 5

def test_naik_benar():
    assert naik(3) == 4