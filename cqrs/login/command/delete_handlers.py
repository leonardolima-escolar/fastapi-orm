from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.login.commands import LoginCommand
from sqlalchemy.orm import Session


class DeleteLoginCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)

    async def handle(self, command: LoginCommand) -> bool:
        result = self.repo.delete_login(command.details.get("id"))
        return result
