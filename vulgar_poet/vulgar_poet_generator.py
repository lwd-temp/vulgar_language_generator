# -*- coding: utf-8 -*-

import random
import re

two_char_words = ['朱砂', '天下', '杀伐', '人家', '韶华', '风华', '繁华', '血染', '墨染', '白衣', '素衣', '嫁衣',
                  '倾城', '孤城', '空城', '旧城', '旧人', '伊人', '心疼', '春风', '古琴', '无情', '迷离', '奈何', '断弦', '焚尽',
                  '散乱', '陌路', '乱世', '笑靥', '浅笑', '明眸', '轻叹', '烟火', '一生', '三生', '浮生', '桃花', '梨花', '落花',
                  '烟花', '离殇', '情殇', '爱殇', '剑殇', '灼伤', '仓皇', '匆忙', '陌上', '清商', '焚香', '墨香', '微凉', '断肠',
                  '痴狂', '凄凉', '黄梁', '未央', '成双', '无恙', '虚妄', '凝霜', '洛阳', '长安', '江南', '忘川', '千年', '纸伞',
                  '烟雨', '回眸', '公子', '红尘', '红颜', '红衣', '红豆', '红线', '青丝', '青史', '青冢', '白发', '白首', '白骨',
                  '黄土', '黄泉', '碧落', '紫陌']

four_char_words = ['情深缘浅', '情深不寿', '莫失莫忘', '阴阳相隔', '如花美眷', '似水流年',
                   '眉目如画', '曲终人散', '繁华落尽', '不诉离殇', '一世长安']

sentence_model = ['xx，xx，xx了xx。', 'xxxx，xxxx，不过是一场xxxx。', '你说xxxx，我说xxxx，最后不过xxxx。',
                  'xx，xx，许我一场xxxx。', '一x一x一xx，半x半x半xx。', '你说xxxxxxxx，后来xxxxxxxx。', 'xxxx，xxxx，终不敌xxxx。']


def get_sentence():
    sentence = random.choice(sentence_model)
    four_char_re = re.compile('xxxx')
    two_char_re = re.compile('xx')
    one_char_re = re.compile('x')

    while 'xxxx' in sentence:
        sentence = four_char_re.sub(random.choice(four_char_words), sentence, 1)

    while 'xx' in sentence:
        sentence = two_char_re.sub(random.choice(two_char_words), sentence, 1)

    while 'x' in sentence:
        one_char = random.choice(random.choice(two_char_words))  # randomly select one char from two_char
        sentence = one_char_re.sub(one_char, sentence, 1)

    return sentence


if __name__ == '__main__':
    for i in range(5):
        s = get_sentence()
        print(s)
