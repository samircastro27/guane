
from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class IServiceBase(Generic[CreateSchemaType, UpdateSchemaType], ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *, obj_in: CreateSchemaType) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def update(self, *, _id: int, obj_in: Dict[str, Any]) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *, _id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *, _id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_all(
        self, *, payload: Optional[Dict[str, Any]], skip: int, limit: int
    ) -> Any:
        raise NotImplementedError