from app.Database import db, BaseModelMixin


class Users(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(80), nullable=False)
    last_name=db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    rol_id= db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    def __init__(self, firts_name, email, rol_id):
        self.first_name = firts_name
        self.email = email
        self.rol_id = rol_id

    def __repr__(self):
        return f"User{self.email}"

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_id (cls, rol_id):
        return cls.query.filter_by(rol_id=rol_id).all() 