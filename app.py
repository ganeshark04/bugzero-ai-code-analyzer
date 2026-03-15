import os
import sys
import subprocess
import tempfile
import webbrowser
from threading import Timer
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# --- CONFIGURATION ---
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def open_browser():
    webbrowser.open("http://127.0.0.1:3000")

@app.route("/")
def home():
    return send_file("index.html")

# --- MULTI-LANGUAGE RUNNER (Python & Java 21) ---
@app.route("/run", methods=["POST"])
def run_code():
    data = request.json
    code = data.get("code", "")
    language = data.get("language", "python")
    
    if not code.strip():
        return jsonify({"output": "Console: No code to execute."})

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            if language == "python":
                file_path = os.path.join(temp_dir, "main.py")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code)
                # Run Python
                result = subprocess.run([sys.executable, file_path], capture_output=True, text=True, timeout=5)
            
            elif language == "java":
                # For Java 21 single-file execution, the filename doesn't strictly have to match
                # the class name, but 'Main.java' is best practice.
                file_path = os.path.join(temp_dir, "Main.java")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(code)
                # Run Java 21 (Single file mode is much faster)
                result = subprocess.run(["java", file_path], capture_output=True, text=True, timeout=10)
            
            else:
                return jsonify({"output": "Error: Language not supported."})

            output = result.stdout
            if result.stderr:
                output += f"\n[Runtime Error/Warning]\n{result.stderr}"
            
            return jsonify({"output": output or "Program executed successfully (No output)."})

    except subprocess.TimeoutExpired:
        return jsonify({"output": "Error: Execution timed out (Possible infinite loop)."})
    except Exception as e:
        return jsonify({"output": f"System Error: {str(e)}"})

# --- AI PROFESSIONAL ANALYSIS ---
@app.route("/analyze", methods=["POST"])
def analyze_code():
    try:
        data = request.json
        input_code = data.get("code", "")
        language = data.get("language", "python")

        # Professional Prompt Template
        # We use .format() to avoid the 'unterminated string' f-string error
        prompt_template = """
        You are a Senior Software Architect. Analyze this {lang} code.
        
        STRICT RULES:
        1. If Java, ensure 'import java.util.*;' is included if needed.
        2. Ensure Java code uses 'public class Main'.
        3. Identify logic bugs and provide a clean, optimized fix.

        FORMAT:
        ### 🐞 Bug Detected
        - **WHY:** [Explain the logic error]
        - **FIX:** [Explain the correction]
        
        **FIXED CODE:**
        ```{lang_lower}
        [Complete runnable code here]
        ```
        
        Code to analyze:
        {code_val}
        """
        
        user_prompt = prompt_template.format(
            lang=language.upper(),
            lang_lower=language,
            code_val=input_code
        )

        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": user_prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.1
        )
        return jsonify({"result": chat.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
