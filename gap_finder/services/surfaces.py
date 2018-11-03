from gap_finder.models import surface
import sqlalchemy as sa


class SurfaceService:
    def __init__(self, engine):
        self.engine = engine

    def insert_new_surface(
            self,
            xyz_grid=None,
            plane_cords=None,
            dots_count=None,
            meta=None
    ):
        if not meta:
            meta = {}

        query = surface.insert().values(
            xyz_grid=xyz_grid,
            plane_cords=plane_cords,
            dots_count=dots_count,
            plane_cords_count=len(plane_cords),
            meta=meta
        )

        self.engine.execute(query)

    def get_surfaces(self):
        query = sa.select([surface])
        return self.engine.execute(query)
