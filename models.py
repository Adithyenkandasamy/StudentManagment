import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Database Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    details = db.relationship('StudentDetail', backref='user', uselist=False)

class StudentDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    blood_group = db.Column(db.String(5), nullable=False)
    father_name = db.Column(db.String(150), nullable=False)
    mother_name = db.Column(db.String(150), nullable=False)
    emergency_contact = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    course = db.Column(db.String(100), nullable=False)
    have_own_laptop = db.Column(db.Boolean, nullable=False, default=False)
    profile_picture = db.Column(db.String(150), nullable=False)
    github_link = db.Column(db.String(150), nullable=False)
    linkedin_link = db.Column(db.String(150), nullable=False)
    insta_link = db.Column(db.String(150), nullable=False)




class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

class VideoLinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_title= db.Column(db.String(100), nullable=False)
    videolink= db.Column(db.String(100), nullable=False)


class CourseVideos(db.Model):
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video_links.id'), primary_key=True)


class CourseRoadmap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)


class StudentEducation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    degree= db.Column(db.String(100), nullable=False)
    university = db.Column(db.String(100), nullable=False)
    passing_year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

class StudentProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)
    deployed_url = db.Column(db.String(100), nullable=False)
    git_link = db.Column(db.String(100), nullable=False)
    
class StudentProjectSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('student_project.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class StudentSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'), nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    logout_time = db.Column(db.DateTime, nullable=True)
    lunch_start_time = db.Column(db.DateTime, nullable=True)
    lunch_end_time = db.Column(db.DateTime, nullable=True)
    work_summary = db.Column(db.Text, nullable=True)
    

    def __init__(self, user_id, work_summary=None):
        self.user_id = user_id
        self.work_summary = work_summary