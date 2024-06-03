#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('ente_id')
        r.fieldcell('data')
        r.fieldcell('prot')
        r.fieldcell('descrizione', width='100%')
        r.fieldcell('tipo_doc_id')

    def th_order(self):
        return 'data:d'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='', runOnStart=True)

    def th_top_toolbarsuperiore(self,top):
        bar=top.slotToolbar('5,sections@ente_id,5',
                        childname='superiore',_position='<bar',sections_ente_id_multivalue=False,
                        sections_ente_id_multiButton=False,sections_ente_id_lbl='!![it]Ente',
                        sections_ente_id_width='60em')
                        #,gradient_from='#999',gradient_to='#888')
        #bar.actions.div('Actions')
        
    #def th_bottom_toolbarinferiore(self,bottom):
    #    bar=bottom.slotToolbar('5,sections@cliente_id,15',
    #                    childname='inferiore',_position='<bar',sections_cliente_id_multivalue=False,sections_cliente_id_multiButton=False)
        
    def th_queryBySample(self):
        return dict(fields=[dict(field='data', lbl='Date <=',width='10em', op='lesseq', val=''),
                            dict(field='data', lbl='Date >=',width='10em', op='greatereq', val=''),
                            dict(field='data', lbl='!![it]Data doc.',width='10em'),
                            dict(field='prot', lbl='!![it]Prot.n.',width='10em'),
                            dict(field='descrizione', lbl='!![It]Descrizione',width='70em')],
                            cols=5, isDefault=True) 
    
class ViewFromDocumenti(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('data')
        r.fieldcell('prot')
        r.fieldcell('descrizione', width='100%')
        r.fieldcell('tipo_doc_id')

    def th_order(self):
        return 'ente_id'

    def th_query(self):
        return dict(column='descrizione', op='contains', val='')
        
    def th_queryBySample(self):
        return dict(fields=[dict(field='data', lbl='Date <=',width='10em', op='lesseq', val=''),
                            dict(field='data', lbl='Date >=',width='10em', op='greatereq', val=''),
                            dict(field='data', lbl='!![it]Data doc.',width='10em'),
                            dict(field='prot', lbl='!![it]Prot.n.',width='10em'),
                            dict(field='descrizione', lbl='!![It]Descrizione',width='70em')],
                            cols=5, isDefault=True) 

class Form(BaseComponent):
    py_requires="""gnrcomponents/dynamicform/dynamicform:DynamicForm,
                   gnrcomponents/attachmanager/attachmanager:AttachManager"""

    #def th_form(self, form):
    #    
    #    pane = form.record
    #    fb = pane.formbuilder(cols=2, border_spacing='4px')
    #    fb.field('ente_id' )
    #    fb.field('data' )
    #    fb.field('prot' )
    #    fb.field('descrizione' )
    #    fb.field('tipo_doc_id' )

    def th_form(self, form):
        bc = form.center.borderContainer()
        self.Documenti(bc.borderContainer(region='top',datapath='.record',height='125px', splitter=True))
        tc = bc.tabContainer(region='center',margin='2px')
        self.allegatiDoc(tc.contentPane(title='Allegati'))
       # self.extra(tc.contentPane(title='Extra', datapath='.record'))
    
    def allegatiDoc(self,pane):
        pane.attachmentMultiButtonFrame()

    def Documenti(self,bc):
        left = bc.roundedGroup(region='center',title='!![it]Documenti').div(margin='10px',margin_right='20px')
        fb = left.formbuilder(cols=4, border_spacing='4px',colswidth='auto',fld_width='100%',width='100%')
        fb.field('data' )
        fb.field('prot' )
        fb.field('ente_id',hasDownArrow=True )
        fb.field('tipo_doc_id',hasDownArrow=True )
        fb.field('descrizione', colspan=4 , height='30px', tag='textArea')
        fb.appendDynamicFields('extra')

    #def extra(self,pane):
    #    pane.dynamicFieldsPane('extra')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )

    