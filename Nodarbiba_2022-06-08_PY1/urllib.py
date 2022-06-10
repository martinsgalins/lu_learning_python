import urllib.request


class PageLoader:

    def __init__(self, url):
        self.url = url

    def get_response(self):
        response = urllib.request.urlopen(self.url)
        return response

    def get_content(self):
        response = self.get_response()
        content = response.read().decode('utf-8')

        return content

    def print_msg(self):
        response = self.get_response()
        return response.msg
    
aaa = PageLoader('https://tvnet.lv')
print(aaa.get_content())
print(aaa.print_msg())