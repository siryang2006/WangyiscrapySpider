import redis

#r=redis.Redis(host='127.0.0.1',port=6609,db=0)
#r.set('name','baby')
#print(r.get('name'))
#print(r.dbsize())

class UrlObject:
    def __init__(self):
        print redis.__file__
        self.client =  redis.Redis(host='localhost', port=6379, decode_responses=True) 

    def getNextUrl(self):
        print self.client.ping()

    def insert(self, url):
        self.client.sadd("urls", url)
        print url