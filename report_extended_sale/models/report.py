# -*- coding: utf-8 -*-
##############################################################################
#
#    Ingenieria ADHOC - ADHOC SA
#    https://launchpad.net/~ingenieria-adhoc
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields
from openerp.tools.translate import _

class ir_actions_report(osv.Model):
    _inherit = 'ir.actions.report.xml'
    
    _columns = {    
        'sale_order_state': fields.selection([('draft', 'Quotation'),
                                              ('progress', 'In Progress')], 'Sale Order State', required=False),
    }
    
    _defaults = {
    }

    def get_domains(self, cr, model, record, context=None):
        domains = super(ir_actions_report, self).get_domains(cr, model, record, context=context)
        if record.state in ['draft','sent']:
            sale_order_state = 'draft'
        else:
            sale_order_state = 'progress'        
        if model == 'sale.order':    
            # Search for especific report            
            domains.append([('sale_order_state','=',sale_order_state)])
            # Search without state defined
            domains.append([('sale_order_state','=',False)])
        return domains
