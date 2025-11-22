from typing import Optional
from pydantic import BaseModel, Field

class ServiceRequestSchemes(BaseModel):
    title: str
    brief_info: str
    room_numb: str
    quest_name: str
    service: str

class ReturningApplication(ServiceRequestSchemes):
    id: int

class ApplicationUpdate(ServiceRequestSchemes):
    pass

class WorkerAnswear(BaseModel):
    title: str
    time: str
    worker_name: str