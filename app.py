from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#create instance of flask
app = Flask(__name__)

# Use pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
client=PyMongo(app)

@app.route("/")
def index():
    #find one record of data from the database
    mars_data = client.db.mars.find_one()
    #return template and data
    return render_template("index.html", dict=mars_data)


@app.route("/scrape")
def scrape():
    #run scrape function
    scrape_dict = scrape_mars.scrape()
    #update mongo database 
    client.db.mars.update({}, scrape_dict, upsert=True)
    #redirect back to homepage
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)