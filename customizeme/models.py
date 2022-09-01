from odoo import fields, models


class CustomizeMeProduct(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    customizeme_product_url = fields.Char(string='Product link')
    customizeme_product_custom_inject_to = fields.Char(
        string='Custom inject to', help='You can override here option "Inject to" from CustomizeMe settings for this product.')
    customizeme_attribute_line_ids = fields.One2many(
        'product.template.attribute.line', 'product_tmpl_id', 'Customizeme Product Attributes', copy=True)


class CustomizeMeAttribute(models.Model):
    _name = 'product.template.attribute.line'
    _inherit = 'product.template.attribute.line'

    customizeme_attribute_type = fields.Selection([
        ('suggestion', 'Set suggestion'),
        ('material', 'Set material to part'),
        ('optionalPart', 'Set optional part to part')],
        default='material',
        string='Reaction type',
        help='What should happen on attribute change'
    )
    customizeme_attribute_part_name = fields.Char(
        string='Part name', help='Responding 3D model part name (you can ignore it for type: suggestion)')


class CustomizeMeSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    customizeme_access_key = fields.Char(string='Access key')
    customizeme_inject_to = fields.Char(
        string='Inject to', help='Pseudo selector of element to which CustomizeMe should be added. Let it empty to add CustomizeMe before product details.')

    def set_values(self):
        res = super(CustomizeMeSettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'customizeme.customizeme_access_key', self.customizeme_access_key)
        self.env['ir.config_parameter'].set_param(
            'customizeme.customizeme_inject_to', self.customizeme_inject_to)
        return res

    def get_values(self):
        res = super(CustomizeMeSettings, self).get_values()
        res.update(customizeme_access_key=self.env['ir.config_parameter'].sudo(
        ).get_param('customizeme.customizeme_access_key'))
        res.update(customizeme_inject_to=self.env['ir.config_parameter'].sudo(
        ).get_param('customizeme.customizeme_inject_to'))
        return res
