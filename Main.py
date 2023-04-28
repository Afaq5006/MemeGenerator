import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("memeGeneration.html")

@app.route("/webhookcallback", methods=["POST"])
def generate_meme():
    image_url = request.form.get("image-url")
    
    data = {
        "cmd": "imagine",
        "msg": f"Generate a funny meme using this image: {image_url}",
        "ref": "",
        "webhookOverride": request.url_root + "receive-meme"
    }
    headers = {
        "Authorization": "Bearer <your-token>",
        "Content-Type": "application/json"
    }
    
    response = requests.post("https://api.thenextleg.io/api", json=data, headers=headers)
    webhook_data = response.json()
    
    return render_template("memeResult.html", image_url=webhook_data["outputImageUrl"])

@app.route("/receive-meme", methods=["POST"])
def receive_meme():
    webhook_data = request.json
    if webhook_data["status"] == "success":
        return {"outputImageUrl": webhook_data["outputImageUrl"]}
    else:
        return {"error": webhook_data["error"]}

if __name__ == '__main__':
    app.run()


# from flask import Flask, render_template

# app = Flask(__name__)
# @app.route("/")
# def main():
# 	return render_template("memeGeneration.html")

# if __name__ == '__main__':
# 	app.run()