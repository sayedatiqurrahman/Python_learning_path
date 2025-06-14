from pydantic import BaseModel, Field  # type:ignore
from typing import Optional


# TODO: Create a employee model
# Fields:
# - id: int
# - name: str(minimum 3 char)
# - department: Optional[str] default general
# - salary: float (must be >=10000)


# To Learn about Field visit:  https://docs.pydantic.dev/latest/concepts/fields/


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=12,
        description="Employee Name",
        examples="Atiqur Rahman",
    )
    department: Optional[str] = "General"
    salary: float = Field(ge=100000)
