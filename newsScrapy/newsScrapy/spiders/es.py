#sudo pip install Elasticsearch
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

class ElasticObj:
    def __init__(self, ip ="127.0.0.1"):
        #self.es = Elasticsearch([ip],http_auth=('elastic', 'password'),port=9200)
        self.es = Elasticsearch([ip])
        #self.es.indices.create(index='html-index', ignore)

    def insert(self, url, html):
            data = {
                "@timestamp":datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+0800"),
                "url":url,
                "html":html
            }
            self.es.index(index="html-index", doc_type="html", body=data)

#obj = ElasticObj()
#obj.insert("testurl", "test html<body></body>");

