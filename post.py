 #-*- coding: utf-8 -*-
import sys
import socket
import requests
import random


if __name__ == "__main__":
	
	strs = 'abcdefghijklmnopqrstuvwxyz'
	random.choice(strs)  #a〜zでランダムに１文字
	answerstr="".join([random.choice(strs) for x in xrange(10)])
	score_num=random.randint(0,100)

	r=requests.post("http://"+socket.gethostbyname(socket.gethostname())+":8000",data={"problem_id":1,"answer_string":answerstr,"score":score_num,"time":0,"version":"abc","used_pieces":250})
