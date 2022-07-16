from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app=Flask(__name__)



@app.route("/",methods=['GET','POST'])

def index():
    try:
        raise Exception("we are testing exception")
    except HousingException as e :
        logging.info (e)

    logging.info("logging pipeline checking")
    return "this is machine learning project"



if __name__=="__main__" :
    app.run(debug=True)