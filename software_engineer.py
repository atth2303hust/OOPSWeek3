"""
Họ và tên: Phạm Anh Tú
MSSV: 202419007


"""

from employee import Employee


class SoftwareEngineer(Employee):
    """Nhân sự kỹ sư phần mềm có ngôn ngữ chính và phụ cấp kỹ thuật."""

    def __init__(self, employee_id: str, full_name: str, *args) -> None:
        """
        Mô phỏng hai constructor của đề:

        1. SoftwareEngineer(id, fullName, primaryLanguage)
        2. SoftwareEngineer(id, fullName, baseSalary,
                            primaryLanguage, technicalAllowance)
        """
        if len(args) == 1:
            base_salary = 0.0
            primary_language = args[0]
            technical_allowance = 0.0
        elif len(args) == 3:
            base_salary, primary_language, technical_allowance = args
        else:
            raise TypeError(
                "SoftwareEngineer nhận 3 hoặc 5 đối số theo hai constructor của đề."
            )

        super().__init__(employee_id, full_name, float(base_salary))
        self._validate_non_empty(primary_language, "Ngôn ngữ lập trình chính")
        if technical_allowance < 0:
            raise ValueError("Phụ cấp kỹ thuật không được âm.")

        self._primaryLanguage = primary_language
        self._technicalAllowance = float(technical_allowance)

    @property
    def primaryLanguage(self) -> str:
        """Getter cho ngôn ngữ lập trình chính."""
        return self._primaryLanguage

    @property
    def technicalAllowance(self) -> float:
        """Getter cho phụ cấp kỹ thuật."""
        return self._technicalAllowance

    def calculateMonthlyCost(self) -> float:
        """Ghi đè: tổng chi phí = lương cơ bản + phụ cấp kỹ thuật."""
        return self.baseSalary + self._technicalAllowance

    def displayInfo(self) -> str:
        """Ghi đè hiển thị thông tin kỹ sư phần mềm."""
        return (
            f"SoftwareEngineer(id={self.id}, name={self.fullName}, "
            f"baseSalary={self.baseSalary:,.0f}, language={self._primaryLanguage}, "
            f"allowance={self._technicalAllowance:,.0f})"
        )

    def __del__(self) -> None:
        """In thông báo hủy riêng của SoftwareEngineer rồi gọi destructor cha."""
        try:
            print(f"[Destructor] SoftwareEngineer {self.id} được hủy.")
        except Exception:
            pass
        super().__del__()
