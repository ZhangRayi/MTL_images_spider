# MTL_images_spider
美图录（网站）的图片爬虫（两部分）——基于Scrapy框架的简易爬虫

# 先运行meitulu_project 获取网站相关信息，再使用meitulu_image_project 进行对每个页面的图片进行爬取、储存！

# meitulu_project
通过访问每个tag的index.html得到所有的网页数据中的article的url及相关信息。
json文件默认储存在E盘xxx，请一定自己确认修改!

# meitulu_image_project
通过读取本地(meitulu_project的输出结果)文件，访问并获取相关链接，对每个文章进行遍历式访问以获取图片链接。
jpg(image)位置默认存储地址为E盘xxx，请一定确认自己修改!

# 相关责任 声明
侵权及时删除，误作他用。
若要引用，请注明本文链接！
本作者写这个爬虫只为一时锻炼，无意陷入麻烦！
若因爬虫使用而涉及到任何纠纷，请使用者自己负责！
同意以上内容，敬请使用
