#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
__title__ = ''
__author__ = 'JWH5566'
__mtime__ = '2016/3/29'

from tkinter import *
from tkinter import ttk, filedialog, messagebox
import base64
import json
import os

from bs4 import BeautifulSoup
import requests





# The business logic
config = {}


def fetch_url():
    url = _url.get()
    config['images'] = []
    _images.set(())  # 初始化listbox一个空的元组
    try:
        page = requests.get(url)
    except requests.RequestException as rex:
        _sb(str(rex))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        images = fetch_images(soup, url)
        if images:
            _images.set(tuple(img['name'] for img in images))
            _sb('找到{}张图片'.format(len(images)))
        else:
            _sb('没有找到图片')
        config['images'] = images  # images 是包含字典的列表


def fetch_images(soup, base_url):
    images = []
    for img in soup.findAll('img'):
        src = img.get('src')
        img_url = (
            '{base_url}/{src}'.format(base_url=base_url, src=src)
        )
        name = img_url.split('/')[-1]
        images.append(dict(name=name, url=img_url))
    return images


# saving the images
def save():
    if not config.get('images'):
        _alert('没有图片保存')
        return
    if _save_method.get() == 'img':
        dirname = filedialog.askdirectory(mustexist=True)
        _save_images(dirname)
    else:
        filename = filedialog.asksaveasfilename(
            initialfile='images.json',
            filetype=[('JSON', '.json')]  # 是一个元组的列表， 每个元组有两个元素， 一个是描述， 一个是扩展名
        )
        _save_json(filename)


def _save_images(dirname):
    if dirname and config.get('images'):
        for img in config['images']:
            img_data = requests.get(img['url']).content
            filename = os.path.join(dirname, img['name'])
            with open(filename, 'wb') as f:
                f.write(img_data)
        _alert('保存完成!')


def _save_json(filename):
    if filename and config.get('images'):
        data = {}
        for img in config['images']:
            img_data = requests.get(img['url']).content
            b64_img_data = base64.b64encode(img_data)
            str_img_data = b64_img_data.decode('utf-8')
            data[img['name']] = str_img_data

        with open(filename, 'w') as ijson:
            ijson.write(json.dumps(data))
        _alert('保存完成!')


# alerting the user
def _sb(msg):
    """
        在状态栏显示
    :param msg:
    :return:
    """
    _status_msg.set(msg)


def _alert(msg):
    messagebox.showinfo(message=msg)


# The layout logic
if __name__ == '__main__':
    _root = Tk()
    _root.title('图片爬虫')
    _mainframe = ttk.Frame(_root, padding='5 5 5 5')
    _mainframe.grid(row=0, column=0, sticky=(E, W, N, S))  # 可以在四个方向上面自己扩展

    # 注：row和column是指的是在父框架中的位置
    #  URL 框架
    _url_frame = ttk.LabelFrame(_mainframe, text='URL', padding='5 5 5 5')
    _url_frame.grid(row=0, column=0, sticky=(E, W))
    _url_frame.rowconfigure(0, weight=1)
    _url_frame.columnconfigure(0, weight=1)

    _url = StringVar()  # 使用这个变量来操作textbox的内容
    _url.set('http://localhost:8000')
    _url_entry = ttk.Entry(
        _url_frame, width=40, textvariable=_url
    )
    _url_entry.grid(row=0, column=0, sticky=(E, W, S, N), padx=5)  # padx 设置水平方向的padding 左右都有
    _fetch_btn = ttk.Button(
        _url_frame, text='获取信息', command=fetch_url  # command的意思是点击按钮 调用这个函数
    )
    #  fetch_url
    _fetch_btn.grid(row=0, column=1, sticky=W, padx=5)

    #  图片框架
    _img_frame = ttk.LabelFrame(
        _mainframe, text='Content', padding='9 0 0 0'
    )
    _img_frame.grid(row=1, column=0, sticky=(N, S, E, W))
    _images = StringVar()
    _img_listbox = Listbox(
        _img_frame, listvariable=_images, height=6, width=25
    )
    _img_listbox.grid(row=0, column=0, sticky=(E, W), pady=5)
    _scrollbar = ttk.Scrollbar(
        _img_frame, orient=VERTICAL, command=_img_listbox.yview
    )
    _scrollbar.grid(row=0, column=1, sticky=(S, N), pady=6)
    _img_listbox.configure(yscrollcommand=_scrollbar.set)

    # 单选框框架
    _radio_frame = ttk.Frame(_img_frame)
    _radio_frame.grid(row=0, column=2, sticky=(N, S, W, E))

    _choice_lbl = ttk.Label(
        _radio_frame, text='选择图片存储的类型'
    )
    _choice_lbl.grid(row=0, column=0, padx=5, pady=5)
    _save_method = StringVar()
    _save_method.set('img')  # 设置默认值选中
    _img_only_radio = ttk.Radiobutton(
        _radio_frame, text='存储为图片', variable=_save_method, value='img'
    )
    _img_only_radio.grid(row=1, column=0, padx=5, pady=2, sticky=W)
    _img_only_radio.configure(state='normal')

    _json_radio = ttk.Radiobutton(
        _radio_frame, text='存储为JSON', variable=_save_method, value='json'
    )
    _json_radio.grid(row=2, column=0, padx=5, pady=2, sticky=W)

    _scrape_btn = ttk.Button(
        _mainframe, text='开始抓图!', command=save
    )
    # save
    _scrape_btn.grid(row=2, column=0, sticky=E, pady=5, padx=10)

    # 状态框架
    _status_frame = ttk.Frame(
        _root, relief='sunken', padding='2 2 2 2'
    )
    _status_frame.grid(row=1, column=0, sticky=(E, W, S))
    _status_msg = StringVar()
    _status_msg.set('输入一个URL地址开始抓图...')
    _status = ttk.Label(
        _status_frame, textvariable=_status_msg, anchor=W
    )
    _status.grid(row=0, column=0, sticky=(E, W))

    _root.mainloop()
