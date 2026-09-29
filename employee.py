"""
/****************/
Mã sinh viên: Phạm Anh Tú
Họ tên: 202419007
/****************/

Lớp Employee cho bài thực hành quản lý nhóm dự án và nhân sự.
"""


class Employee:
    """Biểu diễn một nhân sự thông thường."""

    def __init__(
        self,
        employee_id: str = "UNKNOWN",
        full_name: str = "Unnamed employee",
        base_salary: float = 0.0,
    ) -> None:
        """
        Mô phỏng ba constructor của đề bằng tham số mặc định:
        - Employee()
        - Employee(id, fullName)
        - Employee(id, fullName, baseSalary)
        """
        self._validate_non_empty(employee_id, "Mã nhân sự")
        self._validate_non_empty(full_name, "Họ tên")
        if base_salary < 0:
            raise ValueError("Lương cơ bản không được âm.")

        self._id = employee_id
        self._fullName = full_name
        self._baseSalary = float(base_salary)

    @staticmethod
    def _validate_non_empty(value: str, field_name: str) -> None:
        """Kiểm tra chuỗi không rỗng hoặc chỉ gồm khoảng trắng."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} không được rỗng.")

    @property
    def id(self) -> str:
        """Getter cho mã nhân sự."""
        return self._id

    @property
    def fullName(self) -> str:
        """Getter cho họ tên."""
        return self._fullName

    @property
    def baseSalary(self) -> float:
        """Getter cho lương cơ bản."""
        return self._baseSalary

    def increaseSalary(self, value: float, byPercentage: bool | None = None) -> None:
        """
        Mô phỏng hai phiên bản increaseSalary() của đề.

        - increaseSalary(amount): tăng số tiền cố định.
        - increaseSalary(value, True): tăng theo phần trăm.
        - increaseSalary(value, False): tăng số tiền cố định.
        """
        if value <= 0:
            raise ValueError("Giá trị tăng lương phải dương.")

        if byPercentage is None or byPercentage is False:
            self._baseSalary += float(value)
        elif byPercentage is True:
            self._baseSalary *= 1.0 + float(value) / 100.0
        else:
            raise TypeError("byPercentage phải là bool hoặc None.")

    def calculateMonthlyCost(self) -> float:
        """Chi phí hằng tháng của Employee mặc định bằng lương cơ bản."""
        return self._baseSalary

    def displayInfo(self) -> str:
        """Trả về chuỗi thông tin nhân sự; được ghi đè ở lớp dẫn xuất."""
        return (
            f"Employee(id={self._id}, name={self._fullName}, "
            f"baseSalary={self._baseSalary:,.0f})"
        )

    def __del__(self) -> None:
        """In thông báo để quan sát vòng đời đối tượng."""
        try:
            print(f"[Destructor] Employee {self._id} được hủy.")
        except Exception:
            # Tránh lỗi khi Python đang kết thúc interpreter.
            pass
