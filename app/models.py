from app import db, ma

class Account(db.Model) :
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(100), nullable = False, unique = True)
    email = db.Column(db.String(100), nullable = False, unique = True)
    password = db.Column(db.String(100), nullable = False, unique = False)
    phone = db.Column(db.String(100), nullable = False)
    wilaya = db.Column(db.String(100), nullable = False)
    region = db.Column(db.String(100), nullable = False)
    photo = db.Column(db.String(100), nullable = False)
    
    
    def __init__(self, username, email, password, phone, wilaya, region, photo):
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.wilaya = wilaya
        self.region = region 
        self.photo = photo
        
class AccountSchema(ma.Schema) :
    class Meta : 
        fields = ('id','username','email','password','phone','wilaya','region','photo')  