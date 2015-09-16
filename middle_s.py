#-*- coding: utf-8 -*-
import sys
import socket
import requests
import SimpleHTTPServer
import SocketServer
import logging
import cgi

most_efficient = {}

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def __init__(self,request,client_address,server):
		global most_efficient
		SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self,request,client_address,server)
		most_efficient = {"problem_id":0,"answer_string":"","score":9999999,"time":0,"version":""}

	def do_GET(self):
		logging.error(self.headers)
		self.send_response(200)

	def do_POST(self):
		global most_efficient
		form = cgi.FieldStorage(
			fp = self.rfile,
			headers = self.headers,
			environ = {"REQUEST_METHOD":"POST","CONTENT_TYPE":self.headers["Content-Type"],})
		self.send_response(200)

		if most_efficient.get("score") > form["score"].value:
			requests.post("http://sp2lc.salesio-sp.ac.jp/procon26-test/procon.php",
				data = {"problem_id":form["problem_id"].value,"answer_string":form["answer_string"].value,"score":form["score"].value,"time":form["time"].value,"version":form["version"].value})
			most_efficient = {"problem_id":form["problem_id"].value,"answer_string":form["answer_string"].value,"score":form["score"].value,"time":form["time"].value,"version":form["version"].value}

if __name__ == "__main__":

	HOST = socket.gethostbyname(socket.gethostname())#ipget
	PORT = 8000
	Handler = ServerHandler
	httpd = SocketServer.TCPServer((HOST, PORT), Handler)

	print "serving at port", PORT
	httpd.serve_forever()