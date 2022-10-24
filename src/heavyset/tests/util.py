import json
import os

from heavyset.parser import HeavySetBackup


def write_comparable_jsons():
    with open(
        os.path.join(
            os.path.dirname(__file__),
            "./2022-10-11.hsbackup"
        )
    ) as inf:
        json_data = inf.read()
        backup = HeavySetBackup.parse_raw(json_data)

        as_json = backup.json(exclude_none=True, indent=4, sort_keys=True)
        original_formatted = json.dumps(json.loads(json_data), indent=4, sort_keys=True)

        with open('output.json', 'w') as outf:
            outf.write(as_json)

        with open('input.json', 'w') as outf:
            outf.write(original_formatted)
