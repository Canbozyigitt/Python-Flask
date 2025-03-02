from dataclasses import dataclass
from ecommerce import db


@dataclass #dataclass veri tabanına eklenicek olan tabloyu temsil eder 
class User(db.Model):   
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(120))
    email=db.Column(db.String(130))
    password=db.Column(db.String(120))


    def __init__(self,id,username,email,password):
        self.id=id
        self.username=username
        self.email=email
        self.password=password
    @classmethod
    def get_all_users(cls):# Bu yöntem, veritabanında bulunan tüm kullanıcıları sorgulamak için kullanılır 
        return cls.query.all() # bulunduğu sınıfın tüm kayıtlarını döndürür
    
    @classmethod
    def get_user_by(cls,id): #Bu yöntem, belirli bir kullanıcıyı ID'sine göre sorgulamak ve döndürmek için kullanılır.
        return cls.query.filter_by(id=id).first()#ID'si belirtilen değere eşit olan ilk kullanıcıyı döndürür. Eğer böyle bir kullanıcı yoksa None döner.
    
    @classmethod
    def add_user(cls,username,email,password):#Bu yöntem, yeni bir kullanıcı eklemek için kullanılır.
        user=cls(username,email,password)
        db.session.add(user)#yeni kullanıcı eklenir 
        db.session.commit()#değişiklikler kaydedilir    

    @classmethod
    def update_admin(cls,id,username,email,password):
        user=cls.query.filter_by(id=id).first()
        user.username=username
        user.email=email
        user.password=password
        db.session.commit()
    @classmethod
    def delete_user(cls,id):
        user=cls.query.filter_by(id=id).first()
        db.session.delete(user) 
        db.session.commit()






@dataclass
class Admin(db.Model):
    __tablename__='admin'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(120))
    email=db.Column(db.String(120))
    password=db.Column(db.String(120))
    mod=db.Column(db.Integer)


    def __init__(self,id,username,email,password,mod):
        self.id=id
        self.username=username
        self.email=email
        self.password=password
        self.mod=mod

    @classmethod
    def get_all_admins(cls):
        return cls.query.all()
    
    @classmethod
    def get_admin_by(cls,id):
        return cls.query.filter_by(id=id).first()
    @classmethod
    def add_admin(cls,username,email,password):
        admin=cls(username,email,password)
        db.session.add(admin)
        db.session.commit()  
    
    @classmethod
    def update_admin(cls,id,name,email,password,mod):
        admin=cls.query.filter_by(id=id).first()
        admin.name=name
        admin.email=email
        admin.password=password
        admin.mod=mod
        db.session.commit()

    @classmethod
    def delete_admin(cls,id):
        admin=cls.query.filter_by(id=id).first()
        db.session.delete(admin) 
        db.session.commit()

    
@dataclass
class Category(db.Model):
    __tablename__='category'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120))

    def __init__(self,id,name):
        self.id=id
        self.name=name

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()   
        

    @classmethod
    def get_category_by(cls,id):
        return cls.query.filter_by(id=id).first()
    @classmethod
    def add_category(cls,name):
        category=cls(name)
        db.session.add(category)
        db.session.commit()  
    
    @classmethod
    def update_category(cls,id,name):
        category=cls.query.filter_by(id=id).first()
        category.name=name
        db.session.commit()
    @classmethod
    def delete_category(cls,id):
        category=cls.query.filter_by(id=id).first()
        db.session.delete(category) 
        db.session.commit()    

            


@dataclass
class Product(db.Model):
    __tablename__='product'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120))
    price=db.Column(db.Integer)
    oldPrice=db.Column(db.Float)
    description=db.Column(db.String(120))
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))

    def __init__(self,id,name,price,oldPrice,description,category_id,):
        self.id=id
        self.name=name
        self.price=price
        self.oldPrice=oldPrice
        self.description=description
        self.category_id=category_id


    @classmethod
    def get_all_products(cls):
        return cls.query.all()
    
    @classmethod
    def get_product_by_id(cls,id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def add_product(cls,name,price,oldPrice,description,category_id):
        product=cls(cls,name,price,oldPrice,description,category_id)
        db.session.add(product)
        db.session.commit()  
    
    @classmethod
    def update_product(cls,name,price,oldPrice,description,category_id):
        product=cls.query.filter_by(id=id).first()
        product.name=name
        product.price=price
        product.oldPrice=oldPrice
        product.description=description
        product.category_id=category_id
        db.session.commit()
    @classmethod
    def delete_user(cls,id):
        product=cls.query.filter_by(id=id).first()
        db.session.delete(product) 
        db.session.commit()    
        











    
      
