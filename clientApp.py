from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from utility_codes.utils import decodeImage
from predict import dogcat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)




#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"  #gives the name to the uploaded image 
        self.classifier = dogcat(self.filename) #defines the object of dogcat class with passing
                                           #the uploaded image as file



@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html') #renders the initial html template requesting the
                                #user to upload the image to be predicted
    


@app.route("/predict", methods=['POST']) #Executes below function when the user clicks on the
                                         #predict button
@cross_origin()
def predictRoute():
    image = request.json['image'] #gets the uploaded image
    decodeImage(image, ClientApp().filename) #calls the utility function to decode the uploaded
                                 #image to base64 image data and writes that image data to the
                                #file name given by ClientApp() i.e. inputiamge.jpg
    result = ClientApp().classifier.predictiondogcat() # Gets the predicted out put from 
                                 #calling predictiondogcat() method of dogcat() class
                                 #jsonifies the predicted result to display on the html 
    return jsonify(result)        #template
                             

#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp() #defining the object of ClientApp class
    #app.run(host='0.0.0.0', port=port)
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run()
