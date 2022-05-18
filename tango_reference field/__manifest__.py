{
    "name": "Tango Reference Field",
    "summary": """ This module adds the tango reference field to products
        """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["AndresAndrade"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ['product', 'base', 'stock'],
    "data": [
        'views/product_template_view.xml',
    ],
}
