#!/usr/bin/env python3
from passlib.hash import pbkdf2_sha256
import sqlite3
from tqdm import tqdm 
from sqlite3 import Error
import base64
import os
from os import listdir
import os.path
import string
from printplus import PrintPlus
from getpass import getpass
import random

printer = PrintPlus()
db='.misc/storage.db'
ext=[base64.b64decode(bytes("LmphdmE=","utf-8")).decode("utf-8"),base64.b64decode(bytes("LmM=","utf-8")).decode("utf-8"),base64.b64decode(bytes("LmNwcA==","utf-8")).decode("utf-8"),base64.b64decode(bytes("LnB5","utf-8")).decode("utf-8"),base64.b64decode(bytes("LnNxbA==","utf-8")).decode("utf-8")]

def init(db):
	con = None
	try:
		con = sqlite3.connect(db)
	except Error as e:
		print(e)
	if(con!=None):
		cur = con.cursor()
		sql = base64.b64decode(bytes("Q1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgZGF0YSAob2cgVEVYVCwgaGlkIFRFWFQp","utf-8")).decode("utf-8")
		cur.execute(sql)
		sql = base64.b64decode(bytes("Q1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgcGFzcyAoZW5jIFRFWFQscyBJTlQgREVGQVVMVCAwKQ==","utf-8")).decode("utf-8")
		cur.execute(sql)
		con.commit()
	return con

	

def hasUser(cur):
	sql = base64.b64decode(bytes("U0VMRUNUICogZnJvbSBwYXNz","utf-8")).decode("utf-8")
	cur.execute(sql)
	res=cur.fetchall()
	if(len(res)==0):
		return False
	return True


def createUser(con):
	cur = con.cursor()
	printer.text("Hey do you have somethin to hide;) ??").bold().center().show()
	print()
	printer.text(" If you forget this passowrd you will be not able to recover files ").yellow().blanks('-').center().show()
	p=''
	r='a'
	while(True):
		print()
		p = input(printer.getColored(base64.b64decode(bytes("RW50ZXIgbmV3IHBhc3N3b3JkOg==","utf-8")).decode("utf-8"),printer.colors['BOLD']))
		r = input(printer.getColored(base64.b64decode(bytes("UmVwZWF0IHBhc3N3b3JkOg==","utf-8")).decode("utf-8"),printer.colors['BOLD']))

		if(p != r):
			printer.text(base64.b64decode(bytes("UGFzc3dvcmQgZGlkIG5vdCBtYXRjaC5cblBsZWFzZSB0cnkgYWdhaW4uLg==","utf-8")).decode("utf-8")).red().bold().show()
			continue
		if(len(p)<8):
			printer.text(base64.b64decode(bytes("TGVuZ3RoIG9mIHBhc3N3b3JkIG11c3QgYmUgbWluaW11bSA4IGNoYXJlY3RlcnMuXG5QbGVhc2UgdHJ5IGFnYWluLi4=","utf-8")).decode("utf-8")).red().bold().show()
			continue
		break
	sql = base64.b64decode(bytes("aW5zZXJ0IGludG8gcGFzcyAoZW5jKSB2YWx1ZXMgKD8p","utf-8")).decode("utf-8")
	enc = (pbkdf2_sha256.hash(p),)
	cur.execute(sql,enc)
	printer.text(' Account Created Successfully ').blanks('-').green().bold().center().show()
	con.commit()

def getState(cur):
	if(hasUser(cur)):
		sql = base64.b64decode(bytes("U0VMRUNUIHMgZnJvbSBwYXNz","utf-8")).decode("utf-8")
		cur.execute(sql)
		res=cur.fetchall()
		for r in res:
			return r[0]
	return None

def toggleState(cur):
	if(hasUser(cur)):
		sql = base64.b64decode(bytes("VVBEQVRFIHBhc3MgU0VUIHM9Pw==","utf-8")).decode("utf-8")
		d = ((getState(cur)+1)%2,)
		cur.execute(sql,d)
			
def isUser(cur,p):
	if(hasUser(cur)):
		sql = base64.b64decode(bytes("U0VMRUNUIGVuYyBmcm9tIHBhc3M=","utf-8")).decode("utf-8")
		cur.execute(sql)
		res=cur.fetchall()
		for r in res:
			return pbkdf2_sha256.verify(p,r[0])
	return False

def insert(d,cur):
	sql = base64.b64decode(bytes("aW5zZXJ0IGludG8gZGF0YSB2YWx1ZXMgKD8sPyk=","utf-8")).decode("utf-8")
	cur.executemany(sql,d)

def hasValue(cur,v):
	sql = base64.b64decode(bytes("U0VMRUNUICogZnJvbSBkYXRhIHdoZXJlIGhpZD0/","utf-8")).decode("utf-8")
	d=(v,)
	cur.execute(sql,d)
	res=cur.fetchall()
	return len(res)!=0

def getOg(cur,v):
	sql = base64.b64decode(bytes("U0VMRUNUIG9nIGZyb20gZGF0YSB3aGVyZSBoaWQ9Pw==","utf-8")).decode("utf-8")
	d=(base64.b64encode(bytes(v,"utf-8")).decode("utf-8"),)
	cur.execute(sql,d)
	res=cur.fetchall()
	for r in res:
			return base64.b64decode(bytes(r[0],"utf-8")).decode("utf-8")
	return None

def deleteData(cur):
	sql = base64.b64decode(bytes("ZGVsZXRlIGZyb20gZGF0YQ==","utf-8")).decode("utf-8")
	cur.execute(sql)


def main():
	if(not os.path.isdir('.misc')):
		os.mkdir('.misc')
	con=init(db)
	if con != None:
		printer.text(base64.b64decode(bytes("SGkgdGhlcmUhIQ==","utf-8")).decode("utf-8")).bold().center().show()
		cur = con.cursor()

		if(not hasUser(cur)):
			createUser(con)
		printer.text('Menu').bold().blanks('-').center().show()
		if(getState(cur)==0):
			
			print(printer.getColored(' [',printer.colors['YELLOW'])+"1"+printer.getColored(']',printer.colors['YELLOW'])+" Lock the files")
			print(printer.getColored(' [',printer.colors['YELLOW'])+"any other key"+printer.getColored(']',printer.colors['YELLOW'])+" Quit")
			printer.center().blanks('-').show()
			ch = input(' Enter your choice:')
			if(ch=="1"):
				p = getpass(printer.getColored(base64.b64decode(bytes("RW50ZXIgeW91ciBwYXNzd29yZDo=","utf-8")).decode("utf-8"),printer.colors['BOLD']))
				if(isUser(cur,p)):
					fil = [f for f in listdir() if os.path.isfile(f)]
					d=[]
					for i in tqdm (range (len(fil)), desc="Locking...",unit="file"): 
						f = fil[i]
						if(f!='storage.db'): 
							new = ''.join(random.choices(string.ascii_uppercase+string.digits+string.ascii_lowercase,k=10))+str(i)+ext[i%4]
							d.append((base64.b64encode(bytes(f,"utf-8")).decode("utf-8"),base64.b64encode(bytes(new,"utf-8")).decode("utf-8")))
							os.rename(f,new)
						
					insert(d,cur)

					toggleState(cur)
					con.commit()
					printer.text(base64.b64decode(bytes("RG9uZTop","utf-8")).decode("utf-8")).green().bold().center().show()
				else:
					printer.text(base64.b64decode(bytes("SW5jb3JyZWN0IHBhc3N3b3JkISE=","utf-8")).decode("utf-8")).red().bold().center().show()
		else:
			print(printer.getColored(' [',printer.colors['YELLOW'])+"1"+printer.getColored(']',printer.colors['YELLOW'])+" Unlock the files")
			print(printer.getColored(' [',printer.colors['YELLOW'])+"any other key"+printer.getColored(']',printer.colors['YELLOW'])+" Quit")
			printer.center().blanks('-').show()
			ch = input(printer.getColored(' Enter your choice:',printer.colors['BOLD']))
			if(ch=="1"):
				p = getpass(printer.getColored(base64.b64decode(bytes("RW50ZXIgeW91ciBwYXNzd29yZDo=","utf-8")).decode("utf-8"),printer.colors['BOLD']))
				if(isUser(cur,p)):
					fil = [f for f in listdir() if os.path.isfile(f)]
					
					for i in tqdm (range (len(fil)), desc="Unlocking...",unit="file"):
						f=fil[i]
						og=getOg(cur,f)
						if(og!=None):
							os.rename(f,og)
						con.commit()
					deleteData(cur)
					toggleState(cur)
					printer.text(base64.b64decode(bytes("RG9uZTop","utf-8")).decode("utf-8")).green().bold().center().show()
				else:
					printer.text(base64.b64decode(bytes("SW5jb3JyZWN0IHBhc3N3b3JkISE=","utf-8")).decode("utf-8")).red().bold().center().show()
		con.commit()
		con.close()
		printer.text(base64.b64decode(bytes("QnllISE=","utf-8")).decode("utf-8")).bold().center().show()