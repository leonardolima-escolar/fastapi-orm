from cqrs.attendance.handlers import IQueryHandler
from repository.sqlalchemy.signup import MemberAttendanceRepository
from cqrs.attendance.queries import AttendanceListQuery
from sqlalchemy.orm import Session


class ListAttendanceQueryHandler(IQueryHandler):
    def __init__(self, sess: Session):
        self.repo: MemberAttendanceRepository = MemberAttendanceRepository(sess)
        self.query: AttendanceListQuery = AttendanceListQuery()

    async def handle(self) -> AttendanceListQuery:
        data = self.repo.join_member_attendance()
        self.query.records = data
        return self.query
