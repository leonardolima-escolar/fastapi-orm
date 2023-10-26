from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Profile_Members


class ProfileMembersRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess

    def insert_profile_members(self, profile_members: Profile_Members) -> bool:
        try:
            self.sess.add(profile_members)
            self.sess.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def update_profile_members(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Profile_Members).filter(Profile_Members.id == id).update(
                details
            )
            self.sess.commit()

        except Exception as e:
            print(e)
            return False
        return True

    def delete_profile_members(self, id: int) -> bool:
        try:
            self.sess.query(Profile_Members).filter(Profile_Members.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    def get_all_profile_members(self):
        return self.sess.query(Profile_Members).all()

    def get_profile_members(self, id: int):
        return (
            self.sess.query(Profile_Members)
            .filter(Profile_Members.id == id)
            .one_or_none()
        )
