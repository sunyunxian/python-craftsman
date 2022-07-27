'''
结论
1. 只捕获会出现异常的代码段，不会出现一样的代码段不需要捕获
2. 更加精准的捕获，而不是用一个 Exception 就解决了
3. 出现异常不是问题，早点暴露异常
'''
import re

import requests  # type: ignore


def save_website_title(url: str, filename: str) -> bool:
    '''获取某个网址的标题，并存储到文件中'''
    try:
        resp = requests.get(url)
        resp.encoding = 'utf-8'
    except requests.RequestException as e:
        print(f'sava failed: unable to get page content: {e}')
        return False
    obj = re.search(r'<title>(.*)</title>', resp.text)
    if not obj:
        print('Save failed, title tag not found')
        return False

    title = obj.group(1)
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(title)
            return True
    except IOError:
        print(f'Sava failed, unable to write to file {filename}')
        return False


def main():
    save_website_title('http://www.baidu.com', 'baidu_title.txt')


if __name__ == '__main__':
    main()
