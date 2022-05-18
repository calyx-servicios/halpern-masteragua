# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Report Sale Custom",
    "summary": """
        Report Sale Custom""",
    "author": "Calyx Servicios S.A.",
    "maintainers": ["GeorginaGuzman"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ['sale',],
    "data": [
        "view/template.xml",
    ],
}
