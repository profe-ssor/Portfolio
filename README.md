# My Personal Site

Django portfolio project.

**Database:** SQLite only (no Postgres). The DB file is `db.sqlite3` next to `manage.py`.

## Security (before you push or deploy)

- **Never commit** `.env`, `portfolio/.env`, database files, or `__pycache__`.
- Copy **`.env.example`** → **`.env`** locally and fill in real values. Only **`.env.example`** belongs in git.
- **Secrets on Render:** `SECRET_KEY`, `EMAIL_HOST_PASSWORD`, etc. — **remove `DATABASE_URL`** from the Web Service if it was added for Postgres (this app ignores it but old docs may have set it).
- If credentials were ever committed, **rotate** them (Gmail App Passwords, etc.).

### Generate a new `SECRET_KEY` (production)

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Setup (Linux / macOS)

1. **Virtual environment**

   ```bash
   cd /path/to/Portfolio
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Environment variables**

   ```bash
   cp .env.example .env
   # Edit .env
   ```

3. **Run**

   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput   # production / Render build
   python manage.py runserver
   ```

Static files in production are served by **WhiteNoise** (`CompressedStaticFilesStorage`). The build must run **`collectstatic`** (already in `portfolio/build.sh`).

## Render (SQLite)

1. In your **Web Service** → **Environment**, **delete** `DATABASE_URL` if it exists (leftover Postgres).
2. Set `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS` (e.g. `your-app.onrender.com,.onrender.com`).
3. Optional: email variables for the contact form.

**Note:** On Render, the filesystem is often **ephemeral** — `db.sqlite3` may be **reset on each deploy** unless you add a [persistent disk](https://render.com/docs/disks) and point the DB file there (advanced). For a mostly static portfolio this is usually fine.

| Variable | Notes |
|----------|--------|
| `SECRET_KEY` | Required when `DEBUG=False` |
| `DEBUG` | `False` in production |
| `ALLOWED_HOSTS` | Your Render hostname(s) |
| `EMAIL_*` | Optional; for SMTP contact form |
| `CONTACT_RECIPIENT_EMAIL` | Optional |

## Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## Python version

`runtime.txt` targets Python 3.11; 3.12 also works with the pinned requirements.
