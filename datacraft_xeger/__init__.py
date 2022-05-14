import json
import logging


_XEGER_KEY = 'xeger'

_log = logging.getLogger(__name__)


def load_custom():
    import datacraft
    from . import suppliers

    @datacraft.registry.schemas(_XEGER_KEY)
    def _get_xeger_schema():
        """ get the schema for xeger type """
        return datacraft.schemas.load(_XEGER_KEY)

    @datacraft.registry.types(_XEGER_KEY)
    def _configure_xeger_supplier(field_spec, _):
        """ configure the supplier for xeger types """
        if 'data' not in field_spec:
            raise datacraft.SpecException(
                'required data element not defined for ' + _XEGER_KEY + ' type : ' + json.dumps(field_spec))

        return suppliers.xeger_supplier(field_spec['data'])
