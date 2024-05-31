# encoding: utf-8
class Menu(object):
    def config(self,root,**kwargs):
        root.thpage(u"!![it]Enti", table="docs.ente", multipage="True", tags="")
        root.thpage(u"!![it]Tipologia Documenti", table="docs.tip_doc", multipage="True", tags="")
        root.thpage(u"!![it]Documenti Attachments", table="docs.documenti_atc", multipage="True", tags="")
        root.thpage(u"!![it]Documenti", table="docs.documenti", multipage="True", tags="")
