from flask import ( Blueprint, render_template, request, redirect, jsonify ) 
from . import models

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/new')
def new():
    return render_template('reptiles/new.html')


#index route

@bp.route('/', methods=['GET', 'POST']) 
def index(): 
    #GET request handling
    if request.method == 'GET':
        found_reptiles = models.Reptile.query.all()
        reptile_dict = {'reptiles': []}

        for reptile in found_reptiles:
            reptile_dict['reptiles'].append({
                "common_name": reptile.common_name,
                "scientific_name": reptile.scientific_name,
                "conservation_status": reptile.conservation_status,
                "native_habitat":reptile.native_habitat,
                "fun_fact": reptile.fun_fact
            })
        return jsonify(reptile_dict)


#POST REQUESTS
#return to index route - capture an ID
    else:
        data = request.json

        new_reptile = models.Reptile(
            common_name=data['common_name'],
            scientific_name=data['scientific_name'],
            conservation_status=data['conservation_status'],
            native_habitat=data['native_habitat'],
            fun_fact=data['fun_fact'],
        )

        models.db.session.add(new_reptile)
        models.db.session.commit()
        
        return redirect('/reptiles')
        
@bp.route('/<int:reptile_id>')
def show(reptile_id):
    reptile = models.Reptile.query.filter_by(reptile_id=reptile_id).first()

    if reptile is None:
        # Return a response indicating that the reptile was not found
        return jsonify({'error': 'Reptile not found'}), 404

    reptile_dict = {
        'reptile_id': reptile.reptile_id,
        'common_name': reptile.common_name,
        'scientific_name': reptile.scientific_name,
        'conservation_status': reptile.conservation_status,
        'native_habitat': reptile.native_habitat,
        'fun_fact': reptile.fun_fact
    }

    return jsonify(reptile_dict)

# from flask import Blueprint, redirect, request, jsonify
# from . import models

# bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

# @bp.route('/', methods=['GET', 'POST'])
# def index():
#     # GET request handling...
#     if request.method == 'GET':
#         found_reptiles = models.Reptile.query.all()
#         reptile_dict = {'reptiles': []}

#         for reptile in found_reptiles:
#             reptile_dict['reptiles'].append({
#                 'common_name': reptile.common_name,
#                 'scientific_name': reptile.scientific_name,
#                 'conservation_status': reptile.conservation_status,
#                 'native_habitat': reptile.native_habitat,
#                 'fun_fact': reptile.fun_fact
#             })

#         return jsonify(reptile_dict)
    
#     # POST request handling...
#     else:
#         data = request.json
        
#         new_reptile = models.Reptile(
#             common_name=data['common_name'],
#             scientific_name=data['scientific_name'],
#             conservation_status=data['conservation_status'],
#             native_habitat=data['native_habitat'],
#             fun_fact=data['fun_fact'],
#         )

#         models.db.session.add(new_reptile)
#         models.db.session.commit()
        
#         return redirect('/reptiles')
    
# @bp.route('/<int:reptile_id>')
# def show(reptile_id):
#     reptile = models.Reptile.query.filter_by(reptile_id=reptile_id).first()

#     if reptile is None:
#         # Return a response indicating that the reptile was not found
#         return jsonify({'error': 'Reptile not found'}), 404

#     reptile_dict = {
#         'reptile_id': reptile.reptile_id,
#         'common_name': reptile.common_name,
#         'scientific_name': reptile.scientific_name,
#         'conservation_status': reptile.conservation_status,
#         'native_habitat': reptile.native_habitat,
#         'fun_fact': reptile.fun_fact
#     }

#     return jsonify(reptile_dict)


 
