class Data:
    students = [
        {"id": 1, "name": "Karim Ouédraogo", "email": "karim@edu.com"},
        {"id": 2, "name": "Fatou Ndiaye",     "email": "fatou@edu.com"},
        {"id": 3, "name": "Ibrahima Sow",     "email": "ibrahima@edu.com"},
    ]

    teachers = [
        {"id": 1, "name": "Dr. Dieng",    "email": "dieng@edu.com",    "speciality": "Algèbre"},
        {"id": 2, "name": "Prof. Coulibaly", "email": "coulibaly@edu.com", "speciality": "Intelligence Artificielle"},
        {"id": 3, "name": "Dr. Sylla",    "email": "sylla@edu.com",    "speciality": "Chimie"},
    ]

    courses = [
        {"id": 1, "title": "Structures de données",  "teacher_id": 2, "student_ids": [1, 2]},
        {"id": 2, "title": "Algèbre linéaire",        "teacher_id": 1, "student_ids": [2, 3]},
        {"id": 3, "title": "Sécurité informatique",   "teacher_id": 2, "student_ids": [1, 3]},
    ]

    next_student_id = 4
    next_teacher_id = 4
    next_course_id  = 4