# created by doubletony
# no right is reserved
# you're responsible for using these codes

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "thirdparty"))

import tweepy
reload(sys)
sys.setdefaultencoding('utf8')
import cloudstorage as gcs
from google.appengine.api import app_identity
blocked = ['doubletony', 'wengyunchao']

filter_word = [
'China',
'china',
'fuck',
'shit',
'gpsed',
'qieke',
'aiww',
'zhiyongxu',
'pic',
'picture',
'img',
'exe'
]

def no_screen_name(text):
    if "@" in text:
        return False
    return True

def msg_filter(s,f_words=[]):
    if "4sq" in s:
        return False
    if "\xe6\x88\x91" in s:
        return False
    if "I am" in s:
        return False
    if "I'm" in s:
        return False
    if '\xe8\x87\xaa\xe7\x94\xb1' in s: #ziyou
        return False
    if '\xe6\xb0\x91\xe4\xb8\xbb' in s: #mingzhu
        return False
    if '\xe5\x85\x9a' in s:
        return False
    for wo in f_words:
        if wo in s:
            if len(wo) > 0:
                return False
    return True

# Access Token for the client
C_K = ''
C_S = ''

# Access Token for the user
A_T_K = ''
A_T_S =''


def get_block_list():
	
	bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())
	gcs_file = gcs.open('/'+bucket_name + '/block_list.txt')
	content = gcs_file.read()
	return blocked + content.split()

def update_block_list(username):
	bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())
	gcs_file = gcs.open('/'+bucket_name + '/block_list.txt')
	content = gcs_file.read()
	gcs_file.close()
	gcs_file = gcs.open('/'+bucket_name + '/block_list.txt', 'w')
	if len(content) > 1000:
		gcs_file.write('');

	gcs_file.write(content + ' ' + username)
	

def do_retweet():
	
	tweepyAuth = tweepy.OAuthHandler(C_K, C_S)
	tweepyAuth.set_access_token(A_T_K, A_T_S)
	tweepyAPI = tweepy.API(tweepyAuth)

	status = tweepyAPI.home_timeline()

	posted = False
	blocked = get_block_list()
	for s in status:
		if posted:
			break;
		owner_sn = str(s.user.screen_name)
		if owner_sn in blocked:
			continue
		if len(s.text) > 30 and no_screen_name(s.text) and msg_filter(s.text, filter_word):
			tweepyAPI.retweet(s.id)
			posted = True
			update_block_list(owner_sn)
			return s.text


                    
