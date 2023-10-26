from cqrs.members.handlers import ICommandHandler
from repository.sqlalchemy.profile_members import ProfileMembersRepository
from cqrs.members.commands import ProfileMemberCommand
from sqlalchemy.orm import Session


class UpdateMemberCommandHandler(ICommandHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileMembersRepository = ProfileMembersRepository(sess)

    async def handle(self, id, command: ProfileMemberCommand) -> bool:
        result = self.repo.update_profile_members(id, command.details)
        return result
