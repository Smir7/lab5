<< 'EOF'
#!/usr/bin/env python3

import sys
import datetime
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello AppSec World with Flask!"

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat()
    })

def main():
    print(f"Starting Flask app at {datetime.datetime.now()}")
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
EOF
