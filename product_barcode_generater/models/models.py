# -*- coding: utf-8 -*-

import os
import base64
import barcode
from PIL import Image
from barcode import generate
from openerp import models, fields, api
from openerp import api, tools, SUPERUSER_ID
from barcode.writer import ImageWriter

class Product(models.Model):
    _inherit = 'product.template'

    barcode_img = fields.Binary('Barcode')

    def _get_barcode(self, data):
        # name = generate('EAN13', barcode, output='barcode')
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(data, writer=ImageWriter())
        name = ean.save('ean13_barcode')
        filetmp = os.getcwd()+'/'+name
        im = Image.open(filetmp)
        size = 180, 180
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(filetmp, "JPEG")
        with open(filetmp, "rb") as image_file:
            encoded_string=base64.b64encode(image_file.read())
        return encoded_string


    @api.model
    def create(self, vals):
        barcode = vals.get('barcode')
        if barcode:
            barocde_str = self._get_barcode(barcode)
            vals['barcode_img'] = unicode(barocde_str, "utf-8")
        tools.image_resize_images(vals)
        result = super(Product, self).create(vals)
        return result

        bc = barcode('qrcode','Hello Barcode Writer In Pure PostScript.',options=dict(version=9, eclevel='M'), margin=10, data_mode='8bits')