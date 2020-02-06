# Logins #

Learn sql, python, and Flask all in one small project.

Bugs:
- [x] Stupid invalid salt error, something to do with encoding , but I made everything utf-8... (problem was ``checkpw`` on a non-hashed db)
- [x] Copies of same entires are being stored. This means verifying users it total crap. (Fixed with new implementation)

Todo:
- [ ] SESSIONS (w/ logout option)
- [ ] Need alerts for failed login and registers
- [ ] Verify password by retyping it (like modern websites)
- [ ] Need new pages to redirect to when successful register/login (successful register -> login w/ alert & login -> new page w/ name at top)
- [x] Separate Logins and Register front-end 
- [ ] Ensure the refresh or back thing doesn't add logins again
- [x] Make sure user can't enter empty usernames and passwords
- [x] Encrypt username and passwords before storing into database
- [x] Make Exists check work with encryption
- [x] Verify logins and registering all works dandy with encryption
- [ ] Change name to simple\_login


Goals:
- [ ] What am I doing? Perform the database design pattern on this!!!
- [x] Build simple front-end website that registers and signs in users
- [x] Encrypt user passwords and usernames
- [x] Store encrypted usernames and passwords into database
- [x] Implement a simple password and username policy
- [ ] Have a log system setup
- [ ] Attempt to learn more about secure methologies for databases
- [ ] Prevent SQL injections!
- [ ] Have sessions
- [ ] Store unique user information w/ unique web pages

Reminders:
- [ ] Add an install script

Prevent CSRF? simply resubmitting forms http://flask.pocoo.org/docs/0.12/quickstart/#sessions
