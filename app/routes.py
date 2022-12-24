from flask import jsonify, request
from app import app, db
from app.models import Account, AccountSchema, PostSchema, Post
import pickle
from joblib import load



account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)   

@app.get("/accounts")
def get_accounts(): 
    all_accounts = Account.query.all()
    accounts = accounts_schema.dump(all_accounts)
    print(accounts)
    return jsonify(accounts)


@app.get("/accounts/<id>")
def get_account(id):
    account = Account.query.get(id)
    return account_schema.jsonify(account)

@app.post("/accounts")
def create_account():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    wilaya = request.json['wilaya']
    photo = request.json['photo']
    
    account = Account(username, email, password, phone, wilaya, photo)
    
    db.session.add(account)
    db.session.commit()
    return account_schema.jsonify(account)
    

@app.put("/accounts/<id>")
def update_account(id) :
    account = Account.query.get(id)
    
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    wilaya = request.json['wilaya']
    photo = request.json['photo']
    
    account.username = username
    account.email = email
    account.password = password
    account.phone = phone
    account.wilaya = wilaya
    account.photo = photo
    db.session.commit()
    return account_schema.jsonify(account)


@app.delete("/accounts/<id>")
def delete_user(id) :
    account = Account.query.get(id)
    db.session.delete(account)
    db.session.commit()  
    return account_schema.jsonify(account)







post_schema = PostSchema()
posts_schema = PostSchema(many=True)

@app.get("/posts")
def get_posts(): 
    all_posts = Post.query.all()
    posts = posts_schema.dump(all_posts)
    return jsonify(posts)

@app.post("/posts")
def create_post():
    name = request.json['name']
    year = request.json['year']
    price = request.json['price']
    km_driven = request.json['km_driven']
    fuel = request.json['fuel']
    seller_type = request.json['seller_type']
    transmission = request.json['transmission']
    owner_id = request.json['owner_id']
    mileage = request.json['mileage']
    engin = request.json['engin']
    max_power = request.json['max_power']
    torque = request.json['torque']
    seats = request.json['seats']
    # deposit_date = request.json['deposit_date']
    
    post = Post(name, year, price, km_driven, fuel, seller_type, transmission, owner_id, mileage, engin, max_power, torque, seats)
    
    db.session.add(post)
    db.session.commit()
    return account_schema.jsonify(post)









# clf = load("model.pkl")

# @app.post('/prediction')
# def calcul():
#     year = request.json['year']
#     engine = request.json['engin']
#     max_power = request.json['max_power']
#     table = [[year, engine, max_power]]
#     prediciton_prix = clf.predict(table)
#     return jsonify({
#         'valeur predite': prediciton_prix,
#     })






