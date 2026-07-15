# FastAPI Workshop

This repository contains the starter code for the FastAPI workshop.

## Prerequisites

Before the workshop, please make sure you have the following installed:

- Python 3.11 or newer

Verify your Python installation:

```bash
python --version
```

If that doesn't work, try:

```bash
python3 --version
```

---

## Getting Started

### 1. Clone the repository, or download the zip file

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
```

### 2. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
```

**Windows**

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

You should now see `(.venv)` at the beginning of your terminal prompt.

### 4. Install the project dependencies

```bash
pip install -r requirements.txt
```

If `pip` is not available, use:

```bash
python -m pip install -r requirements.txt
```

### 5. Start the FastAPI development server

```bash
uvicorn app.main:app --reload
```

You should see output similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## Accessing the API

Once the server is running, open your browser and visit:

- **Application:** http://127.0.0.1:8000

---

## Project Structure

```text
.
├── app/
│   └── main.py
├── requirements.txt
├── data.json
└── README.md
```

---

## Troubleshooting

### `python` is not recognized

Try using:

```bash
python3
```

instead of:

```bash
python
```

### `pip` is not recognized

Run:

```bash
python -m pip install -r requirements.txt
```

or

```bash
python3 -m pip install -r requirements.txt
```

### Still having issues?

Please let the instructor know before the workshop starts so we can get everything working.