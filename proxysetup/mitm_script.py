from mitmproxy import ctx

def request(flow):
     print ("{0}:{1}".format(flow.request.host, flow.request.url))
