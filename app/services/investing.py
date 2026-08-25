from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject, Donation


async def run_investing_process(
    obj: CharityProject | Donation,
    session: AsyncSession
) -> CharityProject | Donation:
    await session.flush()
    projects = await charity_project_crud.get_objs_for_investing(session)
    donations = await donation_crud.get_objs_for_investing(session)
    if obj.invested_amount >= obj.full_amount:
        obj.invested_amount = obj.full_amount
        obj.fully_invested = True
        obj.close_date = datetime.now()
    while projects and donations:
        project = projects[0]
        donation = donations[0]
        project_need = project.full_amount - project.invested_amount
        donation_free = donation.full_amount - donation.invested_amount
        amount = min(project_need, donation_free)
        project.invested_amount += amount
        donation.invested_amount += amount
        if project.invested_amount == project.full_amount:
            project.fully_invested = True
            project.close_date = datetime.now()
            projects.pop(0)
        if donation.invested_amount == donation.full_amount:
            donation.fully_invested = True
            donation.close_date = datetime.now()
            donations.pop(0)
    await session.commit()
    await session.refresh(obj)
    return obj
