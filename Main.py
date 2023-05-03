from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('memeGeneration.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    # Get input values from the user
    image_url = request.form['image_url']
    description = request.form['description']

    # Call backend code with input values
    url = "https://api.thenextleg.io/api"
    payload = json.dumps({
        "cmd":"imagine",
        "imgUrl": image_url,
        "msg": description,
        "ref": "",
        "webhookOverride": ""
    })
    headers = {
      'Authorization': 'Bearer 4c6741d5-9907-4bfd-9bf6-f1ab9f901170',
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.loads(response.text)

    # Get generated image URL from the webhook response
    image_url = result['imgUrl']

    # Display the generated image on the frontend
    return render_template('memeGeneration.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)


# # import requests
# # from flask import Flask, render_template, request

# # app = Flask(__name__)

# # @app.route("/")
# # def main():
# #     return render_template("memeGeneration.html")

# # @app.route("/webhookcallback", methods=["POST"])
# # def generate_meme():
# #     image_url = request.form.get("image-url")
    
# #     data = {
# #         "cmd": "imagine",
# #         "msg": f"Generate a funny meme using this image: {image_url}",
# #         "ref": "",
# #         "webhookOverride": request.url_root + "receive-meme"
# #     }
# #     headers = {
# #         "Authorization": "Bearer <your-token>",
# #         "Content-Type": "application/json"
# #     }
    
# #     response = requests.post("https://api.thenextleg.io/api", json=data, headers=headers)
# #     webhook_data = response.json()
    
# #     return render_template("memeResult.html", image_url=webhook_data["outputImageUrl"])

# # @app.route("/receive-meme", methods=["POST"])
# # def receive_meme():
# #     webhook_data = request.json
# #     if webhook_data["status"] == "success":
# #         return {"outputImageUrl": webhook_data["outputImageUrl"]}
# #     else:
# #         return {"error": webhook_data["error"]}

# # if __name__ == '__main__':
# #     app.run()


# # # from flask import Flask, render_template

# # # app = Flask(__name__)
# # # @app.route("/")
# # # def main():
# # # 	return render_template("memeGeneration.html")

# # # if __name__ == '__main__':
# # # 	app.run()