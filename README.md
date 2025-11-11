# EnumSMTPusers
A python tool to enumerate usernames using the SMTP protocol



### Usage
**install:**

~~~
git clone https://github.com/hdwyer0/EnumSMTPusers
~~~

**run:**

~~~
python3 enumsmtpusers.py <server> <port> <wordlist> <mode>
~~~



### Modes
  **fast** (enumerates list in one session)
   - sometimes the session expires or disconnects and this mode will fail to test the whole worlist

  **slow** (reconnects to server for every user)
   - ideal for reliably enumerating users when fast mode fails



### Example
~~~
python3 enumsmtpusers.py 10.10.10.10 25 /path/to/wordlist.txt fast
~~~


Recomended wordlist:
https://github.com/danielmiessler/SecLists/blob/master/Usernames/xato-net-10-million-usernames.txt
