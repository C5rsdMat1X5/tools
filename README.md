# 🧰 Ultimate Python Tools Collection

This repository contains a set of useful Python scripts and tools, organized by folder according to their purpose. Each module is self-contained, with its own dependencies if needed. It's a collection of small apps created for learning by doing—nothing too serious.

## 📁 Project Structure

```bash
.
├── calculators/             # Simple math calculators
├── instagram-unfollower/    # Instagram unfollow tool (not part of this repo)
├── random-tools/            # Miscellaneous tools
├── stock-inventory-app/     # Inventory app using JSON files
└── voice-assistant/         # Voice assistant (not part of this repo)
```

## ⚙️ General Installation

```bash
# Clone the repository
git clone https://github.com/C5rsdMat1X5/tools
cd tools

# Create and activate a virtual environment (optional but recommended)
python3 -m venv venv

# For Linux/macOS:
source venv/bin/activate

# For Windows:
venv\Scripts\activate
```

### Install dependencies per module (if available):

```bash
# For calculators
cd calculators
pip install -r requirements.txt

# For random tools
cd ../random-tools
pip install -r requirements.txt
```

---

## 📦 Folder Descriptions

### `calculators/`

Includes basic calculator scripts:

* `currency-converter.py`: Currency conversion.
* `ecuations-calculator.py`: Solves equations (yes, spelled with an "e").
* `factorial-calculator.py`: Computes factorials.
* `simple-calculator.py`: Basic arithmetic operations.
* `requirements.txt`: Required dependencies.

### `random-tools/`

Miscellaneous utilities:

* `text-chain-generator.py`: Text chain generator.
* `youtube-downloader.py`: Download YouTube content.
* `requirements.txt`: Required dependencies.

### `stock-inventory-app/`

Mini inventory management app:

* `main.py`: Entry point.
* `data/inventory.py`: Inventory logic.
* `data/inventory.json`: Local inventory data.

---

## 🐍 General Requirements

* Python 3.8+
* Install dependencies with `pip` using the `requirements.txt` in each folder

---

## 🧠 Contributions

Pull requests and suggestions are welcome. Memes about your procrastination while using these scripts are also accepted.

---

## 📌 Final Note

The `voice-assistant/` and `instagram-unfollower/` folders are **not part of this repository** and are maintained separately as part of other projects.

---

## 🧠 Author

Developed by Matías Henríquez.
