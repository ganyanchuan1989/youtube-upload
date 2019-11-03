import httplib2
import socks
# YOUTUBE_UPLOAD_SCOPE = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"]

hObj = httplib2.Http(proxy_info=httplib2.ProxyInfo(
    socks.PROXY_TYPE_HTTP, "127.0.0.1", 1080))
#response, content = hObj.request('https://www.w3.org')
response, content = hObj.request('https://www.google.com')
# content
print(content)
