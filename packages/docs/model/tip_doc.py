# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('tip_doc', pkey='id', name_long='!![it]Tipologia Documento', name_plural='!![it]Tipologia Documenti',caption_field='hierarchical_descrizione')
        self.sysFields(tbl,hierarchical='descrizione', counter=True, df=True)
        tbl.column('descrizione',name_long='Descrizione')
        
