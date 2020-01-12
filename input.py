''' This block is used to input characters from terminal '''
from __future__ import print_function
from getch import _getChUnix as getChar
import signal

class AlarmException(Exception):
    '''This class executes the alarmexception.'''
    pass

def getpress():
	''' moves Mandalorian'''
	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

	def user_input(timeout=0.15):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)

		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''

	return user_input()
