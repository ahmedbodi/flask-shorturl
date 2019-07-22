from werkzeug.routing import BaseConverter, ValidationError
from .url_encoder import UrlEncoder

class UrlConverter(BaseConverter):

    def __init__(self, url_map):
        super(UrlConverter, self).__init__(url_map)
        self.encoder = UrlEncoder()

    def to_python(self, value):
        try:
            return self.encoder.decode_url(value)
        except Exception as exc:
            raise ValidationError("Invalid URL")

    def to_url(self, value):
        return self.encoder.encode_url(value)

