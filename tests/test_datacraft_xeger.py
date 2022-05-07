import datacraft_xeger._impl as impl


def test_basic():
    supplier = impl.xeger_supplier(f'[0-9]abc[0-9]')

    val = supplier.next(0)

    assert len(val) == 5
    assert 'abc' in val
