#!/usr/bin/env python
# -*- coding:utf-8 -*-

from xlutils.copy import copy
import xlrd
import xlwt


def load_result(filename):
    xls_book = xlrd.open_workbook(filename=filename, on_demand=True)
    data_sheet = xls_book.sheet_by_name('result')
    rows_data = data_sheet.get_rows()

    comb_dict_keys = []
    r_data = rows_data.next()  # first row is key name
    for k in r_data:
        comb_dict_keys.append(k.value)

    mitama_combs = []

    for r_data in rows_data:
        combs_data = dict()
        for i in range(len(comb_dict_keys)):
            combs_data[comb_dict_keys[i]] = r_data[i].value

        mitama_combs.append(combs_data)

    return mitama_combs


def write_independent_comb_result(filename, independet_combs):
    pass


def sort_mitama_combs(mitama_combs, sort_key=u'攻击x暴伤'):
    def cmp_key(comb1, comb2):
        if comb1.get(sort_key, 0) >= comb2.get(sort_key, 0):
            return True
        else:
            return False

    mitama_combs.sort(cmp=cmp_key)


def search_independent_comb(mitama_combs):
    used_mitama = []
    independent_comb = []
    for combs_data in mitama_combs:
        mitama_serials = combs_data.get(u'御魂序号', '').split(',')
        if not (set(used_mitama) & set(mitama_serials)):
            # 无重复御魂，即为独立组合
            independent_comb.append(combs_data)
            used_mitama.extend(mitama_serials)

    return independent_comb


if __name__ == '__main__':
    import sys

    mitama_combs = load_result(sys.argv[1])
    sort_mitama_combs(mitama_combs)
    print(mitama_combs)
