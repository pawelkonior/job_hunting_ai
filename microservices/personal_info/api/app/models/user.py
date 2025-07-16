from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

from api.app.core.database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String, nullable=False)
    email: Mapped[String] = mapped_column(String, nullable=False, unique=True)


    social_links: Mapped[list["SocialLink"]] = relationship(back_populates="user", cascade="all, delete-orphan")
