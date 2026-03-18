# 🛒 Flask Market

A full-stack **online marketplace web application** built with Python and Flask. Users can register, log in, browse items, buy and sell products — all through a clean, responsive web interface backed by a relational database.

---

## 🚀 Features

- 🔐 **User Authentication** — Register, login, and logout with secure session management
- 🛍️ **Browse Items** — View all available market items with details and pricing
- 💰 **Buy & Sell** — Purchase items from other users or list your own for sale
- 🏦 **Budget System** — Each user has a wallet balance that updates on transactions
- 🗄️ **Database Backed** — Persistent storage using SQLite via SQLAlchemy ORM
- ⚡ **One-Click Setup** — Automated scripts to install, seed, and launch instantly

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML, Jinja2 Templates, CSS |
| Database | SQLite + SQLAlchemy ORM |
| Auth | Flask-Login, Flask-Bcrypt |
| Forms | Flask-WTF |

---

## 📁 Project Structure

```
Flask_Market/
├── market/
│   ├── __init__.py        # App factory and config
│   ├── models.py          # Database models (User, Item)
│   ├── routes.py          # All route handlers
│   ├── forms.py           # WTForms for login/register/market
│   └── templates/         # Jinja2 HTML templates
│       ├── base.html
│       ├── home.html
│       ├── market.html
│       ├── register.html
│       └── login.html
├── run.py                 # App entry point
├── create_db.py           # Initialize the database
├── seed_demo.py           # Seed demo user + sample items
├── seed_items.py          # Seed market items only
├── requirements.txt       # Python dependencies
├── run_all.bat            # One-click Windows launcher
├── run_all.ps1            # PowerShell launcher
└── README.md
```

---

## ⚡ Quick Start (Windows — One Click)

### Option 1 — Double Click
```
run_all.bat
```

### Option 2 — PowerShell
```powershell
Right-click run_all.ps1 → "Run with PowerShell"
```

Both scripts automatically:
1. Create a virtual environment
2. Install all dependencies from `requirements.txt`
3. Seed the database with a demo user and sample items
4. Launch the Flask app at `http://127.0.0.1:5000`

**Demo Credentials:**
```
Username : demo
Password : password123
```

---

## 🖥️ Manual Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Architcybercrime/Flask_Market.git
cd Flask_Market
```

### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Initialize the Database
```bash
python create_db.py
```

### 5. Seed Demo Data (Optional)
```bash
python seed_demo.py    # Adds demo user + items
# OR
python seed_items.py   # Adds items only
```

### 6. Run the Application
```bash
python run.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## 📸 Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Landing page |
| Market | `/market` | Browse & buy items |
| Register | `/register` | Create new account |
| Login | `/login` | User login |
| Logout | `/logout` | End session |

---

## 🔧 Requirements

- Python 3.8+
- pip
- Windows (for `.bat`/`.ps1` scripts) or any OS for manual setup

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for the full list of contributors and collaborators.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author & Collaborators

**Archit Agrawal** — Creator & Maintainer
- GitHub: [@Architcybercrime](https://github.com/Architcybercrime)
- Email: architagrawalking@gmail.com
- LeetCode: [leetcode.com/u/yO3MAhboDD](https://leetcode.com/u/yO3MAhboDD/)

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for all collaborators.

---

*Built with ❤️ using Flask — learning backend web development one route at a time.*
