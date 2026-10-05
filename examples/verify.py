from pathlib import Path
import json
from decimal import Decimal

data = json.loads(Path(__file__).with_name('scenario.json').read_text(encoding='utf-8'))
assert data['synthetic'] is True
from datetime import date
assert date.fromisoformat(data['calendar_date']).isocalendar().week == data['expected_iso_week']
assert data['illustrative_only'] is True
assert data['record'].startswith('DEMO-')
print('Ejemplo sintético coherente; no ejecuta ni valida el sistema operativo.')
