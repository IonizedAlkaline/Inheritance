class Bird:
    def __init__(self):
        print('bird is ready')
    def whoisthis(self):
        print('bird')
    def swim(self):
        print('swim faster')

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print('penguin is ready')
    def whoisthis(self):
        print('penguin')
    def run(self):
        print('run faster')
bob = Penguin()
bob.whoisthis()
bob.run()
bob.swim()
