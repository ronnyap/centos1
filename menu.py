#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
		
                (             )     *                      )      *             )         
 (  (           )\ )   (   ( /(   (  `           *   )  ( /(    (  `         ( /(         
 )\))(   ' (   (()/(   )\  )\())  )\))(   (    ` )  /(  )\())   )\))(   (    )\())    (   
((_)()\ )  )\   /(_))(((_)((_)\  ((_)()\  )\    ( )(_))((_)\   ((_)()\  )\  ((_)\     )\  
_(())\_)()((_) (_))  )\___  ((_) (_()((_)((_)  (_(_())   ((_)  (_()((_)((_)  _((_) _ ((_) 
\ \((_)/ /| __|| |  ((/ __|/ _ \ |  \/  || __| |_   _|  / _ \  |  \/  || __|| \| || | | | 
 \ \/\/ / | _| | |__ | (__| (_) || |\/| || _|    | |   | (_) | | |\/| || _| | .` || |_| | 
  \_/\_/  |___||____| \___|\___/ |_|  |_||___|   |_|    \___/  |_|  |_||___||_|\_| \___/  
  
\033[1;91m[W] Do not sell this script .\033[1;m
		''')
		def inicio1():
			while True:
				print ('''
1) User Login Dropbear 
2) Add User
3) Expired User List
4) Delete Expired User
5) Exit
			''')

				opcion0 = raw_input("\033[1;36mchoose > \033[1;m")
					print ('''

                                        ''')
				        repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("sudo sh userlogin.sh 443")
					elif repo == "2":
						cmd1 = os.system("sudo usernew")
					elif repo == "3":
						cmd1 = os.system("cat expireduser.txt")
					elif repo == "4":
						cmd1 = os.system("sh autoexpire.sh")
					elif repo == "5":
						inicio1()

	inicio1()
	except KeyboardInterrupt:
		print ("Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
