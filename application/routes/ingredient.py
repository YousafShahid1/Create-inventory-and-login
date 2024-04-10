from application import app,db
from flask import Blueprint,render_template,flash,request,url_for,redirect
from flask_login import login_required, current_user
from application.forms.ingredient_form import IngredientForm
from application.models.ingredient import Ingredient
from application.models.inventory import Inventory



ingredient = Blueprint('ingredient',__name__, template_folder='templates')

@ingredient.route('/ingredients/<int:inventory_id>', methods=['GET', 'POST'])
@login_required
def ingredients(inventory_id):
    form = IngredientForm()
    if form.validate_on_submit():
        
        ingredient = Ingredient(title=form.title.data, description=form.description.data, inventory_id=inventory_id)
        db.session.add(ingredient)
        db.session.commit()
        flash('Ingredient added successfully!', 'success')
        return redirect(url_for('ingredient.ingredients',inventory_id=inventory_id))
    
    ingredients = Ingredient.query.filter_by(inventory_id=inventory_id).all()
    return render_template('admin/ingredients.html', form=form,  ingredients=ingredients,inventory_id=inventory_id)


@ingredient.route('/delete_ingredient/<int:ingredient_id>', methods=['POST'])
@login_required
def delete_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    db.session.delete(ingredient)
    db.session.commit()
    flash('Ingredient deleted successfully!', 'success')
    return redirect(url_for('ingredient.ingredients',inventory_id=ingredient.inventory_id))