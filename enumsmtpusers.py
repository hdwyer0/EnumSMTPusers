import smtplib
import sys

def smtp_vrfy(server, port, wordlist, mode):
	try:
		# read the usernames from the wordlist
		with open(wordlist, 'r') as file:
			usernames = file.read().splitlines()
        
		print(f"Loaded {len(usernames)} usernames from {wordlist}")
		valid_users = []
        
		if mode == "fast":
			# connect to the SMTP server
			smtp = smtplib.SMTP(server, port)
			smtp.ehlo()  # initiate the SMTP handshake
			print(f"Connected to {server}:{port}")
        
		print("Starting...")
		n=0
		# test each username
		for username in usernames:
			n+=1
			try:
				if mode == "reconnect":
					# connect to the SMTP server
					smtp = smtplib.SMTP(server, port)
					smtp.ehlo()  # initiate the SMTP handshake
                
				print(f"Testing: {username}")
				print(f"{n}/{len(usernames)}: {int(100*n/len(usernames))}%")
				response = smtp.verify(username)
				if response[0] == 250 or response[0] == 252:  # 250 and 252 indicate valid responses
					print(f"Valid user found: {username}")
					valid_users.append(username)

				if mode == "reconnect":
					# disconnect from the server after trying username
					smtp.quit()
            
			except Exception as e:
				print(f"Error testing {username}: {e}")
                
		if mode == "fast":
			# disconnect from the server after exhausting the list
			smtp.quit()
        
		# output the valid usernames
		print("\nValid usernames:")
		for user in valid_users:
			print(user)
    
	except Exception as e:
		print(f"Error: {e}")

def print_usage():
	# print usage and exit the script
	print("\nUsage: python3 enumsmtpusers.py <server> <port> <wordlist> <mode>")
	print("\nMode: slow (reconnects to server for every user)")
	print("Mode: fast (enumerates list in one session)")
	print("\nExample: python3 smtp-user-enum-slow.py 10.10.10.10 25 /path/to/wordlist.txt fast")
	sys.exit(1)

if __name__ == "__main__":
	# check if all arguments are provided
	if len(sys.argv) != 5:
		print("Error: Missing arguments.")
		print_usage()
    
	# define arguments
	server = sys.argv[1]
	try:
		port = int(sys.argv[2])
	except ValueError:
		print("Error: Port must be an integer.")
		print_usage()
	wordlist = sys.argv[3]
	if sys.argv[4] != "fast" and sys.argv[4] != "slow":
		print("Error: Mode not specified: 'slow' or 'fast'.")
		print_usage()
	mode = sys.argv[4]

	# run the script
	smtp_vrfy(server, port, wordlist, mode)
