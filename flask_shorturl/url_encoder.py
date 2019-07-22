class UrlEncoder(object):

    def __init__(self):
        self.alphabet = 'mn6j2c4rv8bpygw95z7hsdaetxuk3fq'
        self.block_size = 24
        self.mask = (1 << 24) - 1
        self.mapping = range(24)

    def encode_url(self, n, min_length=MIN_LENGTH):
        return self.enbase(self.encode(n), min_length)

    def decode_url(self, n):
        return self.decode(self.debase(n))

    def encode(self, n):
        return (n & ~self.mask) | self._encode(n & self.mask)

    def _encode(self, n):
        result = 0
        for i, b in enumerate(reversed(self.mapping)):
            if n & (1 << i):
                result |= (1 << b)
        return result

    def decode(self, n):
        return (n & ~self.mask) | self._decode(n & self.mask)

    def _decode(self, n):
        result = 0
        for i, b in enumerate(reversed(self.mapping)):
            if n & (1 << b):
                result |= (1 << i)
        return result

    def enbase(self, x, min_length=MIN_LENGTH):
        result = self._enbase(x)
        padding = self.alphabet[0] * (min_length - len(result))
        return '%s%s' % (padding, result)

    def _enbase(self, x):
        n = len(self.alphabet)
        if x < n:
            return self.alphabet[x]
        return self._enbase(int(x // n)) + self.alphabet[int(x % n)]

    def debase(self, x):
        n = len(self.alphabet)
        result = 0
        for i, c in enumerate(reversed(x)):
            result += self.alphabet.index(c) * (n ** i)
        return result

