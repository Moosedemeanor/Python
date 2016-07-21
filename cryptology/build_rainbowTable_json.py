Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> alpha='abcdefghijklmnopqrstuvwxyz'
>>> fname = "C:\Users\SESA198806\Desktop\words.txt"
>>> with open(fname) as f:
	content = [x.strip('\n') for x in f.readlines()]

	
>>> f.close()
>>> content[:50]
['&c', "'d", "'em", "'ll", "'m", "'mid", "'midst", "'mongst", "'prentice", "'re", "'s", "'sblood", "'sbodikins", "'sdeath", "'sfoot", "'sheart", "'shun", "'slid", "'slife", "'slight", "'snails", "'strewth", "'t", "'til", "'tis", "'twas", "'tween", "'twere", "'twill", "'twixt", "'twould", "'un", "'ve", '1080', '10th', '1st', '2', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', 'a', "a'", "a's", 'a/c', 'a1']
>>> dic = {}
>>> for letter in alpha:
	dic[letter]=[]

	
>>> print dic
{'a': [], 'c': [], 'b': [], 'e': [], 'd': [], 'g': [], 'f': [], 'i': [], 'h': [], 'k': [], 'j': [], 'm': [], 'l': [], 'o': [], 'n': [], 'q': [], 'p': [], 's': [], 'r': [], 'u': [], 't': [], 'w': [], 'v': [], 'y': [], 'x': [], 'z': []}
>>> dic['other']=[]
>>> dic
{'other': [], 'a': [], 'c': [], 'b': [], 'e': [], 'd': [], 'g': [], 'f': [], 'i': [], 'h': [], 'k': [], 'j': [], 'm': [], 'l': [], 'o': [], 'n': [], 'q': [], 'p': [], 's': [], 'r': [], 'u': [], 't': [], 'w': [], 'v': [], 'y': [], 'x': [], 'z': []}
>>> for word in content:
	try:
		if str(word)[0].isalpha():
			dic[str(word)[0].lower()].append(str(word).lower())
		else:
			dic['other'].append(str(word).lower())
	except:
		continue

	
>>> len(dic)
27
>>> len(dic['a'])
23801
>>> len(dic['other'])
45
>>> wordcount = 0
>>> for key in dic:
	wordcount+=len(dic[key])

	
>>> wordcount
354984
>>> import json
>>> savepath = "C:\Users\SESA198806\Desktop\words.json"
>>> with open(savepath, 'w') as fp:
	json.dump(dic, fp)

	
>>> fp.close()
>>> with open(savepath, 'r') as fp:
	reread_dict = json.load(fp)

	
>>> fp.close()
>>> len(reread_dict)
27
>>> len(reread_dict['a'])
23801
>>> wordcount = 0
>>> for key in dic:
	wordcount+=len(reread_dict[key])

	
>>> wordcount
354984
>>> 
