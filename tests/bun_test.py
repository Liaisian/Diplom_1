class TestBun:

    @pytest.mark.parametrize('name, price', [
        ('Classic Bun', 2.5),
        ('PraktiCUM Bun', 3),
        (None, 0.0),
        ('Null price Bun', None),
        (None,None),
        (123,'1.2'),
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name


    @pytest.mark.parametrize('name, price', [
        ('Classic Bun', 2.5),
        ('PraktiCUM Bun', 3),
        (None, 0.0),
        ('Null price Bun', None),
        (None,None),
        (123,'1.2'),
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price