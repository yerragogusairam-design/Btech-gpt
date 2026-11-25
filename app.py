
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/style.css")
def css():
    return send_from_directory(BASE_DIR, "style.css")

@app.route("/script.js")
def javascript():
    return send_from_directory(BASE_DIR, "script.js")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    question = data.get("message", "").strip()

    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    q = question.lower()

    topics = {
        "python": """Python is a popular programming language.

Main features:
1. Easy to learn and read.
2. Simple syntax.
3. Supports object-oriented programming.
4. Used in AI, web development and data science.

Example:
print("Hello World")""",

        "c programming": """C is a general-purpose programming language.

Features:
1. Fast execution.
2. Structured programming.
3. Supports pointers.
4. Used in system programming.

Example:
#include <stdio.h>
int main() {
    printf("Hello World");
    return 0;
}""",

        "java": """Java is a high-level, object-oriented programming language.

Features:
1. Platform independent.
2. Secure and reliable.
3. Object-oriented.
4. Used in web and mobile applications.

Example:
class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}""",

        "dbms": """DBMS stands for Database Management System.

It is software used to store and manage data.

Examples:
1. MySQL
2. Oracle
3. PostgreSQL

Advantages:
- Data security.
- Less data duplication.
- Easy data management.""",

        "data structures": """Data Structures are ways of organizing and storing data.

Types:
1. Array
2. Linked List
3. Stack
4. Queue
5. Tree
6. Graph

They help us manage data efficiently.""",

        "computer networks": """A Computer Network connects computers to share information.

Types:
1. LAN - Local Area Network
2. MAN - Metropolitan Area Network
3. WAN - Wide Area Network

Examples: Internet and college networks.""",

        "operating system": """An Operating System manages computer hardware and software.

Examples:
1. Windows
2. Linux
3. macOS
4. Android

Functions:
- Memory management.
- File management.
- Process management.""",

        "html": """HTML stands for HyperText Markup Language.

It is used to create the structure of web pages.

Example:
<h1>Hello World</h1>
<p>Welcome to BTech GPT</p>"""
    }

    answer = None

    for topic, content in topics.items():
        if topic in q:
            answer = content
            break

    if answer is None:
        answer = f"""Welcome to BTech GPT Free Demo Mode!

Your question:
{question}

This topic is not available yet.

Available topics:
Python, C Programming, Java, DBMS,
Data Structures, Computer Networks,
Operating System and HTML.

More topics will be added soon."""

    return jsonify({
        "answer": answer,
        "mode": "Free Demo"
    })

if __name__ == "__main__":
    app.run(debug=True)


