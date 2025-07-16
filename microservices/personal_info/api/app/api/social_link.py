from fastapi import APIRouter, Depends

from api.app.core.database import get_db
from api.app.models.social_link import SocialLink
from api.app.schemas.social_link import SocialLinkOut, SocialLinkCreate

router = APIRouter(prefix="/social-links", tags=["Social Links"])


@router.post("/", response_model=list[SocialLinkOut])
async def add_social_links(
        links: list[SocialLinkCreate],
        db=Depends(get_db)
):
    user_id = 1

    created = []

    for link in links:
        item = SocialLink(user_id=user_id, **link.model_dump())
        db.add(item)
        created.append(item)

    await db.commit()

    for item in created:
        await db.refresh(item)

    return created
