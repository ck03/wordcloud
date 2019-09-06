from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import jieba
import operator


def GetWordCloud():
    path_txt = 'D://study/python2/03爬蟲/aa.txt'
    path_img = "D://study/python2/03爬蟲/bb.jpg"
    f = open(path_txt, 'r', encoding='UTF-8').read()
    background_image = np.array(Image.open(path_img))
    # 結巴分詞，生成字符串，如果不通過分詞，無法直接生成正確的中文詞雲,感興趣的朋友可以去查一下，有多種分詞模式
    # Python join() 方法用於將序列中的元素以指定的字符連接生成一個新的字符串。
    cut_text = " ".join(jieba.cut(f))
    cut_list = cut_text.split(" ")
    # print(cut_list)
    cut_list2 = []
    for ele in cut_list:
        if ele != "\n":
            cut_list2.append(ele)
    # print(cut_list2)
    dic = {}
    for ele in cut_list2:
        if ele not in dic:
            dic[ele] = 1
        else:
            dic[ele] = dic[ele] + 1
    # print(dic)
    sorted_word = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    dic = {}
    n = 0
    for ele in sorted_word:
        # print(ele[0], ele[1])
        dic[ele[0]] = ele[1]
        n += 1
       
    print(dic)

    wordcloud = WordCloud(
        # 設置字體，不然會出現口字亂碼，文字的路徑是電腦的字體一般路徑，可以換成別的
        font_path="C:/Windows/Fonts/soukoumincho.ttf",
        background_color="white",
        # stopwords=stopwordss,
        max_font_size=100,
        min_font_size=4,
        max_words=5000,
        # random_state=240,
        # mask參數=圖片背景，必須要寫上，另外有mask參數再設定寬高是無效的
        mask=background_image,
    )
    # ).generate(cut_text)

    # generate_from_frequencies 參數要帶 dictionary , generate 則帶 str    
    wordcloud.generate_from_frequencies(dic)
    # 生成顏色值
    image_colors = ImageColorGenerator(background_image)
    # 下面代碼表示顯示圖片
    # plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    GetWordCloud()

