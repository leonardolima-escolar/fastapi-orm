from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.login.commands import LoginCommand
from sqlalchemy.orm import Session


class AddLoginCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)

    async def handle(self, command: LoginCommand) -> bool:
        result = self.repo.insert_login(command.details)
        return result
