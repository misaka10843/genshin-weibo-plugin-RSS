# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time
from PIL import Image, ImageDraw, ImageFont
import sys
import os   
import io


#############################
#
#获取最新的RSS XML
#
#############################

os.system("cd "+sys.path[0]+" && wget -O rss.xml https://rssfeed.today/weibo/rss/6593199887")


#############################
#
#文字转图片
#
#############################

class ImgText:
    font = ImageFont.truetype("font.ttf", 16)

    def __init__(self, text):
        # 预设宽度 可以修改成你需要的图片宽度
        self.width = 1100
        # 文本
        self.text = text
        # 段落 , 行数, 行高
        self.duanluo, self.note_height, self.line_height = self.split_text()

    def get_duanluo(self, text):
        txt = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt)
        # 所有文字的段落
        duanluo = ""
        # 宽度总和
        sum_width = 0
        # 几行
        line_count = 1
        # 行高
        line_height = 0
        for char in text:
            width, height = draw.textsize(char, ImgText.font)
            sum_width += width
            if sum_width > self.width:  # 超过预设宽度就修改段落 以及当前行数
                line_count += 1
                sum_width = 0
                duanluo += '\n'
            duanluo += char
            line_height = max(height, line_height)
        if not duanluo.endswith('\n'):
            duanluo += '\n'
        return duanluo, line_height, line_count

    def split_text(self):
        # 按规定宽度分组
        max_line_height, total_lines = 0, 0
        allText = []
        for text in self.text.split('\n'):
            duanluo, line_height, line_count = self.get_duanluo(text)
            max_line_height = max(line_height, max_line_height)
            total_lines += line_count
            allText.append((duanluo, line_count))
        line_height = max_line_height
        total_height = total_lines * line_height
        return allText, total_height, line_height

    def draw_text(self):
        """
        绘图以及文字
        :return:
        """
        note_img = Image.open("bg.png").convert("RGBA")
        draw = ImageDraw.Draw(note_img)
        # 左上角开始
        x, y = 5, 5
        for duanluo, line_count in self.duanluo:
            draw.text((x, y), duanluo, fill=(0, 40, 77), font=ImgText.font)
            y += self.line_height * line_count
        note_img.save("txt.png")


#############################
#
#执行php并且读取解析出来的rss替换和删除html标签
#
#############################

def html():
    os.system("php getRSS.php")
    print ("间歇停止1秒等待php获取完其rss解析文件，\n这一步需要Windows添加php的全局变量并且重启后才能使用，Linux需要安装php才能运行\n（就是懒得写python，就直接写成了php+python了qwq）")
    time.sleep(1)
    html = io.open('rss.out',encoding='utf-8').read()
    html = html.replace('<br>',"\n")
    html = html.replace('<br />',"\n")
    soup = BeautifulSoup(html,'html.parser')
    print(soup.get_text())
    path = './rss.out'
    os.remove(path)
    return soup.get_text()


if __name__ == '__main__':
    n = ImgText(
        html())
    n.draw_text()