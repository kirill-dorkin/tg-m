import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import Account
from scripts.functions import join_grp

if len(sys.argv) != 2:
    print("Usage: python scripts/subscribe_all.py <channel>")
    sys.exit(1)

channel = sys.argv[1]

for acc in Account.objects.all():
    success = join_grp(channel, acc.sess_str)
    status = "joined" if success else "failed"
    print(f"{acc.acc_name}: {status}")
