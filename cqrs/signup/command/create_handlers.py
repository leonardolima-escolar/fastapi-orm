from cqrs.signup.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.signup.commands import SignupCommand
from sqlalchemy.orm import Session


class AddSignupCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)

    async def handle(self, command: SignupCommand) -> bool:
        result = self.repo.insert_signup(command.details)
        return result
