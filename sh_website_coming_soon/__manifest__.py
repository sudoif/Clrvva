# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Website Coming Soon",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Website",
    "summary": """
Website Coming Soon Template Website Under Processing Template
Website Creative Template Modern Template Cool Template
Vibrant Template Website Maintenance Mode Comming Soon
Under Construction Auto Launch Odoo
""",
    "description": """
Don’t settle for a simple "Coming Soon" template when you could use
one of these to really get customers talking!here is a creative, modern,
and vibrant “coming soon” template, and you can also
customize the template like text, background image etc,
Website Coming Soon/Under Processing Template Odoo.
creative,Modern,Cool & Vibrant Coming Soon Template Module,
Feature of Website Maintenance / Under Construction Template Odoo  .
Website Creative Template App, Modern Template, Cool Template,
Vibrant Template Odoo, Website Maintenance Module.
""",
    "version": "16.0.1",
    "depends": [
        "website",
        "portal"
    ],
    "application": True,
    "data": [
        "views/res_config_settings_view.xml",
        "views/website_view.xml",
        "views/sh_website_coming_soon_templates.xml",
    ],
    'assets': {
        'web.assets_frontend': [
            'sh_website_coming_soon/static/src/css/animate.css',
            'sh_website_coming_soon/static/src/css/coming_soon.css',
            'sh_website_coming_soon/static/src/js/countdown.js'
        ]
    },
    "images": ["static/description/background.png", ],
    "auto_install": False,
    "installable": True,
    "price": 25,
    "currency": "EUR",
    "license": "OPL-1"
}
