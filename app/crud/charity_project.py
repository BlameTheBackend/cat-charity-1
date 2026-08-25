from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.investable import CRUDInvestable
from app.models import CharityProject


class CRUDCharityProject(CRUDInvestable):

    async def get_charity_project_id_by_name(
            self, project_name: str, session: AsyncSession) -> Optional[int]:
        db_project_id_result = await session.execute(
            select(CharityProject.id)
            .where(CharityProject.name == project_name))
        db_project_id = db_project_id_result.scalars().first()
        return db_project_id


charity_project_crud = CRUDCharityProject(CharityProject)
