 #-*- coding: utf-8 -*-
import sys
import socket
import requests
import SimpleHTTPServer
import SocketServer
import logging
import cgi

if __name__ == "__main__":
	
	r=requests.post("http://"+socket.gethostbyname(socket.gethostname())+":8000",data={"problem_id":1,"answer_string":"ssxxrrrrs","score":50,"time":0,"version":"abc"})
