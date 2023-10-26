from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.login.commands import LoginCommand
from sqlalchemy.orm import Session


class UpdateLoginCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)

    async def handle(self, id, command: LoginCommand) -> bool:
        result = self.repo.update_login(id, command.details)
        return result
