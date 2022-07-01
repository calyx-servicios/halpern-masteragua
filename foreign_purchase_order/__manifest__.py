# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Foreign Purchase Order",
    "summary": """
        This module add a notebook page in purchase order for the foreign fields.
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["<lucianobaleani>"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Purchase",
    "version": "13.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["purchase"],
    'data': [
        "security/ir.model.access.csv",
        "views/purchase_booking_views.xml",
        "views/purchase_channel_views.xml",
        "views/purchase_dispatcher_views.xml",
        "views/purchase_menu_extension_views.xml",
        "views/purchase_order_inherited_views.xml",
    ],
}
