#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# 2019081312030 小小程苑
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import socketserver
import json

PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("interface.html", "rb") as f:
            小小程苑要访问接口啦 = f.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(小小程苑要访问接口啦))
        self.end_headers()
        self.wfile.write(小小程苑要访问接口啦)
        

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        一堆乱码 = body.decode().split("&")
        又一堆乱码 = [东西.split("=") for 东西 in 一堆乱码]

        if( [1 for 东西 in 又一堆乱码 if 东西[1] and 东西[0].endswith("name")] ):
            data = "，".join(["你的" + 东西[0]  + "是" +  东西[1] for 东西 in 又一堆乱码 if 东西[1]])
            self.send_response(200)
        else:
            data = "必填项未填写"
            self.send_response(500)


        返回json = json.dumps({"data": data}, ensure_ascii=False)
        self.send_header("Content-encoding", "utf-8")
        self.send_header("Content-type", "text/json")
        self.send_header("Content-length", len(返回json))
        self.end_headers()
        self.wfile.write(返回json.encode())


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

#
# 一点点参考资料
# https://docs.python.org/3/library/http.server.html
# https://blog.anvileight.com/posts/simple-python-http-server/
# https://stackoverflow.com/questions/6391280/simplehttprequesthandler-override-do-get
# https://www.w3schools.com/python/python_json.asp
#