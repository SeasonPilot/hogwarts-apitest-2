def test_version():
    from hogwarts_apitest import  __version__
    assert isinstance(__version__,str)

import requests

class BaseApi(object):
    url = ""
    method = ""
    headers = {}
    json = {}
    params = {}


    def set_params(self,**params):
        self.params = params
        return self


    def run(self):
        
        self.resp = requests.request(
            self.method,
            self.url,
            headers=self.headers,
            params=self.params,
            data=self.json
        )
        print(self)
        return self

    def validate(self,key,value):
        actual_value=getattr(self.resp,key)
        assert actual_value ==value
        return self

class ApiHttpbinGet(BaseApi):

    url ="http://httpbin.org/get"
    method='GET'
    headers= {"accept":"application/json"}





class ApiHttpbinPost(BaseApi):

    url ="http://httpbin.org/post"
    method='POST'
    headers= {"accept":"application/json"}


    def set_data(self,**json):

        self.json = json
        return self




def test_httpbin_get():
    ApiHttpbinGet().\
        run().\
        validate("status_code",200)

def test_httpbin_get_with_param():

    ApiHttpbinGet().set_params(abc=123)\
        .run()\
        .validate("status_code", 200)


def test_httpbin_post():

    ApiHttpbinPost().set_data(abc=123)\
        .run() \
        .validate("status_code", 200)

