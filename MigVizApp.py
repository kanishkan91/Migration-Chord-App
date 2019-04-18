from flask import Flask, flash, redirect, render_template, request, session, abort,send_from_directory,send_file,jsonify
import pandas as pd

import json

#dfP=pd.read_excel(r'C:\Users\Public\Pythonfiles\CropsFull.xlsx')



app= Flask(__name__)

class DataStore():
    CountryName=None
    Year=None
    Prod= None
    Africa=None
data=DataStore()




@app.route("/main",methods=["GET","POST"])

@app.route("/",methods=["GET","POST"])
def homepage():
    #CountryName = request.form.get('Country_field','India')
    #print(CountryName)
    #Year = request.form.get('Year_field', 2013)
    #data.CountryName=CountryName
    #data.Year=Year
    #df = pd.read_csv(r'C:\Users\Public\Pythonfiles\FlowDataforOnlineVizVersion2.csv')
    # dfP=dfP
    CountryName = data.CountryName
    data.CountryName = CountryName
    with open('migrations.json') as json_file:
        df = json.load(json_file)
    datadisplay = df

    data.Prod=datadisplay
    with open('Africa.json') as json_file:
        Afr = json.load(json_file)
    datadisplay2 = Afr
    print(datadisplay2)
    data.Africa=datadisplay2
    # print(CountryName)
    #Year = data.Year
    #data.Year = Year

    # choose columns to keep, in the desired nested json hierarchical order




    return render_template("try2.html")


@app.route("/get-data",methods=["GET","POST"])
def returnMigData():
    d=data.Prod
    return ((jsonify(d)))
# export the final result to a json file

@app.route("/get-Africa-Data",methods=["GET","POST"])
def returnAfricaData():
    a=data.Africa
    return ((jsonify(a)))


if __name__ == "__main__":
    app.run(debug=True)
