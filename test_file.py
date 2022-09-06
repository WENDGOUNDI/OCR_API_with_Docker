# Libraries Importation
import base64
import requests

# Below we have the API KEY + TOKEN
url = "http://127.0.0.1:5000/image_label?key=5FDVakRB0a0NvPwMr"

with open("wire_label_content_1.PNG", "rb") as image_file:
    image = base64.b64encode(image_file.read())


# Feed the API with the data
data = {"base64string": str(image)}
r = requests.post(url, json=data)
print(r.text)