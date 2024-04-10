from application import db,app
from flask import Blueprint,flash,request,url_for,render_template,redirect
from flask_login import login_required, current_user
from application.forms.inventory_form import InventoryForm
from application.models.inventory import Inventory

inventory = Blueprint('inventory',__name__, template_folder='templates')

@inventory.route('/admin/dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    form = InventoryForm()
    if form.validate_on_submit():
        inventory = Inventory(title=form.title.data)
        db.session.add(inventory)
        db.session.commit()
        flash('Inventory added successfully!', 'success')
        return redirect(url_for('inventory.admin_dashboard'))
    inventories = Inventory.query.all()
    return render_template('admin/inventories.html', form=form, inventories=inventories)


@inventory.route('/delete_inventory/<int:inventory_id>', methods=['POST'])
@login_required
def delete_inventory(inventory_id):
    inventory = Inventory.query.get_or_404(inventory_id)
    db.session.delete(inventory)
    db.session.commit()
    flash('Inventory deleted successfully!', 'success')
    return redirect(url_for('inventory.admin_dashboard'))
