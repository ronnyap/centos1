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
4)Delete Expired User

			''')

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while opcion0 == "1":
					print ('''
1) User Login Dropbear 
2) Add User
3) Expired User List
4)Delete Expired User


                                        ''')
				        repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m"
							

			''')

				opcion0 = raw_input("\033[1;36mchoose > \033[1;m")
			
				while opcion
							if opcion2 == "1":
								cmd = os.system("sudo sh userlogin.sh 443")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("sudo usernew")
								print (" ")
                elif opcion2 == "3":
								cmd = os.system("sudo cat expireduser.txt")
                print (" ")
							elif opcion2 == "4":
								cmd = os.system("sudo sh autoexpire.sh")
                else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")
                while opcion1 == "5" :
							print ('''
								inicio1()
	elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Thank You")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
