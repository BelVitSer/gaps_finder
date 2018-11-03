import sqlalchemy as sa
from sqlalchemy.types import JSON

from gap_finder.settings import DB_SETTINGS

metadata = sa.MetaData()

surface = sa.Table(
    "surface", metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column("xyz_grid", sa.PickleType, nullable=False),
    sa.Column("plane_cords", sa.JSON, default=[], nullable=False),
    sa.Column("dots_count", sa.Integer, nullable=False),
    sa.Column("plane_cords_count", sa.Integer, nullable=False),
    sa.Column("meta", JSON, default={})
)


def get_engine(user=None, password=None, host=None, port=None, db_name=None):
    """
    Возвращает engine

    :param user:
    :param password:
    :param host:
    :param port:
    :param db_name:
    :return:
    """
    db_url = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
        user=user,
        password=password,
        host=host,
        db_name=db_name,
        port=str(port)
    )

    return sa.create_engine(db_url)


def create_tables(engine):
    metadata.create_all(engine, checkfirst=True)


if __name__ == '__main__':
    from gap_finder.generation import get_x_y_grid
    from gap_finder.services.surfaces import SurfaceService

    engine = get_engine(**DB_SETTINGS)
    X, Y = get_x_y_grid(10)
    Z = Y

    create_tables(engine)
    s = SurfaceService(engine)
    p = s.get_surfaces()
