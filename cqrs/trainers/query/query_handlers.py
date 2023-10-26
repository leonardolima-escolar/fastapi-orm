from cqrs.trainers.handlers import IQueryHandler
from repository.sqlalchemy.profile_trainers import ProfileTrainersRepository
from cqrs.trainers.queries import ProfileTrainerListQuery, ProfileTrainerRecordQuery
from sqlalchemy.orm import Session


class ListTrainerQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileTrainersRepository = ProfileTrainersRepository(sess)
        self.query: ProfileTrainerListQuery = ProfileTrainerListQuery()

    async def handle(self) -> ProfileTrainerListQuery:
        data = self.repo.get_all_profile_trainers()
        self.query.records = data
        return self.query


class RecordTrainerQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileTrainersRepository = ProfileTrainersRepository(sess)
        self.query: ProfileTrainerRecordQuery = ProfileTrainerRecordQuery()

    async def handle(self, id) -> ProfileTrainerListQuery:
        data = self.repo.get_profile_trainers(id)
        self.query.record = data
        return self.query
