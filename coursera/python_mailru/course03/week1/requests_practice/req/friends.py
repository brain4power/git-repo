import requests
import json

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'

"""В итоге запросы будут иметь вид:

– Для получения id пользователя по username или user_id:

https://api.vk.com/method/users.get?v=5.71&access_token=[token]&user_ids=[user_id]

– Для получения списка друзей:

https://api.vk.com/method/friends.get?v=5.71&access_token=[token]&user_id=[user_id]&fields=bdate

При анализе ответа, полученного методом friends.get, можно заметить, что bdate есть не у всех пользователей 
и у некоторых в bdate отсутствует год рождения. Поэтому необходимо пропускать этот случай. 
Примеры возможных значений: "bdate":"6.6", "bdate":"25.8.1993".Для вычисления возраста, необходимо 
взять текущий год , и вычесть из него год рождения пользователя, полученный из API (без учета месяца и числа).

"""


def get_vk_uid(name):
    link = 'https://api.vk.com/method/users.get?v=5.71&access_token=' + ACCESS_TOKEN
    resp = requests.get(link, params={'user_ids': name})
    return resp.json()['response'][0]['id']


def get_friends_list(uid):
    link = 'https://api.vk.com/method/friends.get?v=5.71&access_token=' + ACCESS_TOKEN + '&user_id=' + uid
    return link


def calc_age(uid):
    CURRENT_YEAR = 2019
    try:
        int(uid)
    except ValueError:
        uid = str(get_vk_uid(uid))

    link = 'https://api.vk.com/method/friends.get?v=5.71&access_token=' + ACCESS_TOKEN + '&user_id=' + uid
    param = {'fields': 'bdate'}
    r = requests.get(link, params=param)
    friend_data = r.json()['response']['items']

    bdays_data = {}
    for each in friend_data:
        if 'bdate' in each:
            bday = each['bdate'].split('.')
            if len(bday) == 3:
                spam = str(CURRENT_YEAR - int(bday[2]))
                if spam in bdays_data:
                    bdays_data[spam] += 1
                else:
                    bdays_data[spam] = 1

    result = []
    for each in bdays_data:
        result.append(tuple([int(each), bdays_data[each]]))
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    return result


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)

