from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm, AddItemForm, AddFundsForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    search_query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    sort = request.args.get('sort', 'id')
    if request.method == "POST":
        #Purchase Item Logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')
        #Sell Item Logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congratulations! You sold {s_item_object.name} back to market!", category='success')
            else:
                flash(f"Something went wrong with selling {s_item_object.name}", category='danger')


        return redirect(url_for('market_page'))

    if request.method == "GET":
        base_q = Item.query.filter(Item.owner == None)
        if search_query:
            base_q = base_q.filter(Item.name.ilike(f"%{search_query}%"))

        # sorting
        if sort == 'price_asc':
            order = Item.price.asc()
        elif sort == 'price_desc':
            order = Item.price.desc()
        elif sort == 'name':
            order = Item.name.asc()
        else:
            order = Item.id.asc()

        pagination = base_q.order_by(order).paginate(page=page, per_page=8, error_out=False)
        items = pagination.items
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form, search_query=search_query, pagination=pagination, sort=sort)


@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item_page():
    form = AddItemForm()
    if form.validate_on_submit():
        try:
            price_val = int(form.price.data)
        except ValueError:
            flash('Price must be a whole number', category='danger')
            return render_template('add_item.html', form=form)

        # create item and assign ownership to creator
        new_item = Item(name=form.name.data, price=price_val, barcode=form.barcode.data, description=form.description.data, owner=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        flash(f'Item {new_item.name} added to market!', category='success')
        return redirect(url_for('market_page'))
    return render_template('add_item.html', form=form)


@app.route('/item/<int:item_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_item(item_id):
    item = Item.query.get_or_404(item_id)
    if item.owner is None or item.owner != current_user.id:
        flash('You can only edit items you own.', category='danger')
        return redirect(url_for('market_page'))
    form = AddItemForm()
    if request.method == 'GET':
        form.name.data = item.name
        form.price.data = str(item.price)
        form.barcode.data = item.barcode
        form.description.data = item.description
        return render_template('edit_item.html', form=form, item=item)
    if form.validate_on_submit():
        try:
            item.price = int(form.price.data)
        except ValueError:
            flash('Price must be a whole number', category='danger')
            return render_template('edit_item.html', form=form, item=item)
        item.name = form.name.data
        item.barcode = form.barcode.data
        item.description = form.description.data
        db.session.commit()
        flash('Item updated.', category='success')
        return redirect(url_for('profile_page'))


@app.route('/item/<int:item_id>/delete', methods=['POST'])
@login_required
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    if item.owner is None or item.owner != current_user.id:
        flash('You can only delete items you own.', category='danger')
        return redirect(url_for('market_page'))
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted.', category='info')
    return redirect(url_for('profile_page'))


@app.route('/add_funds', methods=['GET', 'POST'])
@login_required
def add_funds_page():
    form = AddFundsForm()
    if form.validate_on_submit():
        try:
            amt = int(form.amount.data)
        except ValueError:
            flash('Amount must be a whole number', category='danger')
            return render_template('add_funds.html', form=form)
        current_user.budget += amt
        db.session.commit()
        flash(f'Added {amt}$ to your account.', category='success')
        return redirect(url_for('profile_page'))
    return render_template('add_funds.html', form=form)


@app.route('/profile')
@login_required
def profile_page():
    owned_items = Item.query.filter_by(owner=current_user.id)
    return render_template('profile.html', owned_items=owned_items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))










