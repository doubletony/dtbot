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

# Access Token for the client
C_K = ''
C_S = ''

# Access Token for the user
A_T_K = ''
A_T_S = ''

# Hmm, it is kind of conflicts of interests.
blocked = ['doubletony']

# "的 一 是 了 我 不 人 在 他 有 这 个 上 们 来 到 时 大 地 为 子 中 你 说 
# 生 国 年 着 就 那 和 要 她 出 也 得 里 后 自 以 会 家 可 下 而 过 天 去
# 能 对 小 多 然 于 心 学 么 之 都 好 看 起 发 当 没 成 只 如 事 把 还 用
# 第 样 道 想 作 种 开 美 总 从 无 情 己 面 最 女 但 现 前 些 所 同 日 手
# 又 行 意 动 方 期 它 头 经 长 儿 回 位 分 爱 老 因 很 给 名 法 间 斯 知
# 世 什 两 次 使 身 者 被 高 已 亲 其 进 此 话 常 与 活 正 感"
# The most commonly used Chinese Characters. It should cover 60%
# text.
ch_chars = [
    '\xe7\x9a\x84',
    '\xe4\xb8\x80',
    '\xe6\x98\xaf',
    '\xe4\xba\x86',
    '\xe6\x88\x91',
    '\xe4\xb8\x8d',
    '\xe4\xba\xba',
    '\xe5\x9c\xa8',
    '\xe4\xbb\x96',
    '\xe6\x9c\x89',
    '\xe8\xbf\x99',
    '\xe4\xb8\xaa',
    '\xe4\xb8\x8a',
    '\xe4\xbb\xac',
    '\xe6\x9d\xa5',
    '\xe5\x88\xb0',
    '\xe6\x97\xb6',
    '\xe5\xa4\xa7',
    '\xe5\x9c\xb0',
    '\xe4\xb8\xba',
    '\xe5\xad\x90',
    '\xe4\xb8\xad',
    '\xe4\xbd\xa0',
    '\xe8\xaf\xb4',
    '\xe7\x94\x9f',
    '\xe5\x9b\xbd',
    '\xe5\xb9\xb4',
    '\xe7\x9d\x80',
    '\xe5\xb0\xb1',
    '\xe9\x82\xa3',
    '\xe5\x92\x8c',
    '\xe8\xa6\x81',
    '\xe5\xa5\xb9',
    '\xe5\x87\xba',
    '\xe4\xb9\x9f',
    '\xe5\xbe\x97',
    '\xe9\x87\x8c',
    '\xe5\x90\x8e',
    '\xe8\x87\xaa',
    '\xe4\xbb\xa5',
    '\xe4\xbc\x9a',
    '\xe5\xae\xb6',
    '\xe5\x8f\xaf',
    '\xe4\xb8\x8b',
    '\xe8\x80\x8c',
    '\xe8\xbf\x87',
    '\xe5\xa4\xa9',
    '\xe5\x8e\xbb',
    '\xe8\x83\xbd',
    '\xe5\xaf\xb9',
    '\xe5\xb0\x8f',
    '\xe5\xa4\x9a',
    '\xe7\x84\xb6',
    '\xe4\xba\x8e',
    '\xe5\xbf\x83',
    '\xe5\xad\xa6',
    '\xe4\xb9\x88',
    '\xe4\xb9\x8b',
    '\xe9\x83\xbd',
    '\xe5\xa5\xbd',
    '\xe7\x9c\x8b',
    '\xe8\xb5\xb7',
    '\xe5\x8f\x91',
    '\xe5\xbd\x93',
    '\xe6\xb2\xa1',
    '\xe6\x88\x90',
    '\xe5\x8f\xaa',
    '\xe5\xa6\x82',
    '\xe4\xba\x8b',
    '\xe6\x8a\x8a',
    '\xe8\xbf\x98',
    '\xe7\x94\xa8',
    '\xe7\xac\xac',
    '\xe6\xa0\xb7',
    '\xe9\x81\x93',
    '\xe6\x83\xb3',
    '\xe4\xbd\x9c',
    '\xe7\xa7\x8d',
    '\xe5\xbc\x80',
    '\xe7\xbe\x8e',
    '\xe6\x80\xbb',
    '\xe4\xbb\x8e',
    '\xe6\x97\xa0',
    '\xe6\x83\x85',
    '\xe5\xb7\xb1',
    '\xe9\x9d\xa2',
    '\xe6\x9c\x80',
    '\xe5\xa5\xb3',
    '\xe4\xbd\x86',
    '\xe7\x8e\xb0',
    '\xe5\x89\x8d',
    '\xe4\xba\x9b',
    '\xe6\x89\x80',
    '\xe5\x90\x8c',
    '\xe6\x97\xa5',
    '\xe6\x89\x8b',
    '\xe5\x8f\x88',
    '\xe8\xa1\x8c',
    '\xe6\x84\x8f',
    '\xe5\x8a\xa8',
    '\xe6\x96\xb9',
    '\xe6\x9c\x9f',
    '\xe5\xae\x83',
    '\xe5\xa4\xb4',
    '\xe7\xbb\x8f',
    '\xe9\x95\xbf',
    '\xe5\x84\xbf',
    '\xe5\x9b\x9e',
    '\xe4\xbd\x8d',
    '\xe5\x88\x86',
    '\xe7\x88\xb1',
    '\xe8\x80\x81',
    '\xe5\x9b\xa0',
    '\xe5\xbe\x88',
    '\xe7\xbb\x99',
    '\xe5\x90\x8d',
    '\xe6\xb3\x95',
    '\xe9\x97\xb4',
    '\xe6\x96\xaf',
    '\xe7\x9f\xa5',
    '\xe4\xb8\x96',
    '\xe4\xbb\x80',
    '\xe4\xb8\xa4',
    '\xe6\xac\xa1',
    '\xe4\xbd\xbf',
    '\xe8\xba\xab',
    '\xe8\x80\x85',
    '\xe8\xa2\xab',
    '\xe9\xab\x98',
    '\xe5\xb7\xb2',
    '\xe4\xba\xb2',
    '\xe5\x85\xb6',
    '\xe8\xbf\x9b',
    '\xe6\xad\xa4',
    '\xe8\xaf\x9d',
    '\xe5\xb8\xb8',
    '\xe4\xb8\x8e',
    '\xe6\xb4\xbb',
    '\xe6\xad\xa3',
    '\xe6\x84\x9f',
    ]

filter_word = [
'China',
'china',
'fuck',
'shit',
'http',
'https',
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

# A good message is in Chinese and without any link.
# The bot should spam the followers with any tweets
# containing promotion information.

def is_good_message(s, f_words=[]):
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
        	return False
    for ch in ch_chars:
    	# Just need one chinese character.
        if ch in s:
        	return True
    return False

def get_block_list():
	bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())
	gcs_file = gcs.open('/'+bucket_name + '/block_list.txt')
	content = gcs_file.read()
	gcs_file.close()
	return blocked + content.split()

def update_block_list(username):
	bucket_name = os.environ.get('BUCKET_NAME',
                               app_identity.get_default_gcs_bucket_name())
	gcs_file = gcs.open('/'+bucket_name + '/block_list.txt')
	content = gcs_file.read()
	gcs_file.close()
	gcs_file = gcs.open('/'+bucket_name + '/block_list.txt', 'w', content_type='text/plain')
	if len(content) > 1000:
		gcs_file.write(username)
		gcs_file.close()
		return

	gcs_file.write(content + ' ' + username)
	gcs_file.close()

def do_retweet():
	tweepyAuth = tweepy.OAuthHandler(C_K, C_S)
	tweepyAuth.set_access_token(A_T_K, A_T_S)
	tweepyAPI = tweepy.API(tweepyAuth)

	status = tweepyAPI.home_timeline(count = 200)

	posted = False
	blocked = get_block_list()
	for s in status:
		if posted:
			break;
		owner_sn = str(s.user.screen_name)
		if owner_sn in blocked:
			continue
		if len(s.text) > 30 and no_screen_name(s.text) and is_good_message(s.text, filter_word):
			tweepyAPI.retweet(s.id)
			posted = True
			update_block_list(owner_sn)
			return s.text


                    
