#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('nome')
        r.fieldcell('note')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        #pane = form.record
        #fb = pane.formbuilder(cols=2, border_spacing='4px')
        #fb.field('nome' )
        #fb.field('note' )
        bc = form.center.borderContainer()
        self.ente(bc.roundedGroupFrame(title='!![it]Ente',region='top',datapath='.record',height='60px', splitter=True))
        tc = bc.tabContainer(margin='2px',region='center')
        self.docs(tc.contentPane(title='!![it]Documenti'))

    def ente(self, pane):
        fb = pane.div(margin_left='50px',margin_right='80px').formbuilder(cols=3, border_spacing='4px',colswidth='auto',fld_width='100%')
        fb.field('nome' )
        fb.field('note' )

    def docs(self,pane):
        pane.stackTableHandler(relation='@ente_doc',
                                viewResource='ViewFromDocumenti',extendedQuery=True,pbl_classes=True)
            
    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
