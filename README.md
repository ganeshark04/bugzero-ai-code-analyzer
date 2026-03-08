# 🐞 BugZero AI | Pro IDE

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![AI](https://img.shields.io/badge/AI-Groq%20LLM-orange)
![Testing](https://img.shields.io/badge/Testing-TestSprite-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

BugZero AI is an **AI-powered code analysis platform** that helps developers detect bugs, understand issues, and generate improved code automatically.

It provides an interactive **browser-based IDE** where users can write code, run programs, and receive AI-driven debugging insights.

Built for the **TestSprite AI Dev Hackathon**.

---

# 🚀 Features

* 🔍 **AI Bug Detection** – Automatically identifies coding mistakes
* 💡 **Technical Explanation** – Explains why the bug occurs
* 🛠 **Auto Fix Suggestions** – Provides corrected code
* ▶ **Integrated Code Runner** – Run code directly in the browser
* 🌐 **Multi-language Support** – Python & Java
* 🧪 **Automated Testing** – Test cases generated using TestSprite MCP

---

# 🎬 Demo

## Python Bug Analysis

![Python Demo](python-demo.png)

---

## Java Bug Analysis

![Java Demo](java-demo.png)

---

# 🧠 How It Works

1️⃣ Write code in the **BugZero editor**
2️⃣ Click **Analyze**
3️⃣ Code is sent to the **Groq LLM API**
4️⃣ AI returns:

* Bug detection
* Explanation
* Suggested fix
* Improved code

---

# 🏗 Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask

### AI

* Groq API (LLaMA model)

### Testing

* TestSprite MCP

---

# 📂 Project Structure

```id="q3r0vo"
bugzero-ai-code-analyzer
│
├── app.py
├── index.html
├── requirements.txt
├── README.md
│
├── python-demo.png
├── java-demo.png
│
└── testsprite_tests
    └── api_test.js
```

---

# ⚙ Installation

Clone the repository:

```id="o46cav"
git clone https://github.com/ganeshark04/bugzero-ai-code-analyzer
```

Navigate to project folder:

```id="oq0m8g"
cd bugzero-ai-code-analyzer
```

Install dependencies:

```id="h37mpk"
pip install -r requirements.txt
```

Run the application:

```id="j7gx3y"
python app.py
```

Open in browser:

```id="23xvab"
http://127.0.0.1:5000
```

---

# 🧪 Testing

This project integrates **TestSprite MCP** for automated test generation.

Generated tests are located in:

```id="p1p6qk"
testsprite_tests/
```

These tests validate:

* API endpoints
* UI interactions
* Edge cases

---

# 🎯 Example

### Input Code

```python id="vnpv3j"
def divide(a,b):
    return a/b

print(divide(10,0))
```

### AI Output

BUG: Division by zero

WHY: The function does not check if the divisor is zero.

FIXED CODE:

```python id="sj9jqq"
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b
```

---

# 👨‍💻 Author

**Gagan Rao K**

---

# 📜 License

MIT License
