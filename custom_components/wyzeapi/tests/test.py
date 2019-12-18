from .secrets import *
from ..wyzeapi.wyzeapi_exceptions import *
from ..wyzeapi.wyzeapi import WyzeApi

def TestAccessTokenError():
	print("Test: TestAccessTokenError")

	wyze = WyzeApi(username, password, no_save=True)

	bulbs = wyze.list_bulbs()
	# Kill access token

	wyze._access_token = "Killed"

	bulbs[0].turn_off()

	print("SUCCESS")

def TestBadPassword():
	print("Test: TestBadPassword")

	try:
		wyze = WyzeApi(username, "BadPassword", no_save=True)
	except WyzeApiError:
		print("SUCCESS")
		return

	print("ERROR")

def TestBulbs():
	print("Test: TestBulbs")

	wyze = WyzeApi(username, password, no_save=True)

	bulbs = wyze.list_bulbs()

	for bulb in bulbs:
		bulb.turn_off()
		bulb.turn_on()
		bulb.update()

	print("SUCCESS")

def TestSwitches():
	print("Test: TestSwitches")

	wyze = WyzeApi(username, password, no_save=True)

	switches = wyze.list_switches()

	for switch in switches:
		switch.turn_off()
		switch.turn_on()
		switch.update()

	print("SUCCESS")

if __name__ == '__main__':
	TestAccessTokenError()
	TestBadPassword()
	TestBulbs()
	TestSwitches()

