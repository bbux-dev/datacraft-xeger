import rstr
import datacraft


class _XegerSupplier(datacraft.ValueSupplierInterface):
    def __init__(self, regex):
        self.regex = regex

    def next(self, iteration):
        return rstr.xeger(self.regex)


def xeger_supplier(regex: str) -> datacraft.ValueSupplierInterface:
    return _XegerSupplier(regex)
