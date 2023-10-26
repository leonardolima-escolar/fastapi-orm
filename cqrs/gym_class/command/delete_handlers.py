from cqrs.gym_class.handlers import ICommandHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.gym_class.commands import GymClassCommand
from sqlalchemy.orm import Session


class DeleteGymClassCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)

    async def handle(self, command: GymClassCommand) -> bool:
        result = self.repo.delete_gym_class(command.details.get("id"))
        return result
