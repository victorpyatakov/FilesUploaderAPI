from pydantic import BaseModel


class FileInfo(BaseModel):
    guid: str
    name: str
