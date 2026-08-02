from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

# Encode function
def encode(msg):
    key = random.randint(1,5)

    encoded = ""
    for ch in msg:
        encoded += chr(ord(ch) + key)

    encoded = encoded[::-1]

    rand = ''.join(random.choice(string.ascii_letters) for _ in range(4))
    secret = rand + encoded + rand

    return secret, key


# Decode function
def decode(secret, key):
    secret = secret[4:-4]
    secret = secret[::-1]

    decoded = ""
    for ch in secret:
        decoded += chr(ord(ch) - key)

    return decoded


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Encode API
@app.route("/encode", methods=["POST"])
def encode_api():
    msg = request.json["message"]
    code, key = encode(msg)
    return jsonify({"code": code, "key": key})


# Decode API
@app.route("/decode", methods=["POST"])
def decode_api():
    code = request.json["code"]
    key = int(request.json["key"])
    message = decode(code, key)
    return jsonify({"message": message})


if __name__ == "__main__":
    app.run(debug=True)