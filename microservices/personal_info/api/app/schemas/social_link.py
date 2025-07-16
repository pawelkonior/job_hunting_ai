from pydantic import BaseModel, HttpUrl, model_validator, field_serializer


class SocialLinkCreate(BaseModel):
    platform: str
    url: HttpUrl

    @field_serializer("url")
    def serialize_url(self, url: HttpUrl) -> str:
        return str(url)


class SocialLinkOut(SocialLinkCreate):
    id: int

    class Config:
        orm_mode = True
