#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import datetime
import csv
import random
import re
from threading import Thread
import _thread
import urllib.request
import urllib.error
import requests
from requests.adapters import HTTPAdapter

file = ''
now_time = datetime.datetime.now().strftime('%Y-%m-%d')

def view():
    root = tk.Tk()
    lb = tk.Label(root, text='文件处理', \
                  bg='#d3fbfb', \
                  fg='red', \
                  font=('华文新魏', 16), \
                  width=660, \
                  height=1, )
    lb.pack()
    text_val = tk.Text(root, width=100, height=2)  # 30的意思是30个平均字符的宽度，height设置为两行
    text_val.place(relx=0.25, rely=0.05)
    # 上传文件
    def upload_files():
        selectFiles = tk.filedialog.askopenfilenames(
            title='可选择1个或多个文件')  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
        for selectFile in selectFiles:
            global file
            file = selectFile
            print(file)
            text_val.insert(tk.INSERT, file)  # INSERT表示输入光标所在的位置，初始化后的输入光标默认在左上角
    # button
    btn1 = tk.Button(root, text='上传文件', command=lambda: upload_files())
    btn1.place(relx=0.01, rely=0.05, relwidth=0.2, relheight=0.05)
    # button
    btn1 = tk.Button(root, text='获取Baiduspider', command=lambda: start())
    btn1.place(relx=0.01, rely=0.15, relwidth=0.2, relheight=0.05)
    # button
    btn1 = tk.Button(root, text='获取200', command=lambda: http_200())
    btn1.place(relx=0.25, rely=0.15, relwidth=0.2, relheight=0.05)
    # button
    btn1 = tk.Button(root, text='获取404', command=lambda: http_404())
    btn1.place(relx=0.5, rely=0.15, relwidth=0.2, relheight=0.05)

    text = tk.Text(root, width=100, height=2)
    text.place(relx=0.01, rely=0.25)
    text.update()

    # 所有百度
    def search_str():
        baidu_str_all = text.get("0.01", 1.6)
        str = baidu_str_all
        with open(file, mode='r') as f:
            data_list = []
            for val in f.readlines():  # 读取文件的每一行
                if baidu_str_all in val:
                    str += val
                    # 分割
                    str_sp = val.split(",")
                    data_list.append(tuple(str_sp))
        # 导出
        _thread.start_new_thread(file_csv, (baidu_str_all, data_list))
        # txt
        _thread.start_new_thread(file_text, (baidu_str_all, str))

    # button
    btn1 = tk.Button(root, text='筛选', command=lambda: search_str())
    btn1.place(relx=0.01, rely=0.35, relwidth=0.2, relheight=0.05)

    # button
    btn1 = tk.Button(root, text='获取状态码', command=lambda: http_request())
    btn1.place(relx=0.01, rely=0.55, relwidth=0.2, relheight=0.05)

    root.title("文件处理")
    root.geometry('660x660')
    root.mainloop()
# 获取http
def http_request():
    result = ''
    str_baidu = 'http_status_code'
    code = ''
    with open(file, mode='r') as f:
        for url in f.readlines():  # 读取文件的每一行
            # res = requests.get(url, timeout=5, allow_redirects=False)
            # code = str(res.status_code)
            try:
                # response = urllib.request.urlopen(url, timeout=5)
                # code = str(response.status)
                res = requests.get(url, timeout=5, allow_redirects=False)
                code = str(res.status_code)
            except:
                print("Unexpected error:")
                code = 'error'
            finally:
                print(url)
            result += code + '\t' + url

    with open(str_baidu + now_time + '.log', 'w') as fr:
        fr.write(result)


# 所有百度
def start():
    baidu_str_all = ''
    str_baidu = 'Baiduspider'
    with open(file, mode='r') as f:
        data_list = []
        for val in f.readlines():  # 读取文件的每一行
            if str_baidu in val:
                baidu_str_all += val
                # 分割
                str_sp = val.split(",")
                data_list.append(tuple(str_sp))
    # 导出
    _thread.start_new_thread(file_csv, (str_baidu, data_list))
    # txt
    _thread.start_new_thread(file_text, (str_baidu, baidu_str_all))


# 取出200文件
def http_200():
    str = ''
    str_200 = ',200,'
    with open(file, mode='r') as f:
        data_list = []
        for val in f.readlines():  # 读取文件的每一行
            if str_200 in val:
                str += val
                # 分割
                str_sp = val.split(",")
                data_list.append(tuple(str_sp))
    # 导出
    _thread.start_new_thread(file_csv, (str_200, data_list))
    # txt
    _thread.start_new_thread(file_text, (str_200, str))


# 取出404文件
def http_404():
    str = ''
    str_404 = ',404,'
    with open(file, mode='r') as f:
        data_list = []
        for val in f.readlines():  # 读取文件的每一行
            if str_404 in val:
                str += val
                # 分割
                str_sp = val.split(",")
                data_list.append(tuple(str_sp))
    # 导出
    _thread.start_new_thread(file_csv, (str_404, data_list))
    # txt
    _thread.start_new_thread(file_text, (str_404, str))


# 写入文件
def file_text(file, str_content):
    # txt
    with open('file/' + file + now_time + '.log', 'w') as fr:
        fr.write(str_content)

# 导出csv
def file_csv(file,data_list):
    csvfile = open('file/' + file + now_time + '.csv', 'w', newline='')  # 打开方式还可以使用file对象
    writer = csv.writer(csvfile)
    writer.writerows(data_list)
    csvfile.close()


if __name__ == '__main__':
     view()
