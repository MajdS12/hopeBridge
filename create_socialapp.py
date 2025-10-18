# create_socialapp.py
import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).with_name(".env"))
except Exception:
    pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

SITE_DOMAIN = os.getenv("SITE_DOMAIN", "127.0.0.1:8000")
SITE_NAME = os.getenv("SITE_NAME", "Local")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
    raise SystemExit("❌ GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET missing in .env")

site, _ = Site.objects.get_or_create(
    id=1, defaults={"domain": SITE_DOMAIN, "name": SITE_NAME}
)
site.domain = SITE_DOMAIN
site.name = SITE_NAME
site.save()

app, created = SocialApp.objects.get_or_create(
    provider="google",
    defaults={
        "name": "Google",
        "client_id": GOOGLE_CLIENT_ID,
        "secret": GOOGLE_CLIENT_SECRET,
    },
)
app.client_id = GOOGLE_CLIENT_ID
app.secret = GOOGLE_CLIENT_SECRET
app.save()
app.sites.add(site)
app.save()

print("✅ Google SocialApp configured successfully.")
print(f"Domain: {SITE_DOMAIN} | Client ID: {GOOGLE_CLIENT_ID[:12]}...")
