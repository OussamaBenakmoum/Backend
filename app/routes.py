from flask import jsonify, request
from app import app, db
from app.models import Account, AccountSchema


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
    region = request.json['region']
    photo = request.json['photo']
    
    account = Account(username, email, password, phone, wilaya, region, photo)
    
    db.session.add(account)
    db.session.commit()
    return account_schema.jsonify(account)
    # return user_schema.jsonify(user)
    


@app.put("/accounts/<id>")
def update_account(id) :
    account = Account.query.get(id)
    
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    wilaya = request.json['wilaya']
    region = request.json['region']
    photo = request.json['photo']
    
    account.username = username
    account.email = email
    account.password = password
    account.phone = phone
    account.wilaya = wilaya
    account.region = region 
    account.photo = photo
     
    db.session.commit()
    
    return account_schema.jsonify(account)