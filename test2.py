from conversion import conversion as conv

def test(a):
    c = conv(a)

    test_c = a / 60

    assert c == test_c


test(1233)
test(1200)
test(47368880)
