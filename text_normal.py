# -*- coding: utf-8 -*-

# --------------------------------
# Name:         text_normal.py
# Author:       devshilei@gmail.com
# @Time         2020/7/14 下午4:16
# Description:
# --------------------------------
import json


def normal_dbc_to_sbc(text):
    """
    description: 对文本进行标准化【全角字符替换为半角字符】
                 注：此处保留原始中文句号“。”以及顿号“、”，
                 因其在句子中长用来表平行关系且替换为其他半角字符容易引起歧义。
                 Double Byte Character，简称：DBC   全角字符
                 Single Byte Character，简称：SBC   半角字符
    :param text:    待处理文本
    :return:        输出为标准化之后的文本
    """
    mapping_data = json.load(open("dbc_mapping_sbc_data.json", mode="r", encoding="utf8"))
    for dbc_char, sbc_char in mapping_data.items():
        text = text.replace(dbc_char, sbc_char)
    return text


def normal_zh_cn_hant_mapping(text):
    """
    description: 中文繁体、简体字标注化，将繁体转为简体字
    :param text: 待转化文本
    :return:     返回标准化后的文本
    """
    mapping_data = json.load(open("zh_cn_hant_mapping_data.json", mode="r", encoding="utf8"))
    for trad_char, simp_char in mapping_data.items():
        text = text.replace(trad_char, simp_char)
    return text
