from flask import Flask, render_template, request, redirect, url_for
from models import db, Sneaker # Importing the models
from flask import jsonify, request
# from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/sneakers.db'

db.init_app(app)  # Initialize the db with the app

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    sort_by = request.args.get('sort', 'name', type=str)  # 'name' is the default now
    direction = request.args.get('direction', 'asc', type=str)  # 'asc' for ascending
    per_page = 8

    if direction == 'asc':
        sneakers = Sneaker.query.order_by(getattr(Sneaker, sort_by).asc()).paginate(page=page, per_page=per_page)
    else:
        sneakers = Sneaker.query.order_by(getattr(Sneaker, sort_by).desc()).paginate(page=page, per_page=per_page)

    total_sneakers = db.session.query(Sneaker).count()

    return render_template('index.html', sneakers=sneakers, total_sneakers=total_sneakers)

@app.route('/add', methods=['GET', 'POST'])
def add_sneaker():
    if request.method == 'POST':
        name = request.form['name']
        sku = request.form['sku']
        # main_color = request.form['main_color']
        brand = request.form['brand']
        model = request.form['model']
        size = int(request.form['size'])  # Convert the form input to integer
        image = request.form['image']
        condition = request.form['condition']
        location = request.form['location']
        description = request.form['description']

        # Check for existing sneaker based on name and sku
        existing_sneaker = Sneaker.query.filter_by(name=name, sku=sku).first()
        if existing_sneaker:
            return "Sneaker already exists", 400

        new_sneaker = Sneaker(name=name, sku=sku, brand=brand, model=model, size=size, image=image, condition=condition, location=location, description=description)
        db.session.add(new_sneaker)
        db.session.commit()
        
        return redirect('/')

    return render_template('add_sneaker.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_sneaker(id):
    sneaker = Sneaker.query.get(id)

    if request.method == 'POST':
        sneaker.name = request.form['name']
        sneaker.sku = request.form['sku']
        # sneaker.main_color = request.form['main_color']
        sneaker.brand = request.form['brand']
        sneaker.model = request.form['model']
        sneaker.size = int(request.form['size'])  # Convert the form input to integer
        sneaker.image = request.form['image']
        sneaker.condition = request.form['condition']
        sneaker.location = request.form['location']
        sneaker.description = request.form['description']  # Include the description field

        db.session.commit()
        return redirect('/')

    return render_template('edit_sneaker.html', sneaker=sneaker)

@app.route('/sneaker/<int:id>', methods=['GET'])
def sneaker_details(id):
    sneaker = Sneaker.query.get_or_404(id)  # Replace with your actual query
    return render_template('sneaker_details.html', sneaker=sneaker)

@app.route('/search_sneaker', methods=['POST'])
def search_sneaker():
    query = request.form.get('query').strip()
    # Use ilike for partial, case-insensitive name matching and == for exact SKU matching
    sneakers = Sneaker.query.filter((Sneaker.name.ilike(f"%{query}%")) | (Sneaker.sku == query)).all()

    if len(sneakers) == 1:
        return redirect(url_for('sneaker_details', id=sneakers[0].id))
    elif len(sneakers) > 1:
        return render_template('search_results.html', sneakers=sneakers)
    else:
        return "Not in database", 404
    
from sqlalchemy import or_

@app.route('/jordan1s', methods=['GET'])
def jordan1s():
    # Relaxing query to be case-insensitive and to allow partial matches
    jordan1s = Sneaker.query.filter(or_(
        Sneaker.model.ilike('%jordan 1 retro%'),
        Sneaker.model.ilike('%aj1 retro%')
    )).all()

    return render_template('jordan1s.html', jordan1s=jordan1s)

from collections import defaultdict
from sqlalchemy import func

@app.route('/data_artistry')
def data_artistry():
    brands = db.session.query(Sneaker.brand, func.count(Sneaker.brand)).group_by(Sneaker.brand).all()
    model_counts = db.session.query(Sneaker.model, func.count(Sneaker.model)).group_by(Sneaker.model).all()

    # New query to get all sneakers
    all_sneakers = Sneaker.query.all()

    aggregated_models = defaultdict(int)

    for model, count in model_counts:
        if model.startswith("Jordan 1 Retro"):
            aggregated_models["Jordan 1 Retro"] += count
        elif model.startswith("Jordan 2 Retro"):
            aggregated_models["Jordan 2 Retro"] += count
        elif model.startswith("Jordan 3 Retro"):
            aggregated_models["Jordan 3 Retro"] += count
        elif model.startswith("Jordan 4 Retro"):
            aggregated_models["Jordan 4 Retro"] += count
        elif model.startswith("Jordan 5 Retro"):
            aggregated_models["Jordan 5 Retro"] += count
        elif model.startswith("Jordan 6 Retro"):
            aggregated_models["Jordan 6 Retro"] += count
        elif model.startswith("Jordan 7 Retro"):
            aggregated_models["Jordan 7 Retro"] += count
        elif model.startswith("Jordan 8 Retro"):
            aggregated_models["Jordan 8 Retro"] += count
        elif model.startswith("Jordan 9 Retro"):
            aggregated_models["Jordan 9 Retro"] += count
        elif model.startswith("Jordan 10 Retro"):
            aggregated_models["Jordan 10 Retro"] += count
        elif model.startswith("Jordan 11 Retro"):
            aggregated_models["Jordan 11 Retro"] += count
        elif model.startswith("Jordan 12 Retro"):
            aggregated_models["Jordan 12 Retro"] += count
        elif model.startswith("Jordan 13 Retro"):
            aggregated_models["Jordan 13 Retro"] += count
        elif model.startswith("Nike Air Max 1"):
            aggregated_models["Nike Air Max 1"] += count
        # Add more conditions here for other model groupings
        else:
            aggregated_models[model] += count

    models = [(model, count) for model, count in aggregated_models.items()]

    return render_template('data_artistry.html', brands=brands, models=models, sneakers=all_sneakers)


@app.route('/api/add_sneaker', methods=['POST'])
def api_add_sneaker():
    data = request.get_json()
    name = data.get('name')
    sku = data.get('sku')
    brand = data.get('brand') 
    model = data.get('model')
    size = data.get('size')
    image = data.get('image')
    condition = data.get('condition')
    location = data.get('location')
    description = data.get('description')
    
    # Check if the sneaker already exists based on name and sku
    existing_sneaker = Sneaker.query.filter_by(name=name, sku=sku).first()
    if existing_sneaker:
        return jsonify({"message": "Sneaker already exists"}), 400

    new_sneaker = Sneaker(name=name, sku=sku, brand=brand, model=model, size=size, image=image, condition=condition, location=location, description=description)
    db.session.add(new_sneaker)
    db.session.commit()

    return jsonify({"message": "Sneaker added successfully", "id": new_sneaker.id}), 201

from flask import jsonify

@app.route('/get_sneakers/<int:page>', methods=['GET'])
def get_sneakers(page):
    sneakers = Sneaker.query.paginate(page, per_page=12, error_out=False)
    sneaker_list = [s.as_dict() for s in sneakers.items]  # Assuming you have an `as_dict` method in your Sneaker model
    return jsonify(sneaker_list)

from flask import Flask, jsonify
from models import db, Sneaker  # Replace 'your_models_file' with the actual file name

@app.route('/fetch/<int:page>', methods=['GET'])
def fetch(page):
    per_page = 8  # Number of items per page, adjust as needed
    pagination = Sneaker.query.paginate(page, per_page, False)
    items = pagination.items
    data = [item.as_dict() for item in items]
    return jsonify(data)



with app.app_context():
    if not os.path.exists('/data/sneakers.db'):
        db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
