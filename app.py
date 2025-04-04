from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# connect to api
API_URL = "http://127.0.0.1:5000/classify"

# folder for images
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if "file" not in request.files:
            return "No image uploaded!", 400

        file = request.files["file"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # send POST to api
        response = requests.post(API_URL, files={"image": open(filepath, "rb")})

        if response.status_code == 200:
            result = response.json()

            # # get colors
            prediction = result.get("food", [])
            #color_names = [item[0].lower() for item in prediction]

            return render_template("index.html", filename=file.filename, food=prediction)
        else:
            return "Error in processing", 500
    
    return render_template("index.html", filename=None)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)