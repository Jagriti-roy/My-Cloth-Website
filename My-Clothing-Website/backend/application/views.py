from flask_cors import CORS,cross_origin
from celery.result import AsyncResult
from .tasks import create_service_req_csv
from .decorators import roles_required  # Adjust the import path based on your project structure
from flask import jsonify, request, render_template, send_from_directory,current_app as app
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from .models import *
from .sec import cache
from flask_cors import cross_origin
import os
import uuid
from datetime import datetime

##################################################################################################################################################
###############################################################       Handle 404 errors       ####################################################

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/uploads/<path:filename>')
def serve_uploads(filename):
    return send_from_directory('static/uploads', filename, mimetype='image/jpeg')

@app.route('/api/postUsers', methods=["POST"])
@cross_origin(origins=["http://localhost:5173"])
def postUsers():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    address = data.get('address')
    phone_number = data.get('phone_number')

    new_user = User(
        name=name,
        email=email,
        password=generate_password_hash(password),
        address=address,
        phone_number=phone_number,
    )

    db.session.add(new_user)
    db.session.commit()

    default_role_id = 2
    new_role = RoleUsers(user_id=new_user.id, role_id=default_role_id)
    db.session.add(new_role)
    db.session.commit()

    return jsonify({'success': True, 'message': 'User created successfully!'})

@app.route('/api/getUsers', methods=['GET'])
@roles_required('admin')
@jwt_required()
def getUsers():
    users = User.query.all()
    return jsonify([
        {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'password': user.password,
            'address': user.address,
            'phone_number': user.phone_number,
            'active': user.active,
            'created_at': user.created_at,
        } for user in users
    ])


# @app.route('/api/getUsers',methods=['GET'])
# def getUsers():
#     users = Role.query.filter_by(name ="user").first()
#     users = users.users
#     return jsonify([{
#         'user_id' : p.user_id,
#         'email' : p.email,
#         'password' : p.password,
#         'fullname' : p.fullname,
#         'qualification' : p.qualification,
#         'dob' : p.dob,
#     } for p in users ])

############################################################################################################################################################
######################################################################        SUBJECTS       ###############################################################

# @app.route('/api/getSubjects', methods=['GET'])
# def getSubjects():
#     subjects = Subject.query.all()
#     return jsonify([
#         {
#             'subject_id': p.subject_id,
#             'name': p.name,
#             'description': p.description,
#             'chapters': [
#                 {
#                     'chapter_id': c.chapter_id,
#                     'name': c.name,
#                     'description': c.description
#                 } for c in p.chapters
#             ]
#         } for p in subjects
#     ])

# @app.route('/api/postSubject',methods=["POST"])
# @cross_origin(origins=["http://localhost:5173"])
# @auth_required('token')
# @roles_required("admin")
# def postSubject():
#     data = request.json
#     name = data.get('name')
#     description = data.get('description')
#     new_subject = Subject(name=name,description=description)
#     db.session.add(new_subject)
#     db.session.commit()
#     return jsonify({
#         'success':True,
#         'message':'Subject Added Successfully!'
#     })

# @app.route('/api/editSubject',methods=["POST"])
# @cross_origin(origins=["http://localhost:5173"])
# @auth_required('token')
# @roles_required("admin")
# def editSubject():
#     data = request.json
#     subject_id = data.get('id')
#     edited_name = data.get('name')
#     edited_description = data.get('description')
#     edited_subject = Subject.query.get(subject_id)
#     edited_subject.name = edited_name
#     edited_subject.description = edited_description

#     db.session.commit()

#     return jsonify({
#         'success':True,
#         'message':'Subject Edited Successfully!'
#     })

# @app.route('/api/deleteSubject',methods=['POST'])
# @cross_origin(origins=["http://localhost:5173"])
# @auth_required('token')
# @roles_required("admin")
# def deleteSubject():
#     data = request.json
#     id = data.get('id')
#     subject_to_be_deleted = Subject.query.get(id)
#     for i in subject_to_be_deleted.chapters:
#         to_be_deletedChapter = Chapter.query.get(i.chapter_id)
#         quiz_selected = Quiz.query.filter_by(chapter_id = to_be_deletedChapter.chapter_id).first()
#         if(quiz_selected):
#             return jsonify({
#                 'success':True,
#                 'message':to_be_deletedChapter.name+' chapter of the subject '+subject_to_be_deleted.name+' is in the Quiz '+str(quiz_selected.quiz_id)
#             })
#         db.session.delete(to_be_deletedChapter)
#     db.session.delete(subject_to_be_deleted)
#     db.session.commit()
#     return jsonify({
#         'success':True,
#         'message':'Subject Deleted Successfully!'
#     })


# @roles_required('admin')
# @jwt_required()
############################################################################################################################################################
######################################################################        CHAPTERS       ###############################################################


############################################################################################################################################################
######################################################################        QUIZZES       ###############################################################

############################################################################################################################################################
######################################################################        QUESTIONS       ##################################################################


############################################################################################################################################################
######################################################################        SCORES       ##################################################################

############################################################################################################################################################
######################################################################        ADMIN       ##################################################################


@app.route("/api/authenticate", methods=["POST"])
def login_func():
    credentials = request.get_json()
    email = credentials.get("email")
    password = credentials.get("password")
    
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity={'id': user.id, 'email': user.email, 'roles': [role.name for role in user.roles]})
        return jsonify({'access_token': access_token, 'role': [role.name for role in user.roles]}), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/api/logout', methods=['POST'])
def logout():
    return jsonify({'message': 'Logged out successfully!'}), 200