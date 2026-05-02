from dataclasses import dataclass

@dataclass
class Message:
    role: str
    task_description: str
    task_structure: str
    criteria_format: str
    criteria_description: str
    response_restrictions: str
    response_fromat: str