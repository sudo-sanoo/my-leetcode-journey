class Codec:
    def __init__(self):
        self.urlmap = {}
        self.prefix = "https://your-tinyurl-website.com/encode-decode-url-service/this-url-is-unnecessarily-long/what-am-i-doing/"

    # generate a 6 character long random code
    def getCode(self):
        return "".join((random.choice(string.ascii_letters + string.digits) for _ in range(6)))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        code = self.getCode()
        while code in self.urlmap: # if the code exists (used), generate another code
            code = self.getCode()
        self.urlmap[code] = longUrl # map the code as the key to the longUrl as its value
        return self.prefix + code # the shortUrl is made up of a prefix and the 6-char code
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        code = shortUrl.replace(self.prefix, "") # extract only the code
        return self.urlmap[code] # return the value mapped to the code

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
