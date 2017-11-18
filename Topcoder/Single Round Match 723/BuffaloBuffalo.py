class BuffaloBuffalo:
    def check(self, s):
        if s != s.strip():
            return "Not good"

        for word in s.split(' '):
            if word != 'buffalo':
                return "Not good"

        return "Good"
