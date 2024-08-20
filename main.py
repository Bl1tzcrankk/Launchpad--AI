from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from g4f.client import Client

app = Flask(__name__)
CORS(app)

@app.route("/")
def generateText():
    try:
        prompt = request.args.get("prompt")
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
        )
        return jsonify({"success": True, "data": response.choices[0].message.content})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "data": str(e)})

if __name__ == "__main__":
    app.run("0.0.0.0", 6000, debug=False)
