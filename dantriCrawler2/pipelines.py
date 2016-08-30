# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
class Dantricrawler2Pipeline(object):

    def __init__(self):
        self.xahoi = codecs.open("xa-hoi", "w", "utf-8")
        self.thegioi = codecs.open("the-gioi", "w", "utf-8")
        self.thethao = codecs.open("the-thao", "w", "utf-8")
        self.giaoduc = codecs.open("giao-duc", "w", "utf-8")
        self.kinhte = codecs.open("kinh-te", "w", "utf-8")
        self.vanhoa = codecs.open("van-hoa", "w", "utf-8")
        self.giaitri = codecs.open("giai-tri", "w", "utf-8")
        self.phapluat = codecs.open("phap-luat", "w", "utf-8")
        self.suckhoe = codecs.open("suc-khoe", "w", "utf-8")
        self.digitechno = codecs.open("digital-techno", "w", "utf-8")
        self.others = codecs.open("others", "w", "utf-8")



    def process_item(self, item, spider):

        if not item:
            return

        if "xa-hoi" in item["link"]:
            if item["content"]:
                self.xahoi.write(" ".join(item["content"]).replace("\n", " ") + "\n")

        elif "the-gioi" in item["link"]:
            if item["content"]:
                self.thegioi.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "the-thao" in item["link"]:
            if item["content"]:
                self.thethao.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "giao-duc" in item["link"]:
            if item["content"]:
                self.giaoduc.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "kinh-doanh" in item["link"]:
            if item["content"]:
                self.kinhte.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "van-hoa" in item["link"]:
            if item["content"]:
                self.vanhoa.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "giai-tri" in item["link"]:
            if item["content"]:
                self.giaitri.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "phap-luat" in item["link"]:
            if item["content"]:
                self.phapluat.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "suc-khoe" in item["link"]:
            if item["content"]:
                self.suckhoe.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        elif "suc-manh-so" in item["link"]:
            if item["content"]:
                self.digitechno.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        else:
            if item["content"]:
                self.others.write(" ".join(item["content"]).replace("\n", " ") +"\n")

        return item



#class Dantricrawler2Pipeline(object):
#    def __init__(self):
#        self.content = codecs.open("text", "w", "utf-8")

#    def process_item(self, item, spider):
#        if not item:
#            return

#        if item["content"]:
#            self.content.write(" ".join(item["content"]).replace("\n", " ") + "\n")

#        return item
