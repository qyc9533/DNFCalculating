from math import *
from PublicReference.base import *

class 大将军主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率,2)

class 大将军技能0(被动技能):
    名称 = '弹夹改装'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['交叉射击','聚合弹','凝固汽油弹','轻火力速射']
    关联技能2 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (10 + self.等级) / 100, 3)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + (2 * self.等级) / 100, 3)

class 大将军技能1(被动技能):
    名称 = '兵器研究'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    冷却关联技能 = ['交叉射击','M18阔剑地雷','C4飞弹','G18冰冻手雷','G35感电手雷','G61重力地雷','G38ARG智能手雷','爆裂弹','聚合弹','重火力支援','镭射狙击','凝固汽油弹','轻火力速射']

    def 加成倍率(self, 武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 物理攻击力倍率(self,武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def 魔法攻击力倍率(self,武器类型):
        return (1.1 + (self.等级 - 10) * 0.02) if self.等级 >= 10 else (1 + self.等级 * 0.01)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 - 0.01 * self.等级, 3)

class 大将军技能2(被动技能):
    名称 = '手雷精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['G35感电手雷','G18冰冻手雷']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.1 * self.等级, 3)


class 大将军技能3(大将军主动技能):
    名称 = 'M18阔剑地雷'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 568.82
    成长 = 64.18
    攻击次数 = 3
    CD = 6.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7


class 大将军技能4(大将军主动技能):
    名称 = 'G35感电手雷'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 462.77
    成长 = 52.23
    CD = 3.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if (self.等级 < 18):
            return 1.0
        else:
            return round(1 + 0.01 * (self.等级-18), 3)

class 大将军技能5(大将军主动技能):
    名称 = '交叉射击'
    脱手 = 0
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1163.62
    成长 = 131.38
    攻击次数 = 3
    脱手 = 0
    技能施放时间 = 0.4
    CD = 8.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7


class 大将军技能6(大将军主动技能):
    名称 = '爆裂弹'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    基础 = 529.5
    成长 = 100.5
    CD = 5.0

class 大将军技能7(大将军主动技能):
    名称 = 'G18冰冻手雷'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 588.8
    成长 = 63.2
    CD = 4.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7


class 大将军技能8(大将军主动技能):
    名称 = '聚合弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7243.23
    成长 = 817.77
    CD = 18.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7

class 大将军技能9(大将军主动技能):
    名称 = 'C4飞弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6331.11
    成长 = 714.89
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.基础 *= 1.23
        self.成长 *= 1.23
        # self.倍率 *= 1.18

class 大将军技能10(大将军主动技能):
    名称 = '凝固汽油弹'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7844.37
    成长 = 885.63
    基础2 = 45.97
    成长2 = 5.03
    攻击次数2 = 15
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.基础 *= 1.31
        self.成长 *= 1.31
        # self.倍率 *= 1.18
        self.攻击次数2 = 0
        self.CD *=0.94


class 大将军技能11(大将军主动技能):
    名称 = '镭射狙击'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 2681.0
    成长 = 303.0
    攻击次数 = 5
    CD = 45.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7
    是否有护石 = 1

    def 装备护石(self):
        self.基础 *= 1.28
        self.成长 *= 1.28
        # self.倍率 *= 1.18


class 大将军技能12(被动技能):
    名称 = '弹药主宰'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['所有']
    关联技能2 = ['爆裂弹']

    def 加成倍率(self, 武器类型):
        return 1.105 + self.等级 * 0.015 if self.等级 > 0 else 1

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.3


class 大将军技能13(大将军主动技能):
    名称 = '黑玫瑰特种战队'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 858.23
    成长 = 371.83
    攻击次数 = 16
    基础2 = 150.83
    成长2 = 66.15
    攻击次数2 = 90
    CD = 145.0

class 大将军技能14(大将军主动技能):
    名称 = 'G61重力地雷'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 5003.05
    成长 = 564.95
    基础2 = 167.19
    成长2 = 18.81
    攻击次数2 = 30
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7
    技能施放时间 = 3

    是否有护石 = 1

    def 装备护石(self):
        self.基础 *= 1.83
        self.成长 *= 1.83
        self.技能施放时间 = 1.5
        self.攻击次数2 = 15
        # self.倍率 *= 1.18

class 大将军技能15(大将军主动技能):
    名称 = '轻火力速射'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 975.75
    成长 = 110.25
    攻击次数 = 17
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 7

    是否有护石 = 1

    def 装备护石(self):
        self.基础2 = self.基础*0.22
        self.成长2 = self.成长*0.22
        self.技能施放时间 = 2
        self.攻击次数2 = 17
        self.CD *=0.95
        # self.倍率 *= 1.18

class 大将军技能16(被动技能):
    名称 = '战地功勋'
    所在等级 = 75
    等级上限 = 30
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)

class 大将军技能17(大将军主动技能):
    名称 = '重火力支援'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 4125.33
    成长 = 465.67
    攻击次数 = 10
    CD = 45.0


class 大将军技能18(大将军主动技能):
    名称 = 'G38ARG智能手雷'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 13127.83
    成长 = 1482.17
    攻击次数 = 1
    基础2 = 3063.17
    成长2 = 345.83
    攻击次数2 = 10
    CD = 40.0

class 大将军技能19(大将军主动技能):
    名称 = '超新星核爆'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 48138.5
    成长 = 14532.5
    基础2 = 1374.75
    成长2 = 415.25
    攻击次数2 = 15
    脱手 = 0
    技能施放时间 = 1
    CD = 180.0

class 大将军技能20(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 大将军技能21(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 大将军技能22(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

大将军技能列表 = []
i = 0
while i >= 0:
    try:
        exec('大将军技能列表.append(大将军技能'+str(i)+'())')
        i += 1
    except:
        i = -1

大将军技能序号 = dict()
for i in range(len(大将军技能列表)):
    大将军技能序号[大将军技能列表[i].名称] = i

大将军一觉序号 = 0
大将军二觉序号 = 0
大将军三觉序号 = 0
for i in 大将军技能列表:
    if i.所在等级 == 50:
        大将军一觉序号 = 大将军技能序号[i.名称]
    if i.所在等级 == 85:
        大将军二觉序号 = 大将军技能序号[i.名称]
    if i.所在等级 == 100:
        大将军三觉序号 = 大将军技能序号[i.名称]

大将军护石选项 = ['无']
for i in 大将军技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        大将军护石选项.append(i.名称)

大将军符文选项 = ['无']
for i in 大将军技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1 and i.名称!='爆裂弹':
        大将军符文选项.append(i.名称)

class 大将军角色属性(角色属性):

    职业名称 = '大将军'

    武器选项 = ['手弩','步枪']
    
    #'物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法百分比','物理百分比']
    
    #默认
    伤害类型 = '魔法百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['智力','力量']

    主BUFF = 1.84
   
    #基础属性(含唤醒)
    基础力量 = 893.0
    基础智力 = 892.0
    
    #适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    #人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13

    远古记忆 = 0
  
    def __init__(self):
        self.技能栏= deepcopy(大将军技能列表)
        self.技能序号= deepcopy(大将军技能序号)

    def 伤害计算(self, x=0):
        self.所有属性强化(self.进图属强)
        # Will添加
        self.CD倍率计算()
        self.加算冷却计算()

        self.被动倍率计算()
        self.伤害指数计算()
        
        # 弹药改良加成1.1
        self.伤害指数 *= 1.1

        技能释放次数 = []
        技能单次伤害 = []
        技能总伤害 = []

        # 技能单次伤害计算
        for i in self.技能栏:
            if i.是否主动 == 1:
                技能单次伤害.append(i.等效百分比(self.武器类型) * self.伤害指数 * i.被动倍率)
            else:
                技能单次伤害.append(0)

        技能消耗时间 = 0.0;
        爆裂弹间隔 = 0.115;
        每轮射击次数 = floor(0.5 * (16 + floor(0.5 * (min(self.技能栏[self.技能序号['弹夹改装']].等级, 20)-10)))-1)
        每轮时间 = 爆裂弹间隔 * 每轮射击次数;

        if (self.武器类型 != '手弩'):
            爆裂弹间隔 = 0.14;
            每轮射击次数 = floor(0.5 * (9 + floor(0.5 * (min(self.技能栏[self.技能序号['弹夹改装']].等级, 20)-9)))-1)
            每轮时间 = 爆裂弹间隔 * 每轮射击次数;

        爆裂弹位置 = -1
        # 技能释放次数计算
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 == '爆裂弹':
                    技能释放次数.append(0)
                    爆裂弹位置 = len(技能释放次数)-1
                else:
                    if self.次数输入[self.技能序号[i.名称]] == '/CD':
                        技能释放次数.append(int((self.时间输入) / (i.等效CD(self.武器类型)+i.技能施放时间) + 1 + i.基础释放次数))
                        if i.脱手 ==1:
                            技能消耗时间 += int((self.时间输入) / (i.等效CD(self.武器类型) + i.技能施放时间) + 1 + i.基础释放次数) * 0.2
                        else:
                            技能消耗时间 += int((self.时间输入) / (i.等效CD(self.武器类型) + i.技能施放时间) + 1 + i.基础释放次数) *  i.技能施放时间
                    elif self.次数输入[self.技能序号[i.名称]] != '0':
                        技能释放次数.append(int(self.次数输入[self.技能序号[i.名称]]))
                    else:
                        技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        if self.次数输入[self.技能序号['爆裂弹']] == '/CD':
           技能释放次数[爆裂弹位置] =int(floor((self.时间输入-技能消耗时间)/每轮时间)*每轮射击次数)
        else:
            if self.次数输入[self.技能序号['爆裂弹']] != '0':
                技能释放次数[爆裂弹位置] = int(self.次数输入[self.技能序号['爆裂弹']])*每轮射击次数
            else:
                技能释放次数[爆裂弹位置].append(0)


        # 单技能伤害合计

        for i in self.技能栏:
            if i.是否主动 == 1 and 技能释放次数[self.技能序号[i.名称]] != 0:
                技能总伤害.append(技能单次伤害[self.技能序号[i.名称]] * 技能释放次数[self.技能序号[i.名称]] * (
                            1 + self.白兔子技能 * 0.20 + self.年宠技能 * 0.10 * self.宠物次数[self.技能序号[i.名称]] / 技能释放次数[
                        self.技能序号[i.名称]] + self.斗神之吼秘药 * 0.12))
            else:
                技能总伤害.append(0)

        总伤害 = 0
        for i in self.技能栏:
            总伤害 += 技能总伤害[self.技能序号[i.名称]]

        if x == 0:
            return 总伤害

        if x == 1:
            详细数据 = []
            for i in range(0, len(self.技能栏)):
                详细数据.append(技能释放次数[i])
                详细数据.append(技能总伤害[i])
                if 技能释放次数[i] != 0:
                    详细数据.append(技能总伤害[i] / 技能释放次数[i])
                else:
                    详细数据.append(0)
                if 总伤害 != 0:
                    详细数据.append(技能总伤害[i] / 总伤害 * 100)
                else:
                    详细数据.append(0)
            return 详细数据


class 大将军(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 大将军角色属性()
        self.角色属性A = 大将军角色属性()
        self.角色属性B = 大将军角色属性()
        self.一觉序号 = 大将军一觉序号
        self.二觉序号 = 大将军二觉序号
        self.三觉序号 = 大将军三觉序号
        self.护石选项 = deepcopy(大将军护石选项)
        self.符文选项 = deepcopy(大将军符文选项)

