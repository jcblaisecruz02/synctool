import argparse
import os
import time

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--folder', type=str, required=True, help='Folder to watch.')
	parser.add_argument('--sleep', type=int, default=1, help='Sleep timer in seconds.')
	parser.add_argument('--command', type=str, required=True, help='Command to run when files have changed.')

	args = parser.parse_args()
	print('Watching', args.folder)

	# Get initial list of contents
	contents = os.listdir(args.folder)
	while(True):
		ncontents = os.listdir(args.folder)
		if contents != ncontents:
			print("Folder contents have changed!")
			print("Added: " + str(set(ncontents) - set(contents)))
			contents = ncontents
			os.system(args.command)
			print("Command executed. Resume watching.")
			
		time.sleep(args.sleep)

if __name__ == '__main__':
	main()
