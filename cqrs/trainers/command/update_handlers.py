from cqrs.trainers.handlers import ICommandHandler
from repository.sqlalchemy.profile_trainers import ProfileTrainersRepository
from cqrs.trainers.commands import ProfileTrainerCommand
from sqlalchemy.orm import Session


class UpdateTrainerCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileTrainersRepository = ProfileTrainersRepository(sess)

    async def handle(self, id, command: ProfileTrainerCommand) -> bool:
        result = self.repo.update_profile_trainers(id, command.details)
        return result
