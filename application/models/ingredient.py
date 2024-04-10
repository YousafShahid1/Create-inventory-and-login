from application import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
