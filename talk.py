# encoding: utf-8
from random import *
import jieba
import jieba.analyse
jieba.set_dictionary("dict.txt.big.txt")
tagsTest = jieba.analyse.extract_tags('測試',1)
# 為了先讀取jieba，後面對話不會中斷...

x = 0

# 抓到名字
name = input(">>> 請輸入你的名字: ")
print(">>> 小白: 哈囉"+name+"~你今天有什麼煩惱嗎？")

# 選擇不同的後段話（chooseNumber是有幾個選項）
def choose():
	chooseNumber = 10
	randomNumber = random()
	if randomNumber<(1/chooseNumber):
		return '我懂，沒事的'
	elif randomNumber<(2/chooseNumber):
		return '你已經是個很棒的人了，只是遇到了挫折'
	elif randomNumber<(3/chooseNumber):
		return '時間總會過去，遙想我們曾經幻想的未來，一切走的都不容易，對吧'
	elif randomNumber<(4/chooseNumber):
		return '若這時候放棄了，你還值得去跟世界搏鬥嗎'
	elif randomNumber<(5/chooseNumber):
		return '忘了所有的人事物吧，就從腳下這一步，重新開始，你早就注定與他人走條不同的路'
	elif randomNumber<(6/chooseNumber):
		return '做個勇敢的人，享受痛苦，享受經驗，這一切都是個遊戲'
	elif randomNumber<(7/chooseNumber):
		return '我知道你的意思，你一定很難受對吧'
	elif randomNumber<(8/chooseNumber):
		return '有我陪著，雖然這沒什麼用，但...我相信你可以做到的，你是無所不能的！'
	elif randomNumber<(9/chooseNumber):
		return '拜託，別這麼說...'
	elif randomNumber<(10/chooseNumber):
		return '是啊，你說的沒錯。'

# 選擇是否要後段話
def WhetherChoose():
	chooseNumber = 2
	randomNumber = random()
	if randomNumber<(1/chooseNumber):
		return 0
	elif randomNumber<(2/chooseNumber):
		return 1
	# elif randomNumber<(3/chooseNumber):
	# 	return 1

# 決定前段開頭話，融合x(也就是之後jieba分詞的最關鍵詞)
def randomOpen(x):
	chooseNumber = 10
	randomNumber = random()
	if randomNumber<(1/chooseNumber):
		return '恩...'+x+'...'
	elif randomNumber<(2/chooseNumber):
		return '什麼'+x+'?'
	elif randomNumber<(3/chooseNumber):
		return '不要'+x
	elif randomNumber<(4/chooseNumber):
		return '我懂...'+x
	elif randomNumber<(5/chooseNumber):
		return x+'><'
	elif randomNumber<(6/chooseNumber):
		return '什麼'+x+'?'
	elif randomNumber<(7/chooseNumber):
		return '我就知道你要說的是'+x
	elif randomNumber<(8/chooseNumber):
		return 'oh God!'+x+'!'
	elif randomNumber<(9/chooseNumber):
		return '恩....'
	elif randomNumber<(10/chooseNumber):
		return '了解了...'

# 抓到輸入的對話，並抓取關鍵詞，然後使用前段話，在隨機產生是否要後端化
def rawInputTest():
    x = input(">>> "+name+": ")
    keyword = useJebia(x)
    print (">>> 小白: "+randomOpen(keyword))
    if WhetherChoose()==0:
   		print(">>> 小白: "+choose())

# 這是抓取關鍵詞（使用jieba的程式碼)
def useJebia(talk):
	tags = jieba.analyse.extract_tags(talk,1)
	return (tags[0])

# 這部分是一直能夠對話的原因（一直執行rawInputTest()）
while (True):
    rawInputTest()