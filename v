try:
	#
	import base64,codecs,marshal,struct,socket,pickle
	from collections import *
	import functools
	import kivy 

except ImportError as e:
	print('[!] Module %s ---....'%str(e).split(' ')[-1])
	exit(1)





class start(object):
	"""this is just testing class"""
	def __init__(self, arg):
		self.arg=arg
		pass
	def encrypt(self,message):
		message_bytes = message.encode('u8')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('u8')
		return(base64_message)# base64en
	def decrypt(self,base64_message):
		base64_bytes = base64_message.encode('ascii')
		message_bytes = base64.b64decode(base64_bytes)
		message = message_bytes.decode('ascii')
		return(message)#base64 d
	def count(self):

		d=[1,2,3,4,5,6,7,8,9,10,11,12,13,]

		c=Counter(d)
		da=c.items()
		lengs=len(da)
		return lengs


		#d=list(c.elements())
		#print(d) #give 13 
	def give_string(self,arg):
		a=namedtuple("naser_project","name,job")
		s=a(arg,"print_strings")
		d=s[0];return(d) #give you string
	def return_number(self,arg):
		x=arg
		#x=[2,2,0,1,2,3,11]
		y=1
		#print(lambda x,y: x+y,x)
		result=functools.reduce(lambda i,y:y+i,x)
		print(result)#give you number
	def rot13(self,arg):
		start = '\x72\x6f\x74\x31\x33'
		mand=codecs.encode(arg,start)
		return(mand) #give rot13
	def compils(self,arg):	
		g=compile(arg,"","exec")
		exec(g)
	def struck(self,arg,num):
		
		de=struct.pack(arg,num)
		de2=struct.unpack(arg,de)
		return (de)#code='b'print(fox.struck(code,12))
	def socks_long(self,arg):
		
		long=socket.htonl(arg)
		return(long)
	def socks_decryptlong(self,arg):
		#
		long2=socket.ntohl(arg)
		return(long2)
	def socks_short(self,arg):
		#
		short=socket.htons(arg)
		return(short)
	def socks_decrypt_short(self,arg):
		short2=socket.ntohs(arg)
		print(short2)
	def picles(self,arg):
		dec=pickle.dumps(arg)
		decs=pickle.loads(arg)
		print(decs)
	def hex(self,arg):
		h = ''.join([hex(ord(i)) for i in arg])
		h=h.replace('0x','\\x')
		return(h)
	def hex_to_url(self,arg):
		h = ''.join([hex(ord(i)) for i in arg])
		h=h.replace('0x','%')
		return(h)
	def ip_split(self,arg):

		request=arg
		di, dp = request.split(':')[0].split()[-1], request.split(':')[1].split()[0]
		return[di,dp]






code='o'

fox=start(code)
print(fox.hex_to_url(code))
#code='b'print(fox.struck(code,12))
#fox.count() make 13

       







     




     
