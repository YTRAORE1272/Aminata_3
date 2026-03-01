from flask import Blueprint, render_template, request, redirect, url_for
from app.data.Data import Data
from app.services.teacher_service import TeacherService

# --- Création du "Blueprint" ---

teachers_bp = Blueprint('teachers', __name__, url_prefix='/teachers')

service = TeacherService(Data)




@teachers_bp.route('/')
def index():
    return "Teachers Index Page"


@teachers_bp.route('/liste')
def liste():
    
    teachers = service.list_teachers()

    return render_template('base.html', teachers=teachers)


# --- AJOUTER un professeur ---

@teachers_bp.route('/add', methods=['GET', 'POST'])

def add():
    
    if request.method == 'POST':
  
        name      = request.form.get('name')   
        email     = request.form.get('email')       
        speciality = request.form.get('speciality') 

        service.add_teacher(name, email, speciality)

        return redirect(url_for('teachers.liste'))

    return render_template('add_teacher.html')


# --- SUPPRIMER un professeur ---

@teachers_bp.route('/delete/<int:teacher_id>')
def delete(teacher_id):
    service.delete_teacher(teacher_id)

    return redirect(url_for('teachers.liste'))