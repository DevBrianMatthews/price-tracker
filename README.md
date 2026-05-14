# 📉 Price Tracker

Price Tracker is a tool to track product prices and notify you via Telegram when prices drop.

---

## 📋 Requirements

- Python 3.10+
- Telegram account

---

## ⬇️ Installation

1. Clone the repository

```bash
git clone https://github.com/DevBrianMatthews/price-tracker.git
cd price-tracker
```

2. Create and activate a virtual environment

```bash
python -m venv env
source env/bin/activate        # Mac/Linux
env\Scripts\activate           # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔗 Dependencies

| Library               | Purpose                             |
| --------------------- | ----------------------------------- |
| `requests`            | Downloads the HTML from the website |
| `beautifulsoup4`      | Parses the HTML                     |
| `python-telegram-bot` | Connects the app with Telegram      |
| `APScheduler`         | Schedules periodic price checks     |
| `python-dotenv`       | Loads environment variables         |

---

## 🔑 Credentials

Create a `.env` file and add your credentials:

```
TELEGRAM_TOKEN=
TELEGRAM_CHAT_ID=
```

You can also copy the contents of `.env.example`, create a `.env` file and fill in your credentials.

---

## 🚀 Usage

Add the URL of the product you want to track to `scheduler.py` and create a file for that store in the `/scrapers` directory, for example `amazon.py`. Implement the HTML parsing logic to extract the price — you can use the existing scraper files as reference.

To run **Price Tracker**:

```bash
python scheduler.py
```

| ℹ️ **Price Tracker** uses **SQLite** to store products and their prices.

---

## ⚠️ Limitations

- Each product URL must be added manually.
- The HTML element containing the price must be identified manually using the browser's DevTools.

---

## 📄 License

MIT License — feel free to use and modify this project.
