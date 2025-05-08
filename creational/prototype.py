import copy
from datetime import date

# Prototype class representing an employment contract
class EmploymentContract:
    def __init__(self, company, position, start_date, salary):
        # Base contract data
        self.company = company
        self.position = position
        self.start_date = start_date
        self.salary = salary
        self.employee_name = None  # Will be assigned after cloning

    def clone(self):
        # Create a deep copy of this contract
        return copy.deepcopy(self)

    def set_employee(self, name, salary=None, start_date=None):
        # Customize the contract for a specific employee
        self.employee_name = name
        if salary:
            self.salary = salary
        if start_date:
            self.start_date = start_date

    def __str__(self):
        # Nicely format the contract details for printing
        return (
            f"Employee: {self.employee_name}\n"
            f"Company: {self.company}\n"
            f"Position: {self.position}\n"
            f"Start Date: {self.start_date}\n"
            f"Salary: ${self.salary}\n"
        )

# Create a base contract template shared by all software developers
contract_template = EmploymentContract(
    company="TechCorp",
    position="Software Developer",
    start_date=date.today(),
    salary=70000
)

# Clone the template for Alice and customize the salary
alice_contract = contract_template.clone()
alice_contract.set_employee("Alice Smith", salary=75000)

# Clone the template for Bob and customize the start date
bob_contract = contract_template.clone()
bob_contract.set_employee("Bob Johnson", start_date=date(2025, 6, 1))

# Output the customized contracts
print(alice_contract)
print(bob_contract)
