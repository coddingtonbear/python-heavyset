import json
import os
from unittest import TestCase

from heavyset.parser import HeavySetBackup


class TestParser(TestCase):
    def test_parses_and_exports_successfuly(self):
        with open(
            os.path.join(
                os.path.dirname(__file__),
                "./2022-10-11.hsbackup"
            )
        ) as inf:
            json_data = inf.read()
            backup = HeavySetBackup.parse_raw(json_data)

            assert backup.dict(exclude_none=True) == json.loads(json_data)
