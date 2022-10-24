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

            reexported = backup.json(exclude_none=True)

            assert json.loads(reexported) == json.loads(json_data)
