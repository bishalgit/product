# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, tools, exceptions, _
from openerp.osv.orm import BaseModel


class IrModelAccess(models.Model):

    _inherit = 'ir.model.access'

    @tools.ormcache_context(
        'uid', 'model', 'mode', 'raise_exception', keys=('lang',))
    def check(
            self, cr, uid, model, mode='read', raise_exception=True,
            context=None):

        if isinstance(model, BaseModel):
            assert model._name == 'ir.model', 'Invalid model object'
            model_name = model.model
        else:
            model_name = model

        if mode != 'read' and model_name in [
                'product.template', 'product.product']:
            if self.pool['res.users'].has_group(
                    cr, uid,
                    'product_management_group.group_products_management'):
                return True
            elif raise_exception:
                raise exceptions.AccessError(_(
                    "Sorry, you are not allowed to manage products."
                    "Only users with 'Products Management' level are currently"
                    " allowed to do that"))
            else:
                return False
        return super(IrModelAccess, self).check(
            cr, uid, model, mode=mode, raise_exception=raise_exception,
            context=context)
