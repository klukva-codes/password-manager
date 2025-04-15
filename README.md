# 🔐 Password Auto-Fill Tool (Selenium)

A simple automation script using Selenium that auto-fills passwords from a local `data.json` file.  
This project is meant for educational use and personal productivity, not for storing sensitive data in public repositories.

---

## ⚠️ Important Note

This project uses a `data.json` file to store login credentials.  
**Do NOT upload this file to GitHub.**  
Make sure to include the filename in your `.gitignore`:

```
data.json
```

For production use, consider storing credentials in a `.env` file or encrypted vault.

---

## 🚀 Features

- Loads credentials from JSON file
- Opens browser and fills in login form
- Automates sign-in with Selenium

---

## 🛠️ Tech Stack

- Python 3
- Selenium WebDriver
- JSON for config storage

---

## ▶️ How to Run

1. Install the required packages:

```bash
pip install selenium
```

2. Place your credentials in a `data.json` file (do not share it!):

```json
{
  "email": "your-email@example.com",
  "password": "your-password"
}
```

3. Run the script:

```bash
python main.py
```

---

## 📁 File Structure

```
password-auto-fill/
├── main.py
├── .gitignore        # includes 'data.json'
├── data.json         # (NOT committed!)
└── README.md
```

---

## 🙋 Author

Created with ❤️ for automation fun by [klukva-codes](https://github.com/klukva-codes)
