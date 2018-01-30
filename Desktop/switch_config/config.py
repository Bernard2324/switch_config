#!/usr/bin/env python

from Crypto.Cipher import DES

class configuration(object):
	
	def __init__(self, address):
		self.device_type = 'cisco_ios'
		self.address = address
		if not isinstance(address, str):
			address = str(address)
		if not any(k in ['11', '12', '13'] for k in [address]):
			raise AttributeError("You Must Enter 11 or 12!")
			
		ip_hosts = {
			'11': '192.168.100.100',
			'12': '192.168.100.101',
			'13': '192.168.100.204'
		}
		self.addr = ip_hosts.get(address)
		self.user = 'admin'
		self.key = str(raw_input("Please Enter Encryption Key: \n").strip())
		self.ciphtext = self.encryption(self.key)
		self.password = "".join([
			chr(x-1) for x in map(ord, [i for i in self.ciphtext])
		])
		
		self.secret = 'secret'
		
	
	def encryption(self, key):
		if not isinstance(key, str):
			key = str(key)
		object = DES.new(key, DES.MODE_ECB)
		cipher = '^\xb6/\xa2B\x9a\xb8\xfe'
		
		return object.decrypt(cipher)
