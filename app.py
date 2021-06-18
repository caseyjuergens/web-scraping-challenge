from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#create instance of flask
app = Flask(__name__)

# Use pymongo to set up mongo connection
conn="mongodb://localhost:27017"
client=PyMongo.MongoClient(conn)

#create mars db
db=client.mars_db
mars= db.mars

@app.route("/")
def index():
    #find one record of data from the database
    mars_data = mars.find_one()
    #return template and data
    return render_template("index.html", dict=mars_data)


@app.route("/scrape")
def scrape():
    #run scrape function
    scrape_dict = scrape_mars.scrape()
    #update mongo database 
    mars.update({}, scrape_dict, upsert=True)
    #redirect back to homepage
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)