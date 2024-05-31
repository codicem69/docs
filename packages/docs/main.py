#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='docs package',sqlschema='docs',sqlprefix=True,
                    name_short='Docs', name_long='Docs', name_full='Docs')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    pass
