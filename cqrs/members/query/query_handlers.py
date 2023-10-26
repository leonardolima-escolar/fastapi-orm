from cqrs.members.handlers import IQueryHandler
from repository.sqlalchemy.profile_members import ProfileMembersRepository
from cqrs.members.queries import ProfileMemberListQuery, ProfileMemberRecordQuery
from sqlalchemy.orm import Session


class ListMemberQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileMembersRepository = ProfileMembersRepository(sess)
        self.query: ProfileMemberListQuery = ProfileMemberListQuery()

    async def handle(self) -> ProfileMemberListQuery:
        data = self.repo.get_all_profile_members()
        self.query.records = data
        return self.query


class RecordMemberQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: ProfileMembersRepository = ProfileMembersRepository(sess)
        self.query: ProfileMemberRecordQuery = ProfileMemberRecordQuery()

    async def handle(self, id) -> ProfileMemberListQuery:
        data = self.repo.get_profile_members(id)
        self.query.record = data
        return self.query
