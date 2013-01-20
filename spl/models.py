# -*- coding: utf-8 -*-

import re
from datetime import datetime
from flask.ext.mongokit import MongoKit, Document

db = MongoKit()

_email_re = re.compile(r'(?:^|\s)[-a-z0-9_a.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)', re.IGNORECASE)

def email_validator(value):
    return bool(_email_re.match(value))


def configure_db(app):
    db.init_app(app)


class Model(Document):

    use_dot_notation = True
    use_schemaless = True
    use_autorefs = True


@db.register
class Contact(Model):
    __collection__ = 'contact'

    structure = {
        'name': basestring,
        'phone': basestring,
        'email': basestring,
    }

    required_fields = ['name']
    validators = {
        'email': email_validator,
    }


@db.register
class Supplier(Model):
    __collection__ = 'supplier'

    FREIGHT_SUPPLIER = u'FREIGHT_SUPPLIER'
    FREIGHT_CUSTOMER = u'FREIGHT_CUSTOMER'

    _freight_types = {
        FREIGHT_SUPPLIER: u'Flete de proveedor',
        FREIGHT_CUSTOMER: u'Flete de cliente',
    }

    structure = {
        'name': unicode,
        'cuit': unicode,
        'iibb': unicode,
        'phone': unicode,
        'fax': unicode,
        'email': unicode,
        'web': unicode,
        'address': unicode,
        'zip_code': unicode,
        'term': int,
        'account_number': unicode,
        'freight_type': unicode, # TODO: use the right type
        'notes': unicode,
        'created_at': datetime,

        'contacts': [{
            'role': unicode,
            'contact': Contact,
        }],
    }
    required_fields = ['name']
    indexes = [{'fields': ['name']}]
    default_values = {
        'created_at': datetime.now,
    }


class PurchaseDocument(Model):
    pass

class PurchaseOrder(Model):
    pass
