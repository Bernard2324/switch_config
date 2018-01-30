#!/usr/bin/env python

import netmiko
import connection

class configInterface(connection.connectNet):
	
	def __init__(self, thost):
		super(configInterface, self).__init__(host=thost)
		
	def escalate(self):
		if not self.connection.check_enable_mode():
			try:
				self.connection.enable()
			except:
				print "Failed to Enter enable Mode!\n"
		else:
			pass
	
	def getConfigure(self):
		""" Make Sure connection is in configuration mode; if not, move to priv-exec mode """
		if not self.connection.check_config_mode():
			try:
				self.connection.config_mode()
			except:
				print "Failed To Enter Configuration Terminal Mode!\n"
		else:
			pass
	
	def commands(self, command_set):
		""" Execute All commands listend in 'command_set'.  Record start/end time for elapsed time """
		
		results = self.connection.send_config_set(command_set)
	
	def dataconfigset(self, interface, maxi):
		interface_cmd = "interface GigabitEthernet{}".format(interface)
		config_set = [
			interface_cmd, 'switchport', 'switchport mode access', 'switchport port-security maximum {}'.format(maxi),
			'switchport port-security violation restrict', 'switchport port-security mac-address sticky',
			'switchport port-security', 'spanning-tree bpduguard enable', 'spanning-tree portfast',
			'switchport access vlan 1', 'switchport voice vlan 111', 'no shutdown'
		]
		return config_set
		
	def clearall(self, interface):
		config_set = [
			'clear port-security all interface GigabitEthernet{}'.format(interface)
		]
		return config_set
	
	def end(self):
		""" Call netmiko method cleanup() for clean close of all sessions and connections """
		self.connection.cleanup()
		print "[*] Connection Closed"
		
