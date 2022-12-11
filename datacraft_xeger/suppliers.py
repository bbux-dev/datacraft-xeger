import rstr
import datacraft


class _XegerSupplier(datacraft.ValueSupplierInterface):
    def __init__(self, regex):
        self.regex = regex

    def next(self, iteration):
        return rstr.xeger(self.regex)


def xeger_supplier(regex: str) -> datacraft.ValueSupplierInterface:
    """Creates a supplier for the given regex

    Args:
        regex: valid regex string to use for generation

    Returns:
        the value supplier interface
    """
    return _XegerSupplier(regex)
