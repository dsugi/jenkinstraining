def kali(a,b):
    hasil=a*b
    return hasil

def bagi(a,b):
    hasil=a/b
    return hasil

def jumlah(a,b):
    hasil=a+b
    return hasil

def kurang(a,b):
    hasil=a-b
    return hasil

def test_kali():
    angka=10
    assert kali(angka,5) == 50

def test_bagi():
    assert bagi(10,5) == 2

def test_jumlah():
    assert jumlah(10,5) == 150

def test_kurang():
    assert kurang(10,5) == 5