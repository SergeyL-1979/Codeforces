from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, MetaData

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





