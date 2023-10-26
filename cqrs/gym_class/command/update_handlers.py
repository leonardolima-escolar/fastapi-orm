from cqrs.gym_class.handlers import ICommandHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.gym_class.commands import GymClassCommand
from sqlalchemy.orm import Session


class UpdateGymClassCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)

    async def handle(self, id, command: GymClassCommand) -> bool:
        result = self.repo.update_gym_class(id, command.details)
        return result
