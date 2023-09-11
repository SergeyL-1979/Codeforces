from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, MetaData
from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()

association_table = Table(
    "association_table",
    metadata,
    Column("theme_id", ForeignKey("theme.id")),
    Column("problem_id", ForeignKey("problem.id")),
)

theme = Table(
    "theme",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("theme", String),
    # Column("children", secondary=association_table),
)


problem = Table(
    "problem",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("contest_id", Integer,),
    Column("index", String),
    Column("title", String),
    Column("theme_id", Integer, ForeignKey(theme.c.id)),
    Column("solve_count", Integer),
    Column("difficulty", Integer),
    Column("date", TIMESTAMP),
)


class Theme:
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    theme: Mapped[str] = mapped_column(String, nullable=False)


class Problem:
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    contest_id: Mapped[int] = mapped_column(Integer)
    index: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    theme: Mapped[int] = mapped_column(Integer, ForeignKey(theme.c.id))
    solve_count: Mapped[int] = mapped_column(Integer)
    difficulty: Mapped[int] = mapped_column(Integer)
    date: Mapped[str] = mapped_column(TIMESTAMP, default=datetime.utcnow)




