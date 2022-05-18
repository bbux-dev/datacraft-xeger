import pytest

import datacraft

import datacraft_xeger.suppliers as impl


def test_basic():
    supplier = impl.xeger_supplier(f'[0-9]abc[0-9]')

    val = supplier.next(0)

    assert len(val) == 5
    assert 'abc' in val


validation_test_specs = [
    {'foo:xeger': '\\d{4}'},
    {
        'foo': {
            'type': 'xeger',
            'data': '\\d{3,4}'
        }
    },
    {
        'foo': {
            'type': 'xeger',
            'data': '(A|B|C|D)'
        }
    }
]


@pytest.mark.parametrize("spec", validation_test_specs)
def test_spec_validation(spec):
    datacraft.entries(spec, 1, enforce_schema=True)


def test_missing_data_field():
    with pytest.raises(datacraft.SpecException):
        datacraft.entries({'foo:xeger': {}}, 1, enforce_schema=True)