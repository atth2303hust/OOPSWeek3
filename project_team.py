"""
/****************/
Họ và tên: Phạm Anh Tú
MSSV; 202419007
/****************/

Lớp ProjectTeam quản lý trưởng nhóm và danh sách thành viên bằng các tham chiếu đối tượng.
"""

from employee import Employee


class ProjectTeam:
    """Biểu diễn một nhóm dự án."""

    def __init__(
        self,
        project_code: str,
        project_name: str,
        leader: Employee | None = None,
    ) -> None:
        """
        Mô phỏng hai constructor:
        - ProjectTeam(projectCode, projectName)
        - ProjectTeam(projectCode, projectName, leader)
        """
        self._projectCode = project_code
        self._projectName = project_name
        self._leader: Employee | None = None
        # Danh sách chỉ lưu tham chiếu đến Employee/SoftwareEngineer có sẵn.
        self._members: list[Employee] = []

        if leader is not None:
            self.addMember(leader, True)

    @property
    def projectCode(self) -> str:
        """Getter cho mã dự án."""
        return self._projectCode

    @property
    def projectName(self) -> str:
        """Getter cho tên dự án."""
        return self._projectName

    @property
    def leader(self) -> Employee | None:
        """Getter cho trưởng nhóm hiện tại."""
        return self._leader

    @property
    def members(self) -> tuple[Employee, ...]:
        """Trả về tuple để mã ngoài không sửa trực tiếp danh sách thành viên."""
        return tuple(self._members)

    def _find_member(self, employee_id: str) -> Employee | None:
        """Tìm đúng đối tượng thành viên theo mã; trả về None nếu không có."""
        return next((member for member in self._members if member.id == employee_id), None)

    def contains(self, employeeId: str) -> bool:
        """Kiểm tra nhóm đã có nhân sự mang mã employeeId hay chưa."""
        return self._find_member(employeeId) is not None

    def addMember(self, employee: Employee, makeLeader: bool = False) -> bool:
        """
        Mô phỏng hai phiên bản addMember():
        - addMember(employee)
        - addMember(employee, makeLeader)
        """
        if not isinstance(employee, Employee):
            raise TypeError("employee phải là một Employee hoặc lớp dẫn xuất.")

        existing_member = self._find_member(employee.id)
        if existing_member is None:
            self._members.append(employee)
            member_in_team = employee
            was_added = True
        else:
            # Không thêm đối tượng thứ hai nếu trùng mã nhân sự.
            member_in_team = existing_member
            was_added = False

        # Leader luôn là chính một đối tượng đang nằm trong danh sách members.
        if makeLeader:
            self._leader = member_in_team
            return True

        return was_added

    def changeLeader(self, employee: Employee) -> bool:
        """Đổi trưởng nhóm; tự thêm nhân sự nếu người đó chưa là thành viên."""
        if not isinstance(employee, Employee):
            raise TypeError("employee phải là một Employee hoặc lớp dẫn xuất.")

        existing_member = self._find_member(employee.id)
        if existing_member is None:
            self._members.append(employee)
            existing_member = employee
        self._leader = existing_member
        return True

    def removeMember(self, employeeId: str) -> bool:
        """Xóa thành viên, nhưng từ chối nếu đó là trưởng nhóm hiện tại."""
        if self._leader is not None and self._leader.id == employeeId:
            return False

        for index, member in enumerate(self._members):
            if member.id == employeeId:
                del self._members[index]
                return True
        return False

    def calculateTotalMonthlyCost(self) -> float:
        """Tính tổng chi phí bằng lời gọi đa hình calculateMonthlyCost()."""
        return sum(member.calculateMonthlyCost() for member in self._members)

    def displayTeam(self) -> str:
        """Hiển thị nhóm và gọi đa hình displayInfo() của từng thành viên."""
        leader_text = (
            f"{self._leader.id} - {self._leader.fullName}"
            if self._leader is not None
            else "Chưa có"
        )
        lines = [
            f"ProjectTeam(code={self._projectCode}, name={self._projectName})",
            f"Leader: {leader_text}",
            "Members:",
        ]
        if not self._members:
            lines.append("  (trống)")
        else:
            for member in self._members:
                lines.append(f"  - {member.displayInfo()}")
        return "\n".join(lines)

    def __del__(self) -> None:
        """Chỉ xóa cấu trúc danh sách nội bộ; không gọi del trên Employee."""
        try:
            print(f"[Destructor] ProjectTeam {self._projectCode} được hủy.")
            self._members.clear()
            self._leader = None
        except Exception:
            pass
