from bs4 import BeautifulSoup
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}

    for key in files:
        files[key] = path + key

    def find_all_links(name):
        with open(files[name], 'r') as fl:
            spam = fl.read()
            result = re.findall(r"(?<=/wiki/)[\w()]+", spam)
        return result

    class Node:
        def __init__(self, name, node_parent):
            self.name = name
            self.parent = node_parent

    parsed_names = []
    all_node_objects = dict()
    all_node_objects[start] = Node(start, None)
    parsed_names.append(start)

    for name in parsed_names:
        for each in find_all_links(name):
            if each in files:
                if each not in parsed_names:
                    parsed_names.append(each)
                    all_node_objects[each] = Node(each, all_node_objects[name])

    # а если несколько путей?
    # путь будет один и кратчайшим по построению дерева -
    # мы тупо не работаем с узлами, по которым уже прошлись и не делаем более длинные петли
    return all_node_objects


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    target = files[end]

    while target.parent:
        bridge.append(target.name)
        target = target.parent
    bridge.append(target.name)
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    out = {}

    def count_imgs(soup_page):
        total = 0
        all_images = soup_page.find_all('img')
        for each in all_images:
            value = re.findall(r' width=\"(\d*)\"', str(each))
            if value:
                if int(value[0]) >= 200:
                    total += 1
        return total

    def count_headers(soup_page):
        total = 0
        all_headers = []
        for el in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            spam = soup_page.find_all(el)
            for el in spam:
                all_headers.append(el)
        for each in all_headers:
            if str(each.text).startswith('C') or \
                    str(each.text).startswith('T') or \
                    str(each.text).startswith('E'):
                total += 1
        return total

    def get_links_len(body):
        all_a = body.find_all('a')
        max_count = 0

        def count_sublings(tag):
            sublings_array = ['a']
            while tag.nextSibling:
                if tag.nextSibling.name and tag.nextSibling.name != 'br':
                    sublings_array.append(tag.nextSibling.name)
                tag = tag.nextSibling
            max_count_a = 0
            count_in = 0
            for name in sublings_array:
                if name == 'a':
                    count_in += 1
                    if count_in > max_count_a:
                        max_count_a = count_in
                else:
                    count_in = 0

            return max_count_a

        for lnk in all_a:
            count = count_sublings(lnk)
            if count > max_count:
                max_count = count
        return max_count

    def get_lists(body):
        count = 0
        all_lists = body.find_all(['ul', 'ol'])
        for tag in all_lists:
            if not tag.find_parents(['ul', 'ol']):
                count += 1
        return count

    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        imgs = count_imgs(body)
        headers = count_headers(body)
        linkslen = get_links_len(body)
        lists = get_lists(body)

        out[file] = [imgs, headers, linkslen, lists]

    return out
