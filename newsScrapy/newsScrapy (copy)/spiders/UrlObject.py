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
        #print self.client.ping()
        url = self.client.spop("ToScrayped")
        print("to scrapy:",url)
        return url
        #self.client.srem("ToScrayped", url)

    def toScrapyed(self, url):
        if None != self.client.sismember("Scrayped", url):
            print("exist:", url)
            self.client.sadd("ToScrayped", url)
        else:
            print("inserted:", url)

    def scrapyed(self, url):
        self.client.sadd("Scrayped", url)
        
        #r.srem("set_name2","bb","dd")
        print("scrapyed:",url)