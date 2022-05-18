# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project Custom",
    "summary": """
        This module agregated fields for customise the module project""",
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
    "depends": ['project', 'base',],
    "data": [
        "view/project_view.xml",
    ],
}
