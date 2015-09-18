#-*- coding: utf-8 -*-
import os
import sys
import socket
import requests
import SimpleHTTPServer
import SocketServer
import logging
import cgi

most_efficient = {"problem_id":0,"answer_string":"aaa","score":9999999,"time":0,"version":"xxx","used_pieces":256}

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

	def __init__(self,request,client_address,server):
		global most_efficient
		SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self,request,client_address,server)
	#	most_efficient = {"problem_id":0,"answer_string":"","score":9999999,"time":0,"version":""}

	def do_GET(self):
		logging.error(self.headers)
		self.send_response(200)
		self.end_headers()
		self.wfile.write("error")

	def do_POST(self):
		global most_efficient
		form = cgi.FieldStorage(
			fp = self.rfile,
			headers = self.headers,
			environ = {"REQUEST_METHOD":"POST","CONTENT_TYPE":self.headers["Content-Type"],})
		self.send_response(200)
		self.end_headers()
		self.wfile.write("ok")
		print "score"
		print most_efficient["score"]
		print form["score"].value
		print "used_pieces"
		print most_efficient["used_pieces"]
		print form["used_pieces"].value

		if most_efficient["score"] > int(form["score"].value):
			requests.post("http://sp2lc.salesio-sp.ac.jp/procon26-test/procon.php",
				data = {"problem_id":form["problem_id"].value,"answer_string":form["answer_string"].value,"score":form["score"].value,"time":form["time"].value,"version":form["version"].value,"used_pieces":form["used_pieces"].value})
			most_efficient = {"problem_id":int(form["problem_id"].value),"answer_string":form["answer_string"].value,"score":int(form["score"].value),"time":int(form["time"].value),"version":form["version"].value,"used_pieces":int(form["used_pieces"].value)}
			print most_efficient
			strs = form["answer_string"].value
			files = os.listdir(dirlists)
			filelists = len(files)
			filelists +=1
			print filelists
			f = open(dirlists+"/"+"answer"+str(filelists)+".txt","w")
			f.writelines(strs)
			print "answer"+str(filelists)+".txt"
			print strs
			f.close()
		elif most_efficient["score"] == int(form["score"].value):
			if most_efficient["used_pieces"] > int(form["used_pieces"].value):
				requests.post("http://sp2lc.salesio-sp.ac.jp/procon26-test/procon.php",
					data = {"problem_id":form["problem_id"].value,"answer_string":form["answer_string"].value,"score":form["score"].value,"time":form["time"].value,"version":form["version"].value,"used_pieces":form["used_pieces"].value})
				most_efficient = {"problem_id":int(form["problem_id"].value),"answer_string":form["answer_string"].value,"score":int(form["score"].value),"time":int(form["time"].value),"version":form["version"].value,"used_pieces":int(form["used_pieces"].value)}
				print most_efficient
				strs = form["answer_string"].value
				files = os.listdir(dirlists)
				filelists = len(files)
				filelists +=1
				print filelists
				f = open(dirlists+"/"+"answer"+str(filelists)+".txt","w")
				f.writelines(strs)
				print "answer"+str(filelists)+".txt"
				print strs
				f.close()

if __name__ == "__main__":

	path = "Dirs/"
	dirs = os.listdir(path)
	dirlists = len(dirs)
	dirlists +=1
	if dirs[0]==".DS_Store":
		dirlists -=1
	dirlists = path+"answers"+str(dirlists)
	os.mkdir(dirlists)
	print "mkdir "+dirlists

	HOST = socket.gethostbyname(socket.gethostname())#ipget
	PORT = 8000
	Handler = ServerHandler
	httpd = SocketServer.TCPServer((HOST, PORT), Handler)

	print "serving at port", PORT
	httpd.serve_forever()
