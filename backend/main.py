from typing import Optional, Any, List

from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from crudbase import CRUDBase


class Todo(SQLModel, table=True):
    uuid: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )

    login: str
    name: str
    description: str


class TodoBase(SQLModel):
    login: str
    name: str
    description: str


class TodoCreate(TodoBase):
    pass


class TodoRead(TodoBase):
    uuid: UUID


class TodoUpdate(SQLModel):
    pass


postgresql_url = 'postgresql+asyncpg://postegresql:2g75DA8GzB=2a15W@37.139.35.73:5432/postgres'
engine = create_async_engine(
    postgresql_url,
    future=True,
    echo=True,
)

async def get_session() -> AsyncSession:
    async with AsyncSession(engine) as session:
        yield session


class BaseServiceError(Exception):
    pass


class ClientError(BaseServiceError):
    pass


class ServerError(BaseServiceError):
    pass


class EntityConflictError(ClientError):
    pass


class EntityDoesNotExistError(ClientError):
    pass


class TodoCRUD(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    async def get_by_uuid(self, uuid: UUID) -> Optional[Todo]:
        statement = select(self.model).where(self.model.uuid == uuid)
        results = await self.session.execute(statement)  # noqa

        todo = results.scalar_one_or_none()
        if todo:
            await self.session.refresh(todo)

        return todo


class TodoService:
    def __init__(self, session: AsyncSession):
        self.todos = TodoCRUD(Todo, session)

    async def get(self, push_uuid: UUID) -> Optional[Todo]:
        todo = await self.todos.get_by_uuid(push_uuid)
        if not todo:
            raise EntityDoesNotExistError from None

        return todo

    async def add(self, data: TodoCreate):
        return await self.todos.create(data)

    async def get_all(self) -> List[Todo]:
        return await self.todos.get()

    async def remove(self, push_uuid: UUID) -> Any:
        todo = await self.todos.get_by_uuid(push_uuid)
        if not todo:
            raise EntityDoesNotExistError from None
        return await self.todos.delete(todo)


router = APIRouter()

@router.post(
    '/remove',
    response_model=TodoRead
)
async def remove(
        uuid: UUID,
        session: get_session = Depends(),  # type: ignore
) -> Any:
    return await TodoService(session).remove(uuid)


@router.post(
    '/add',
    response_model=TodoRead
)
async def add(
        data: TodoCreate,
        session: get_session = Depends(),  # type: ignore
) -> Any:
    return await TodoService(session).add(data)

@router.post(
    '/get',
    response_model=List[TodoRead]
)
async def get(
        session: get_session = Depends(),  # type: ignore
) -> Any:
    return await TodoService(session).get_all()

router_api = APIRouter(
    prefix='/v1',
)

router_api.include_router(
    router=router,
    prefix="/todos",
    tags=['todos'],
)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)



def get_application() -> FastAPI:
    _app = FastAPI(
        title="TODLIST",
        description="Vadim Lukin PI-2-18",
        version="1.0.0",
        debug=True,
    )

    _app.add_event_handler(
        event_type="startup",
        func=create_db_and_tables,
    )

    _app.include_router(
        router=router,
        prefix='/api',
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    return _app


app = get_application()