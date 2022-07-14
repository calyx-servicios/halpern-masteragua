{
    "name": "Preprinted report",
    "summary": """
        Preprinted report""",
    "author": "Calyx Servicios S.A.",
    "maintainers": ["DarwinAndrade"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Report",
    "version": "13.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": ["num2words"], "bin": []},
    "depends": [
    ],
    "data": [
        "view/template.xml",
        "report/stock_report.xml",
        "view/stock_picking_view.xml",
    ],
}
