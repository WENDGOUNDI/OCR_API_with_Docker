from flask import Flask, request, jsonify
import base64
from flask_cors import CORS
import json
from paddleocr import PaddleOCR
from PIL import Image
from io import BytesIO
ocr =  PaddleOCR(lang='en', show_log=False, use_angle_cls=False, use_gpu=False)

AUTHENTICATION_KEY = "5FDVakRB0a0NvPwMr"
#AUTHENTICATION_KEY = 'mykey345'

app = Flask(__name__)
CORS(app)

@app.route('/image_label', methods=["POST"])
def image_label():
    
    key = request.args.get('key', None)
    if key and key == AUTHENTICATION_KEY:

        image_bas64_string = request.json['base64string']
        
        if image_bas64_string:
            if image_bas64_string[:2] == "b'":
                image_bas64_string = image_bas64_string[2:]
            if image_bas64_string[-1] == "'":
                image_bas64_string = image_bas64_string[:-1]


            im = Image.open(BytesIO(base64.b64decode(image_bas64_string)))
            api_image = im.save('converted_images.png', 'PNG')

            result = ocr.ocr("converted_images.png")
            result_list = list()
            for line in result:
                #print(line[1][0])
                result_list.append(line[1][0])
            json_file_result = jsonify({'Ocr_Output':result_list})
            
            return json_file_result
    else:
        result = {
            "ProcessType":"F",
            "ErrorMessage":"Authentification error"}
        return jsonify(response=result), 401
            
            
if __name__ == "__main__":
    app.run(debug=True)


