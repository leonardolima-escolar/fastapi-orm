from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Gym_Class


class GymClassRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_gym_class(self, gym_class: Gym_Class) -> bool:
        try:
            self.sess.add(gym_class)
            self.sess.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def update_gym_class(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Gym_Class).filter(Gym_Class.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    def delete_gym_class(self, id: int) -> bool:
        try:
            self.sess.query(Gym_Class).filter(Gym_Class.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_gym_class(self):
        return self.sess.query(Gym_Class).all()

    def get_gym_class(self, id: int):
        return self.sess.query(Gym_Class).filter(Gym_Class.id == id).one_or_none()
