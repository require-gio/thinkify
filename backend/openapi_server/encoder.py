from connexion.jsonifier import Jsonifier

from openapi_server.models.base_model import Model


class JSONEncoder(Jsonifier):

    def dumps(self, data, **kwargs):
        """Central point where JSON serialization happens inside
        Connexion.
        """
        if isinstance(data, list):
            return super().dumps([self.dump(item, **kwargs) for item in data])

        return super().dumps(self.dump(data, **kwargs))

    def dump(self, data, **kwargs):
        if isinstance(data, Model):
            dikt = {}
            for attr in data.openapi_types:
                value = getattr(data, attr)
                if value is None:
                    continue
                attr = data.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return data