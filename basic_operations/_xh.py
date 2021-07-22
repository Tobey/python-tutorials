import json
import random

import os
from os.path import expanduser

import requests


def check_solution():
    from . import functions
    api_request = """"""
    failed = []
    passed = []
    cur = os.path.abspath(__file__)
    hm  = expanduser("~")

    try:
        c = random.randint(1, 1000)
        o = functions.count_a_string('x' * c)
        if o == c:
            passed.append('def count_a_string()')
        else:
            failed.append('def count_a_string()')

    except:
        failed.append('def count_a_string()')

    try:
        c = random.randint(1, 1000)
        o = functions.count_a_list([0] * c)
        if o == c:
            passed.append('def count_a_list()')
        else:
            failed.append('def count_a_list()')

    except:
        failed.append('def count_a_string()')

    try:
        f_name = 'reverse_a_list'
        print(f'running: {f_name}')
        c = random.randint(1, 100)
        rand_list = [random.randint(1, 100) for i in range(c)]
        r = rand_list.copy()
        r.reverse()
        o = functions.reverse_a_list(rand_list)

        if o == r:
            passed.append(f_name)
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)

    try:
        f_name = 'multiplies_two_numbers'
        print(f'running: {f_name}')
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        o = functions.multiplies_two_numbers(a, b)

        if o == a * b:
            passed.append(f_name)
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)

    try:
        f_name = 'create_in_pwd'
        print(f'running: {f_name}')
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        functions.create_in_pwd()

        if os.path.exists(os.path.join(cur, 'testfile1.txt')):
            passed.append(f_name)
            os.remove(os.path.join(cur, 'testfile1.txt'))
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)



    try:
        f_name = 'create_in_desktop'
        print(f'running: {f_name}')

        functions.create_in_desktop()

        if os.path.exists(os.path.join(hm, 'Desktop','testfile2.txt')):
            passed.append(f_name)
            os.remove(os.path.join(hm, 'Desktop','testfile2.txt'))

        else:
            failed.append(f_name)

    except:
        failed.append(f_name)



    try:
        f_name = 'create_in_pwd_with_input'
        print(f'running: {f_name}')
        c = random.randint(1, 100)
        rand_list = [random.randint(1, 100) for i in range(c)]
        functions.create_in_pwd_with_input(rand_list)

        if os.path.exists(os.path.join(cur ,'testfile3.txt')):
            with open(os.path.join(cur ,'testfile3.txt')) as f:
                d = [int(x) for x in f.readlines()]

            if rand_list == d:
                passed.append(f_name)
            else:
                failed.append(f_name)
        else:
            failed.append(f_name)


    except:
        failed.append(f_name)

    try:
        f_name = 'create_filter_int'
        print(f'running: {f_name}')
        o = functions.create_filter_int([1, 2] + ([' ']* 10) + [3]* 12)

        if o == [1, 2] + [3]* 12:
            passed.append(f_name)
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)


    try:
        f_name = 'create_filter_str'
        print(f'running: {f_name}')
        o = functions.create_filter_str([1, 2] + ([' ']* 10) + [3]* 12)

        if o == [' ']*10:
            passed.append(f_name)
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)

    try:
        f_name = 'api_request_function'
        print(f'running: {f_name}')
        o = functions.api_request_function()

        if o == api_request:
            passed.append(f_name)
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)


    try:
        f_name = 'api_request_function_json'
        print(f'running: {f_name}')
        o = functions.api_request_function_json()
        r = requests.get('https://api.discogs.com/releases/249504').json()
        if o == r:
            passed.append(f_name)
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)

    try:
        f_name = 'api_request_function_vids'
        print(f'running: {f_name}')
        p = requests.get('https://api.discogs.com/releases/249504').json()
        n = [x for x in p['videos']['url']]
        o = functions.api_request_function_vids()
        if o == n:
            passed.append(f_name)
        else:
            failed.append(f_name)

    except:
        failed.append(f_name)


    print('{} failed -- {}'.format(len(failed), failed))
    print('{} passed -- {}'.format(len(passed), passed))
