# Flask Market

A Flask-based marketplace web application where users can buy and sell items. This project demonstrates a complete e-commerce platform with user authentication, item management, and transaction handling.

## Features

- **User Authentication**: Complete user registration and login system with password hashing using Flask-Bcrypt
- **User Budget Management**: Each user starts with a $1000 budget and can add funds
- **Item Marketplace**: Browse available items with search, sorting, and pagination
- **Buy/Sell Items**: Purchase items from the market or sell your owned items back
- **Item Management**: Add, edit, and delete items you own
- **User Profile**: View your owned items and account information
- **Responsive UI**: Clean, user-friendly interface with Bootstrap styling

## Technologies Used

- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Flask-WTF & WTForms**: Form handling and validation
- **Flask-Bcrypt**: Password hashing
- **SQLite**: Database
- **Pillow**: Image processing

## Project Structure

```
Flask_Market/
├── market/                    # Main application package
│   ├── __init__.py           # App initialization
│   ├── models.py             # Database models (User, Item)
│   ├── routes.py             # Application routes
│   ├── forms.py              # WTForms for user input
│   └── templates/            # HTML templates
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── create_db.py              # Database creation script
├── seed_demo.py              # Seed database with demo data
├── seed_items.py             # Seed database with items
├── run_all.bat               # Windows quick-start script
└── run_all.ps1               # PowerShell quick-start script
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Quick Start (Windows)

**Option 1: One-click runner**
- Double-click `run_all.bat`
- OR right-click `run_all.ps1` and select "Run with PowerShell"

This automatically:
- Creates a virtual environment
- Installs all dependencies
- Seeds the database with demo data
- Starts the Flask application

**Option 2: Manual Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/Architcybercrime/Flask_Market.git
   cd Flask_Market
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database**
   ```bash
   python create_db.py
   ```

6. **Seed demo data (optional)**
   ```bash
   python seed_demo.py
   ```
   This creates:
   - Demo user (username: `demo`, password: `password123`)
   - Sample items in the marketplace

7. **Run the application**
   ```bash
   python run.py
   ```

8. **Access the application**
   Open your web browser and navigate to: `http://127.0.0.1:5000`

## Usage

### Getting Started

1. **Register a new account** or use the demo account:
   - Username: `demo`
   - Password: `password123`

2. **Browse the marketplace** to view available items
   - Use the search bar to find specific items
   - Sort items by price or name
   - Navigate through pages if there are many items

3. **Purchase items** if you have sufficient budget
   - Click on an item to view details
   - Click "Purchase" to buy the item

4. **Manage your items**:
   - View your owned items in your profile
   - Add new items to the marketplace
   - Edit or delete items you own
   - Sell items back to the market

5. **Add funds** to increase your budget when needed

### Key Routes

- `/` or `/home` - Home page
- `/register` - User registration
- `/login` - User login
- `/market` - Marketplace (browse and buy items)
- `/profile` - User profile and owned items
- `/add_item` - Add a new item
- `/add_funds` - Add funds to your budget
- `/logout` - Logout

## Database Schema

### User Model
- `id`: Unique identifier
- `username`: Unique username (2-30 characters)
- `email_address`: Unique email address
- `password_hash`: Hashed password
- `budget`: User's available funds (default: $1000)
- `items`: Relationship to owned items

### Item Model
- `id`: Unique identifier
- `name`: Item name (unique)
- `price`: Item price
- `barcode`: Unique barcode (8-12 characters)
- `description`: Item description
- `owner`: Foreign key to User (null if available in market)

## Development

### Running in Debug Mode

The application runs in debug mode by default when started with `python run.py`. This enables:
- Auto-reload on code changes
- Detailed error pages
- Interactive debugger

**Note**: Disable debug mode in production by modifying `run.py`:
```python
app.run(debug=False)
```

### Adding New Features

1. Define models in `market/models.py`
2. Create forms in `market/forms.py`
3. Add routes in `market/routes.py`
4. Create templates in `market/templates/`

## Security Considerations

- Passwords are hashed using Flask-Bcrypt
- Flask-Login manages user sessions securely
- CSRF protection enabled through Flask-WTF
- Input validation on all forms

**Important**: Change the `SECRET_KEY` in `market/__init__.py` before deploying to production:
```python
app.config['SECRET_KEY'] = 'your-secure-secret-key-here'
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.

## Acknowledgments

Built with Flask and various Flask extensions to demonstrate a full-stack web application with authentication, database management, and CRUD operations.
