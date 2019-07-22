from flask import current_app, _app_ctx_stack
from .url_converter import UrlConverter
from .url_encoder import UrlEncoder

class ShortUrl(object):

    def __init__(self, app=None):
        self.app = app
        self.converter = UrlConverter()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('SHORT_URL_MIN_LENGTH', 5)
        app.url_map.converters['short_url'] = self.converter

    @property
    def encoder(self):
        if hasattr(self, '_encoder'):
            return self._encoder

        self._encoder = UrlEncoder()
        return self._encoder

    def encode(self, n):
        return self.encoder.encode(n)

    def decode(self, n):
        return self.encoder.decode(n)

    def enbase(self, n):
        min_length = current_app.config['SHORT_URL_MIN_LENGTH']
        return self.encoder.enbase(n, min_length)

    def debase(self, n):
        return self.encoder.debase(n)

    def encode_url(self, n):
        """
        Encode the id number to a short url.
        ::
            >>> su = ShortUrl()
            >>> su.encode_url(12)
        """
        min_length = current_app.config['SHORT_URL_MIN_LENGTH']
        return self.encoder.encode_url(n, min_length)

    def decode_url(self, n):
        """
        Decode the short url into the id number.
        ::
            >>> su = ShortUrl()
            >>> su.decode_url('zkf2n')
        """
        return self.encoder.decode_url(n)
