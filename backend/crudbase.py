from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from sqlmodel import SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateModelType = TypeVar("CreateModelType", bound=SQLModel)
UpdateModelType = TypeVar("UpdateModelType", bound=SQLModel)


class CRUDBase(Generic[ModelType, CreateModelType, UpdateModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model = model
        self.session = session

    async def get(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        statement = select(self.model).offset(skip).limit(limit)
        results = await self.session.execute(statement)  # noqa
        return results.scalars().all()

    async def create(self, obj_in: CreateModelType) -> ModelType:
        db_obj = self.model.from_orm(obj_in)
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def read(self, model_id: Any) -> Optional[ModelType]:
        statement = select(self.model).where(self.model.id == model_id)
        results = await self.session.exec(statement)  # noqa
        return results.first()

    async def update(
            self, db_obj: ModelType,
            obj_in: Union[UpdateModelType, Dict[str, Any]],
    ) -> ModelType:
        data = obj_in if isinstance(obj_in, dict) else obj_in.dict(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(db_obj, key, value)

        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def delete(
            self, db_obj: ModelType,
    ) -> ModelType:
        await self.session.delete(db_obj)
        await self.session.commit()
        return db_obj
