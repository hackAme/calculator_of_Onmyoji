# coding: utf-8

MITAMA_COL_NAME_ZH = [u'御魂序号', u'御魂类型', u'位置', u'攻击',
                      u'攻击加成', u'防御', u'防御加成', u'暴击',
                      u'暴击伤害', u'生命', u'生命加成', u'效果命中',
                      u'效果抵抗', u'速度']

RESULT_HEADER = [u'组合序号'] + MITAMA_COL_NAME_ZH

RESULT_COMB_HEADER = [u'组合个数', u'result序号', u'攻击x暴伤总和']

EXTEND_HEADER = [u'式神基础攻击', u'式神基础生命', u'式神基础暴伤',
                 u'总攻击', u'总生命',
                 u'攻击x暴伤', u'生命×暴伤']

MITAMA_TYPES = [u'珍珠', u'骰子鬼', u'蚌精', u'魅妖', u'针女',
                u'返魂香', u'土蜘蛛', u'胧车', u'荒骷髅', u'地震鲶',
                u'蜃气楼', u'雪幽魂', u'地藏像', u'蝠翼', u'涅槃之火',
                u'三味', u'魍魉之匣', u'被服', u'招财猫', u'反枕',
                u'轮入道', u'日女巳时', u'镜姬', u'钟灵', u'狰',
                u'火灵', u'鸣屋', u'薙魂', u'心眼', u'木魅', u'树妖',
                u'网切', u'阴摩罗', u'伤魂鸟', u'破势', u'镇墓兽',
                u'狂骨', u'幽谷响']

MITAMA_PROPS = [u'攻击', u'攻击加成', u'防御', u'防御加成', u'暴击',
                u'暴击伤害', u'生命', u'生命加成', u'效果命中',
                u'效果抵抗', u'速度']

MITAMA_ENHANCE = {u"珍珠": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"骰子鬼": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"蚌精": {u"加成类型": u"效果命中", u"加成数值": 15},
                  u"魅妖": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"针女": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"返魂香": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"雪幽魂": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"地藏像": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"蝠翼": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"涅槃之火": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"三味": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"魍魉之匣": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"被服": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"招财猫": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"反枕": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"轮入道": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"日女巳时": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"镜姬": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"钟灵": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"狰": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"火灵": {u"加成类型": u"效果命中", u"加成数值": 15},
                  u"鸣屋": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"薙魂": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"心眼": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"木魅": {u"加成类型": u"防御加成", u"加成数值": 30},
                  u"树妖": {u"加成类型": u"生命加成", u"加成数值": 15},
                  u"网切": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"阴摩罗": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"伤魂鸟": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"破势": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"镇墓兽": {u"加成类型": u"暴击", u"加成数值": 15},
                  u"狂骨": {u"加成类型": u"攻击加成", u"加成数值": 15},
                  u"幽谷响": {u"加成类型": u"效果抵抗", u"加成数值": 15},
                  u"土蜘蛛": {u"加成类型": u"", u"加成数值": 0},
                  u"胧车": {u"加成类型": u"", u"加成数值": 0},
                  u"荒骷髅": {u"加成类型": u"", u"加成数值": 0},
                  u"地震鲶": {u"加成类型": u"", u"加成数值": 0},
                  u"蜃气楼": {u"加成类型": u"", u"加成数值": 0},
                  }

ATTACK_MITAMA_TYPE = [t for t, e in MITAMA_ENHANCE.items()
                      if e[u'加成类型'] in ['', u'攻击加成', u'暴击']]
