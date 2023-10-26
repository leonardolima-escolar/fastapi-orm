from cqrs.trainers.handlers import ICommandHandler
from repository.sqlalchemy.profile_trainers import ProfileTrainersRepository
from cqrs.trainers.commands import ProfileTrainerCommand
from sqlalchemy.orm import Session


class AddTrainerCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileTrainersRepository = ProfileTrainersRepository(sess)

    async def handle(self, command: ProfileTrainerCommand) -> bool:
        result = self.repo.insert_profile_trainers(command.details)
        return result
