{
    "name": "Stock Forecast Report",
    "summary": """ This module adds a custom report to inventory
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
        'views/product_report_views.xml',
        'views/menuitem.xml',
    ],
}
