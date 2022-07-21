{
    "name": "Preprinted Report Py3o",
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
    "depends": ["report_py3o"],
    "data": [
        "views/stock_picking_view.xml",
        "report/invoice_report.xml",
    ],
}
