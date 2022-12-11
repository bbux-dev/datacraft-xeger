import json
import logging

import datacraft
import datacraft._registered_types.common as common
from . import suppliers

_XEGER_KEY = 'xeger'

_log = logging.getLogger(__name__)


def load_custom():
    @datacraft.registry.schemas(_XEGER_KEY)
    def _get_xeger_schema():
        """ get the schema for xeger type """
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$id": "https://github.com/bbux-dev/datacraft-xeger/schemas/xeger.schema.json",
            "type": "object",
            "required": ["type", "data"],
            "properties": {
                "type": {"type": "string", "pattern": "^xeger$"},
                "data": {"type": "string"},
                "additionalProperties": False
            }
        }

    @datacraft.registry.types(_XEGER_KEY)
    def _configure_xeger_supplier(field_spec, _):
        """ configure the supplier for xeger types """
        if 'data' not in field_spec:
            raise datacraft.SpecException(
                'required data element not defined for ' + _XEGER_KEY + ' type : ' + json.dumps(field_spec))

        return suppliers.xeger_supplier(field_spec['data'])

    @datacraft.registry.usage(_XEGER_KEY)
    def _configure_xeger_usage():
        example = {
            "uk_phone:xeger": "\\+44 \\d{4} \\d{6}",
        }
        return common.standard_example_usage(example, 3)
