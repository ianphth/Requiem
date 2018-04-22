init python:
    class Choice(store.object):

        acceptable_attribute = {'self', 'MainName', 'AltName', 'LoopTime', 'Unlocked'}
        # def__init__(self, MainName, AltName, LoopTime, Unlocked):
        #    self.MainName = "Main"
        #    self.AltName = "Alt"
        #    self.LoopTime = 0
        #    self.Unlocked = False
        def __setattr__(self, name, value):
            if name not in type(self).acceptable_attribute:
                raise Exception('Not allow this variable')
            super(store.object, self).__setattr__(name, value)

define p = Character('Nameless One', color="#c8ffc8")    
image black = "#000"
image white = "#FFF"

# 遊戲從這裡開始。
label start:

$ Choice1 = Choice()
$ Choice1.MainName = "忍受"
$ Choice1.AltName = ")(*&%*(#)@"
$ Choice1.LoopTime = 0
$ Choice1.Unlocked = False

label begin:

hide white
show black
with dissolve
if Choice1.LoopTime > 0:
    "這是第[Choice1.LoopTime]次了呢。"

if True:
    "我聽見了。"
    "在那個炙熱的火海中。"
    "雖然眼前的世界一片扭曲，如同幻覺一般，任何事物都無法被清楚的分辨。"
    "雖然火焰燃燒的聲音震耳欲聾，如同惡魔的交響曲般，宣告著將入地獄的命運。"
    p "啊...啊啊...哈哈哈"
    "我倒在地上，任火焰侵蝕我的身體，用最後的力氣呻吟了一番，並發自內心的笑了幾聲。"
    p "這種報應實在太適合我了..."
    "身體的平靜異常到腦內無法理解，完全沒有在火場中大腦所散發的反射動作。"
    "但只有那個聲音如同耳鳴一般的直達腦內，不曾間斷。"
    "比起燒盡我皮膚每一吋、且苦痛難耐的灼傷，這個聲音更是如同尖刺般刺穿我內心的針，折磨著我一點一滴的生命。"
    
    $ Choice1.LoopTime += 1
if Choice1.Unlocked:
    jump Menu1_2
else:
    jump Menu1_1
       
label Menu1_1:
menu:
    
    "我選擇..."
    
    "[Choice1.MainName]":
        jump unveil
        
    "遺忘":
        jump loop
    
label Menu1_2:
menu:
    
    "我決定..."
    
    "[Choice1.AltName]":
        jump passed
        
    "遺忘":
        jump loop
    
label unveil:
    
    "疼痛慢慢地消失，眼前的世界也不斷變暗，一切都在逝去。"
    "唯獨耳中的聲音源源不絕不曾退散..."

    $ Choice1.Unlocked = True
    jump begin
    
label loop:

    show white
    with dissolve
    "反正忘記一切肯定就能有效逃避了吧。"
    "但我真的忘的了嗎...這份痛楚。"
    jump begin

label passed:

    "BHSDFHPEOIQTEPOHOSDGHSDOGHJQO"

    $ Choice1.LoopTime = 0
    return
