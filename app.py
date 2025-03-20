from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Sheik Sameer"  
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

    # Get system top output
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return f"""
    <h1>Internship Test: Q-TOP</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)