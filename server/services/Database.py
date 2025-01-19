"""
"""

# IMPORTS

from models.Classroom import Classroom
from models.ClassroomStudents import classroom_students
from models.Lecture import Lecture
from models.Play import Play
from models.Playbook import Playbook
from models.PlayAnswer import PlayAnswer
from models.User import User

from exceptions import InvalidEmailAddress, EmailAddressAlreadyInUse, ClassroomNotFound, UserNotFound, Unauthorized, PlaybookNotFound, PlayNotFound, LectureNotFound

# DATABASE CLASS
class Database:
    """
    """
    def __init__(self, db):
        """
        """
        self.db = db

    # USER METHODS
    def get_user_by_id(self, user_id):
        """
        """
        user = self.db.session.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound()
        return user
    
    def get_user_by_email(self, email):
        """
        """
        user = self.db.session.query(User).filter(User.email == email).first()
        if not user:
            raise InvalidEmailAddress()
        return user
    
    def create_user(self, username, email, password):
        """
        """
        if self.db.session.query(User).filter(User.email == email).first():
            raise EmailAddressAlreadyInUse()
        # TODO: Implement email verification with one time code + email service.
        user = User(username=username, email=email, password=password, verification_code=None, reset_code=None, is_verified=True)
        self.db.session.add(user)
        self.db.session.commit()
        return user
    
    # CLASSROOM METHODS
    def get_student_classrooms(self, student_id):
        """
        """
        classrooms = self.db.session.query(Classroom).join(classroom_students).filter(classroom_students.c.student_id == student_id).all()
        return classrooms
    
    def get_teacher_classrooms(self, teacher_id):
        """
        """
        classrooms = self.db.session.query(Classroom).filter(Classroom.teacher_id == teacher_id).all()
        return classrooms
    
    def create_classroom(self, name, teacher_id, image_url, join_code):
        """
        """
        classroom = Classroom(name=name, image_url=image_url, join_code=join_code, teacher_id=teacher_id)
        self.db.session.add(classroom)
        self.db.session.commit()
        return classroom
    
    def get_classroom_by_join_code(self, join_code):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.join_code == join_code).first()
        if not classroom:
            raise ClassroomNotFound()
        return classroom
    
    def add_student_to_classroom(self, student_id, classroom_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        student = self.db.session.query(User).filter(User.id == student_id).first()
        if not student:
            raise UserNotFound()
        if student in classroom.students or student.id == classroom.teacher_id:
            raise Unauthorized()
        classroom.students.append(student)
        self.db.session.commit()
        return classroom
    
    def get_classroom_by_id(self, classroom_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        return classroom
    
    def delete_classroom(self, classroom_id, teacher_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if classroom.teacher_id != teacher_id:
            raise Unauthorized()
        self.db.session.delete(classroom)
        self.db.session.commit()
        return classroom
    
    def leave_classroom(self, student_id, classroom_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        student = self.db.session.query(User).filter(User.id == student_id).first()
        if not student:
            raise UserNotFound()
        if student not in classroom.students:
            raise Unauthorized()
        classroom.students.remove(student)
        self.db.session.commit()
        return classroom
    
    # PLAYBOOK METHODS
    def get_playbooks(self, teacher_id):
        """
        """
        playbooks = self.db.session.query(Playbook).filter(Playbook.teacher_id == teacher_id).all()
        return playbooks
    
    def create_playbook(self, name, description, teacher_id, image_url):
        """
        """
        playbook = Playbook(name=name, description=description, teacher_id=teacher_id, image_url=image_url)
        self.db.session.add(playbook)
        self.db.session.commit()
        return playbook
    
    def get_playbook_by_id(self, playbook_id, teacher_id):
        """
        """
        playbook = self.db.session.query(Playbook).filter(Playbook.id == playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        if playbook.teacher_id != teacher_id:
            raise Unauthorized()
        return playbook
    
    def delete_playbook(self, playbook_id, teacher_id):
        """
        """
        playbook = self.db.session.query(Playbook).filter(Playbook.id == playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        if playbook.teacher_id != teacher_id:
            raise Unauthorized()
        self.db.session.delete(playbook)
        self.db.session.commit()
        return playbook
    
    def get_plays(self, playbook_id, teacher_id):
        """
        """
        playbook = self.db.session.query(Playbook).filter(Playbook.id == playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        if playbook.teacher_id != teacher_id:
            raise Unauthorized()
        plays = playbook.plays
        return plays
    
    # PLAY METHODS
    def create_play(self, teacher_id, playbook_id, play_type, play_prompt, play_answer): 
        """
        """
        playbook = self.db.session.query(Playbook).filter(Playbook.id == playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        if playbook.teacher_id != teacher_id:
            raise Unauthorized()
        play = Play(play_type=play_type, play_prompt=play_prompt, play_answer=play_answer, playbook_id=playbook_id)
        self.db.session.add(play)
        self.db.session.commit()
        return play
    
    def delete_play(self, play_id, teacher_id):
        """
        """
        play = self.db.session.query(Play).filter(Play.id == play_id).first()
        if not play:
            raise PlayNotFound()
        playbook = self.db.session.query(Playbook).filter(Playbook.id == play.playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        if playbook.teacher_id != teacher_id:
            raise Unauthorized()
        self.db.session.delete(play)
        self.db.session.commit()
        return play

    def get_play(self, play_id, teacher_id):
        """
        """
        play = self.db.session.query(Play).filter(Play.id == play_id).first()
        if not play:
            raise PlayNotFound()
        playbook = self.db.session.query(Playbook).filter(Playbook.id == play.playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        if playbook.teacher_id != teacher_id:
            raise Unauthorized()
        return play
    
    def update_play(self, play_id, teacher_id, play_type, play_prompt, play_answer):
        """
        """
        play = self.db.session.query(Play).filter(Play.id == play_id).first()
        if not play:
            raise PlayNotFound()
        playbook = self.db.session.query(Playbook).filter(Playbook.id == play.playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        if playbook.teacher_id != teacher_id:
            raise Unauthorized()
        play.play_type = play_type
        play.play_prompt = play_prompt
        play.play_answer = play_answer
        self.db.session.commit()
        return play
    
    # LECTURE METHODS
    def get_lectures(self, classroom_id, user_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if classroom.teacher_id != user_id or user_id not in [student.id for student in classroom.students]:
            raise Unauthorized()
        lectures = classroom.lectures
        return lectures
    
    def create_lecture(self, name, description, user_id, image_url, classroom_id, playbook_id):
        """
        """
        classroom = self.db.session.query(Classroom).filter(Classroom.id == classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if classroom.teacher_id != user_id:
            raise Unauthorized()
        playbook = self.db.session.query(Playbook).filter(Playbook.id == playbook_id).first()
        if not playbook:
            raise PlaybookNotFound()
        lecture = Lecture(name=name, description=description, image_url=image_url, is_active=True, classroom_id=classroom_id, playbook_id=playbook_id)
        self.db.session.add(lecture)
        self.db.session.commit()
        return lecture
    
    def get_lecture(self, lecture_id, user_id):
        """
        """
        lecture = self.db.session.query(Lecture).filter(Lecture.id == lecture_id).first()
        if not lecture:
            raise LectureNotFound()
        classroom = self.db.session.query(Classroom).filter(Classroom.id == lecture.classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if classroom.teacher_id != user_id or user_id not in [student.id for student in classroom.students]:
            raise Unauthorized()
        return lecture
    
    def set_inactive(self, lecture_id, teacher_id):
        """
        """
        lecture = self.db.session.query(Lecture).filter(Lecture.id == lecture_id).first()
        if not lecture:
            raise LectureNotFound()
        classroom = self.db.session.query(Classroom).filter(Classroom.id == lecture.classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if classroom.teacher_id != teacher_id:
            raise Unauthorized()
        lecture.is_active = False
        self.db.session.commit()
        return lecture
    
    # PLAY ANSWER METHODS
    def create_play_answer(self, play_id, user_id, lecture_id, answer):
        """
        """
        play = self.db.session.query(Play).filter(Play.id == play_id).first()
        if not play:
            raise PlayNotFound()
        lecture = self.db.session.query(Lecture).filter(Lecture.id == lecture_id).first()
        if not lecture:
            raise LectureNotFound()
        classroom = self.db.session.query(Classroom).filter(Classroom.id == lecture.classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if user_id not in [student.id for student in classroom.students]:
            raise Unauthorized()
        play_answer = PlayAnswer(answer=answer, play_id=play_id, user_id=user_id)
        self.db.session.add(play_answer)
        self.db.session.commit()
        return play_answer
    
    def get_play_answers(self, play_id, user_id):
        """
        """
        play = self.db.session.query(Play).filter(Play.id == play_id).first()
        if not play:
            raise PlayNotFound()
        lecture = self.db.session.query(Lecture).filter(Lecture.id == play.playbook_id).first()
        if not lecture:
            raise LectureNotFound()
        classroom = self.db.session.query(Classroom).filter(Classroom.id == lecture.classroom_id).first()
        if not classroom:
            raise ClassroomNotFound()
        if user_id not in [student.id for student in classroom.students]:
            raise Unauthorized()
        play_answers = play.answers
        return play_answers