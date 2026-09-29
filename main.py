"Họ và tên: Phạm Anh Tú"
"MSSV: 202419007"

import gc

from employee import Employee
from project_team import ProjectTeam
from software_engineer import SoftwareEngineer


def print_step(number: int, text: str) -> None:
    """In tiêu đề cho từng bước kiểm thử."""
    print(f"\n[{number:02d}] {text}")


def test_second_team(shared_employee: Employee) -> None:
    """Tạo nhóm thứ hai trong phạm vi hàm để mô phỏng khối lệnh cục bộ."""
    print_step(13, "Tạo nhóm thứ hai và thêm nhân sự đã có ở nhóm thứ nhất")
    team2 = ProjectTeam("P002", "Du an Mobile")
    team2.addMember(shared_employee)
    print(team2.displayTeam())

    print_step(14, "Kết thúc phạm vi cục bộ của nhóm thứ hai")
    print("Khi hàm test_second_team kết thúc, team2 không còn được sử dụng.")


def run_demo() -> None:
    """Chạy toàn bộ kịch bản kiểm thử bắt buộc."""
    print("=" * 72)
    print("LAB03-04 - QUAN LY NHOM DU AN VA NHAN SU (PYTHON)")
    print("=" * 72)

    print_step(1, "Tạo hai Employee bằng hai constructor mô phỏng khác nhau")
    employee1 = Employee("E001", "Nguyen An")
    employee2 = Employee("E002", "Tran Binh", 15_000_000)
    print(employee1.displayInfo())
    print(employee2.displayInfo())

    print_step(2, "Tạo hai SoftwareEngineer bằng hai constructor mô phỏng")
    engineer1 = SoftwareEngineer("SE001", "Le Chi", "Python")
    engineer2 = SoftwareEngineer(
        "SE002", "Pham Dung", 22_000_000, "Java", 3_000_000
    )
    print(engineer1.displayInfo())
    print(engineer2.displayInfo())

    print_step(3, "Tăng lương một nhân sự bằng số tiền cố định")
    employee1.increaseSalary(2_000_000)
    print(employee1.displayInfo())

    print_step(4, "Tăng lương một nhân sự khác theo phần trăm")
    employee2.increaseSalary(10, True)
    print(employee2.displayInfo())

    print_step(5, "Tạo nhóm dự án chưa có trưởng nhóm")
    team1 = ProjectTeam("P001", "He thong quan ly du an")
    print(team1.displayTeam())

    print_step(6, "Thêm một nhân sự bằng addMember(employee)")
    print("Thêm E001:", team1.addMember(employee1))

    print_step(7, "Thêm kỹ sư bằng addMember(employee, True) và đặt làm trưởng nhóm")
    print("Thêm SE002 + làm leader:", team1.addMember(engineer2, True))

    print_step(8, "Thử thêm lại một thành viên đã tồn tại")
    print("Thêm lại E001:", team1.addMember(employee1))

    print_step(9, "Hiển thị danh sách bằng lời gọi đa hình")
    team1.addMember(engineer1)
    print(team1.displayTeam())

    print_step(10, "Tính tổng chi phí nhân sự hằng tháng")
    print(f"Tong chi phi: {team1.calculateTotalMonthlyCost():,.0f} VND")

    print_step(11, "Thử xóa trưởng nhóm hiện tại - thao tác phải bị từ chối")
    print("Xóa SE002:", team1.removeMember("SE002"))

    print_step(12, "Đổi trưởng nhóm rồi xóa người từng là trưởng nhóm")
    team1.changeLeader(employee1)
    print("Leader mới:", team1.leader.id if team1.leader else "None")
    print("Xóa SE002 sau khi đổi leader:", team1.removeMember("SE002"))
    print(team1.displayTeam())

    # Employee có thể đồng thời xuất hiện ở nhiều nhóm khác nhau.
    test_second_team(employee1)
    gc.collect()

    print_step(15, "Chứng minh nhân sự của nhóm thứ hai vẫn tồn tại")
    print("Sau khi team2 bị hủy, employee1 vẫn dùng được:")
    print(employee1.displayInfo())
    print("team1 vẫn chứa E001:", team1.contains("E001"))

    print("\n--- KIỂM TRA BIÊN ---")
    try:
        employee1.increaseSalary(0)
    except ValueError as error:
        print("Tăng lương 0 bị từ chối:", error)

    try:
        Employee("", "Khong Hop Le", 1_000_000)
    except ValueError as error:
        print("Mã nhân sự rỗng bị từ chối:", error)

    print("\nHoàn thành kiểm thử.")


if __name__ == "__main__":
    run_demo()
