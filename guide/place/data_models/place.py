import attr

from ..models.place import Place as DBPlace


@attr.s(slots=True)
class Location:
    lat = attr.ib()
    lng = attr.ib()

    @classmethod
    def from_dict(cls, data):
        return cls(
            lat=data['lat'],
            lng=data['lng'],
        )


@attr.s(slots=True)
class Place:
    """
    Data object for a Place.
    """
    location = attr.ib()
    display_name = attr.ib()
    description = attr.ib()
    display_address = attr.ib()

    @classmethod
    def from_dict(cls, data):
        return cls(
            location=Location.from_dict(data['location']),
            display_name=data['display_name'],
            display_address=data['display_address'],
            description=data.get('description'),
        )

    @classmethod
    def safe_from_dict(cls, data):
        try:
            return cls.from_dict(data)
        except KeyError:
            return None

    @classmethod
    def from_db_model(cls, db_model):
        return cls(
            location=Location(lat=db_model.lat, lng=db_model.lng),
            display_name=db_model.display_name,
            display_address=db_model.display_address,
            description=db_model.description,
        )

    def to_db_model(self):
        return DBPlace(
            lat=self.location.lat,
            lng=self.location.lng,
            display_name=self.display_name,
            display_address=self.display_address,
            description=self.description,
        )
