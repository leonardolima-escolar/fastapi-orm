from cqrs.signup.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.signup.commands import SignupCommand
from sqlalchemy.orm import Session


class DeleteSignupCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)

    async def handle(self, command: SignupCommand) -> bool:
        result = self.repo.delete_signup(command.details.get("id"))
        return result
