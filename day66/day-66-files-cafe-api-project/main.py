from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.

'''

# Link to published API documentation (POSTMAN)


# https://documenter.getpostman.com/view/31112532/2sA3s3HrLc

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def randomCafe():
    results = db.session.execute(db.select(Cafe)).scalars().all()
    cafe = random.choice(results) 
    return  jsonify(shop=cafe.to_dict())

@app.route("/all", methods=["GET"])
def allCafe():
    cafe_list=[]
    results = db.session.execute(db.select(Cafe)).scalars().all()
    for cafe in results:
        cafe_list.append(cafe.to_dict())
    return  jsonify(shop=cafe_list)

@app.route("/search", methods=["GET"])
def locationCafe():
    location = request.args.get("loc")  # argumet from URL curl get request using ?loc=variable
    location_list=[]
    results = db.session.execute(db.select(Cafe).where(Cafe.location==location.title())).scalars().all()
    if not results or results is None:
        return jsonify({"error":{"Not Found":"Sorry we don't have a cafe at that location"}}), 404
    else:
        for cafe in results:
            location_list.append(cafe.to_dict())
        return  jsonify(shop=location_list)

# https://learning.postman.com/docs/publishing-your-api/documenting-your-api/
    
# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def addCafe():
               
        # CREATE RECORD
        with app.app_context():
            new_cafe = Cafe(id=request.form.get("id"), name= request.form.get("name"), \
                        map_url=request.form.get("map_url"), location=request.form.get("location"), \
                      seats=request.form.get("seats"), has_toilet=bool(request.form.get("has_toilet")),\
                     has_wifi=bool(request.form.get("has_wifi")), has_sockets=bool(request.form.get("has_sockets")),\
              can_take_calls=bool(request.form.get("can_take_calls")), coffee_price=request.form.get("coffee_price"),\
                img_url=request.form.get("img_url"))
            
            db.session.add(new_cafe)
            db.session.commit()
        
        return jsonify({"response":{"Success":"Successfully added a new Cafe!"}})



# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:id>", methods=["PATCH"])
def updatePrice(id):
               
        # UPDATE RECORD
        with app.app_context():
            
            result = db.session.execute(db.select(Cafe).where(Cafe.id==id)).scalar()
            if result:
                result.coffee_price = request.args.get("new_price")
                db.session.commit()
                return jsonify(response={"success": "Successfully updated the price."}), 200
            else:
                #404 = Resource not found
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
            # OR
            
            # new_price = request.args.get("new_price")
            # result = db.get_or_404(Cafe, id)
            # if result:
            #     result.coffee_price = new_price
            #     db.session.commit()
            #     ## Just add the code after the jsonify method. 200 = Ok
            #     return jsonify(response={"success": "Successfully updated the price."}), 200
            # else:
            #     #404 = Resource not found
            #     return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete(id):
               
        # UPDATE RECORD
        with app.app_context():
            
            if request.args.get("api-key") == "TopSecretAPIKey":
                 result = db.session.execute(db.select(Cafe).where(Cafe.id==id)).scalar()
                 if result:
                      db.session.delete(result)
                      db.session.commit()
                      return jsonify(response={"success": "Record Successfully removed"}), 200
                 else:
                     #404 = Resource not found
                     return jsonify(error={"Not Found": "Sorry record not found in the database."}), 404
            return jsonify(error={"Access denied": " Unauthorized request."}), 403

if __name__ == '__main__':
    app.run(debug=True)
