#!/usr/bin/env python

import getpass
from netmiko import ConnectHandler
import config

class connectNet(config.configuration):
	def __init__(self, host=None):
		""" instantiate with parameters needed for successfull connection.  This includes
			device type, ip address, username, password, and secret (*platform dependant).
			Once this information is received, initiate connection with the target host """
		
		if host is None:
			raise AttributeError("Must Provide Host to Connection\n")
		super(connectNet, self).__init__(host)
		
		self.hostObj = {
			'device_type': self.device_type,
			'ip': self.addr,
			'username': self.user,
			'password': self.password,
			'secret': self.secret
		}
		
		self.connection = ConnectHandler(**self.hostObj)
