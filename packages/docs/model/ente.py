# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('ente', pkey='id', name_long='!![it]Ente', name_plural='!![it]Enti',caption_field='nome')
        self.sysFields(tbl)
        tbl.column('nome', name_short='!![it]Nome')
        tbl.column('note', name_short='!![it]Note')
        