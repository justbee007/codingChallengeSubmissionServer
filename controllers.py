from app import app,db
from flask import request, jsonify
from services import getcountydata
from models import CountyPopulation
from services import pigLatinConversion
@app.route('/create_phrase',methods=['POST'])
def index():
    if request.method=='POST':
        # if(request.is_json==True):
        print(request.json)
        inputVal  = request.json
        nameVal = pigLatinConversion(inputVal['name'])
        countyDetail = getcountydata(inputVal['zipcode'],db)
        if(countyDetail!=None):
            nameVal.update(countyDetail)
        else:
            return {'message':'Please enter a valid zip code'}    
        return nameVal
    else:
        return {'message':'Please send JSON in request body'}

# if __name__ == '__main__':
#     app.run(debug=True)