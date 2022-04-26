from PIL import Image
import sys

# 根据公式
# 变灰度 提升表图的亮度
def lighter(pic):
    pic = pic.convert('L')
    width, height = pic.size
    for w in range(width):
        for h in range(height):
            hd = pic.getpixel((w, h))
            hd = int(hd / 2) + 128
            pic.putpixel((w, h), (hd))
    return pic


# 变灰度 降低里图的亮度
def darker(pic):
    pic = pic.convert('L')
    width, height = pic.size
    for w in range(width):
        for h in range(height):
            hd = pic.getpixel((w, h))
            hd = int(hd / 2)
            pic.putpixel((w, h), (hd))
    return pic

# 统一图片的大小
def same_size(pic1, pic2):
    pic1_width, pic1_height = pic1.size
    pic2_width, pic2_height = pic2.size
    max_width, max_height = max(pic1_width, pic2_width), max(pic1_height, pic2_height)
    same_size_pic1 = Image.new('L', (max_width, max_height), 'white')
    same_size_pic2 = Image.new('L', (max_width, max_height), 'black')
    same_size_pic1.paste(pic1, (int((max_width - pic1_width) / 2), int((max_height - pic1_height) / 2)))
    same_size_pic2.paste(pic2, (int((max_width - pic2_width) / 2), int((max_height - pic2_height) / 2)))
    return same_size_pic1, same_size_pic2

# 表图和里图的合成图
def tank(biao, li):
    w, h = biao.size
    tank_pic = Image.new('LA', (w, h))
    for x in range(w):
        for y in range(h):
            biao_, li_ = biao.getpixel((x, y)), li.getpixel((x, y))
            tank_a = 255 - (biao_ - li_)
            if tank_a == 0:
                tank_p = 0
            else:
                tank_p = int(255 * li_ / tank_a)
            tank_pic.putpixel((x, y), (tank_p, tank_a))
    tank_pic.save('./virtual_tank.png')
    print('合成完成！')

if __name__ == '__main__':
    arg = sys.argv
    if len(arg) == 3:
        biao_tu, li_tu = Image.open(arg[1]), Image.open(arg[2])
        l_biao_tu = lighter(pic=biao_tu)
        l_li_tu = darker(pic=li_tu)
        same_size_l_biao_tu, same_size_l_li_tu = same_size(pic1=l_biao_tu, pic2=l_li_tu)
        tank(biao=same_size_l_biao_tu, li=same_size_l_li_tu)
    else:
        print('请按照格式输入！请重试！')
