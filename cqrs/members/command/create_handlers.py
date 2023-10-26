from cqrs.members.handlers import ICommandHandler
from repository.sqlalchemy.profile_members import ProfileMembersRepository
from cqrs.members.commands import ProfileMemberCommand
from sqlalchemy.orm import Session


class AddMemberCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileMembersRepository = ProfileMembersRepository(sess)

    async def handle(self, command: ProfileMemberCommand) -> bool:
        result = self.repo.insert_profile_members(command.details)
        return result
