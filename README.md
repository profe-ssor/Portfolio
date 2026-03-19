# My Personal Site

Django portfolio project.

## Security (before you push or deploy)

- **Never commit** `.env`, `portfolio/.env`, database files, or `__pycache__`.
- Copy **`.env.example`** → **`.env`** locally and fill in real values. Only **`.env.example`** belongs in git.
- **Secrets live in environment variables** on Render (or any host): `SECRET_KEY`, `DATABASE_URL`, `EMAIL_HOST_PASSWORD`, etc.
- If this repo was ever pushed with a **Gmail app password** or **production `SECRET_KEY`**, **revoke and regenerate** them in Google Account / your host dashboard — git history may still contain old values.

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
   # Edit .env — see comments inside .env.example
   ```

   - Leave **`DATABASE_URL`** empty for local **SQLite** (`db.sqlite3`).
   - For **production**, set `DATABASE_URL` to your Postgres URL on the host.

3. **Run**

   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput   # production
   python manage.py runserver
   ```

## Production (e.g. Render) — set these in the dashboard

| Variable | Example / notes |
|----------|------------------|
| `SECRET_KEY` | Long random string (see above) |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app.onrender.com,.onrender.com` |
| `DATABASE_URL` | Provided when you add Postgres |
| `EMAIL_HOST_USER` | Your Gmail address |
| `EMAIL_HOST_PASSWORD` | Gmail **App Password**, not your login password |
| `DEFAULT_FROM_EMAIL` | Same as `EMAIL_HOST_USER` usually |
| `CONTACT_RECIPIENT_EMAIL` | Inbox for contact form (optional) |

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
