from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Profile_Trainers


class ProfileTrainersRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_profile_trainers(self, profile_trainers: Profile_Trainers) -> bool:
        try:
            self.sess.add(profile_trainers)
            self.sess.commit()
        # except Exception as e:
        #     print(e)
        except:
            return False
        return True

    def update_profile_trainers(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).update(
                details
            )
            self.sess.commit()

        except:
            return False
        return True

    def delete_profile_trainers(self, id: int) -> bool:
        try:
            self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_profile_trainers(self):
        return self.sess.query(Profile_Trainers).all()

    def get_profile_trainers(self, id: int):
        return (
            self.sess.query(Profile_Trainers)
            .filter(Profile_Trainers.id == id)
            .one_or_none()
        )
