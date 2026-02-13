Quick start — one-click runner

Windows (double-click): run_all.bat
PowerShell (right-click -> Run with PowerShell): run_all.ps1

What this does:
- creates a `venv` inside the lesson folder if missing
- installs packages from `requirements.txt`
- seeds the database (`seed_demo.py`) with a demo user (username: `demo`, password: `password123`) and sample items
- starts the Flask app (open http://127.0.0.1:5000)

If you already have Python and prefer a central venv, activate it and run `python run.py` from this folder.
