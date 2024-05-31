# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('documenti', pkey='id', name_long='!![it]Documento', name_plural='!![it]Documenti',caption_field='descrizione')
        self.sysFields(tbl)
        tbl.column('ente_id',size='22', group='_', name_long='!![it]Ente'
                    ).relation('ente.id', relation_name='ente_doc', mode='foreignkey', onDelete='raise')
        tbl.column('data', dtype='D', name_short='!![it]Data')
        tbl.column('prot', name_short='!![it]Prot.n.')
        tbl.column('descrizione', name_short='!![it]Descrizione')
        tbl.column('tipo_doc_id',size='22', group='_', name_long='!![it]Tipologia documento'
                    ).relation('tip_doc.id', relation_name='tipodoc', mode='foreignkey', onDelete='raise')
        