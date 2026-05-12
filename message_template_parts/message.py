from dataclasses import dataclass

@dataclass
class Message:
    role: str
    task_description: str
    task_structure: str
    criteria: str
    response_restrictions: str
    response_fromat: str