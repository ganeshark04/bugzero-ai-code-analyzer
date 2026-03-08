# 🐞 BugZero AI – Code Analyzer & Bug Finder

BugZero AI is an **AI-powered code analysis tool** that detects bugs, explains issues, and generates improved code automatically.

It helps developers quickly understand errors in their code and learn how to fix them using AI.

This project was built for the **TestSprite AI Dev Hackathon**.

---

# 🚀 Features

* 🔍 **AI Code Analysis** – Detect bugs and logical issues
* 💡 **Bug Explanation** – Understand why the error occurs
* 🛠 **Fix Suggestions** – AI recommends solutions
* 🧠 **Improved Code Output** – Generates corrected code
* ▶ **Code Runner** – Execute code directly in the browser
* 🧪 **Automated Tests** – Tests generated using TestSprite MCP

---

# 🧠 How It Works

1. User pastes code into the web editor
2. The backend sends the code to an AI model
3. The AI analyzes the code and detects bugs
4. BugZero returns:

   * Bug description
   * Explanation
   * Fix recommendation
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

### AI Model

* Groq API (LLaMA 3.1)

### Testing

* TestSprite MCP

---

# 📂 Project Structure

```
bugzero-ai-code-analyzer
│
├── app.py
├── index.html
├── requirements.txt
├── README.md
│
└── testsprite_tests
    └── api_test.js
```

---

# 🖥 Demo Screenshot

![BugZero Screenshot](screenshot.png)

---

# ⚙ Installation

Clone the repository:

```
git clone https://github.com/ganeshark04/bugzero-ai-code-analyzer
```

Navigate into the project folder:

```
cd bugzero-ai-code-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# 🧪 Testing

This project uses **TestSprite MCP** to generate automated test cases.

All generated tests are located inside:

```
testsprite_tests/
```

Test categories include:

* API testing
* UI interaction testing
* Edge case validation

---

# 🎯 Example

### Input Code

```python
def divide(a,b):
    return a/b

print(divide(10,0))
```

### AI Output

BUG: Division by zero.

WHY: The function does not check if the divisor is zero.

FIX: Add validation before division.

FIXED CODE:

```python
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b
```

---

# 📌 Hackathon Submission

This project was developed for the **TestSprite AI Dev Hackathon** to demonstrate how AI can improve software quality by automatically detecting bugs and generating fixes.

---

# 👨‍💻 Author

**Gagan Rao K**

---

# 📜 License

MIT License
