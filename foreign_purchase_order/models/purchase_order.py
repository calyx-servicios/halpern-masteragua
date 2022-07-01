from odoo import models, fields, api

# VIEW LOCATION foreign_purchase_order.purchase_order_form_foreign_fields
class PurchaseOrder(models.Model):
    _inherit="purchase.order"

    # CONFIRMATION MENU
    confirmation_not_required = fields.Boolean()
    confirmation_number = fields.Char()
    confirmation_date = fields.Date()

    # PAYMENT DATE MENU
    payment_not_required = fields.Boolean()
    payment_provisory_payment_customs_taxes = fields.Float()
    payment_bank_account = fields.Char()
    payment_applicance_number = fields.Char()
    payment_date = fields.Date()
    payment_reference = fields.Char()
    payment_payment_currency = fields.Char()
    payment_payment_method = fields.Selection(selection=[("deferred", "Deferred"),
                                                        ("anticipated", "Anticipated")],
                                                    copy=False)

    payment_TTE_paid_value = fields.Float()
    payment_currency_type = fields.Text()

    # INTERVENTION MENU
    intervention_not_required = fields.Boolean()
    intervention_reference = fields.Char()
    intervention_vep_amount = fields.Char()
    intervention_application_date = fields.Date()
    intervention_currency = fields.Selection(selection=[("eur", "EUR"),
                                                        ("ars", "ARS"),
                                                        ("usd", "USD")],
                                            copy=False)

    intervention_approval_date = fields.Date()
 
    # ORIGIN(SHIP BOOKING) MENU
    booking_not_required = fields.Boolean()
    booking_transportation_means = fields.Many2one(comodel_name="purchase.booking", ondelete="cascade")
    booking_origin = fields.Char()
    booking_etd_date = fields.Date()
    booking_eta_date = fields.Date()
    booking_transport_company = fields.Char()
    booking_name = fields.Char()
    booking_internal_notes = fields.Text()

    # IMPORTATION DISPATCH MENU
    importation_not_required = fields.Boolean()
    importation_dispatch_number = fields.Char()
    importation_officialization_date = fields.Date()
    importation_channel = fields.Many2one(comodel_name="purchase.channel", ondelete="cascade")

    # EXPENSES MENU
    expenses_not_required = fields.Boolean()
    expenses_dispatcher_fees = fields.Char()
    expenses_currency_payment = fields.Selection(selection=[("eur", "EUR"),
                                                            ("ars", "ARS"),
                                                            ("usd", "USD")],
                                                copy=False)

    expenses_forwarder = fields.Char()
    expenses_fiscal_deposit = fields.Char()
    expenses_port_airport = fields.Char()
    expenses_expenses = fields.Char()
    expenses_currency_payment_expenses = fields.Selection(selection=[("eur", "EUR"),
                                                                   ("ars", "ARS"),
                                                                   ("usd", "USD")],
                                                        copy=False)

    # PROFORM MENU
    proform_not_required = fields.Boolean()
    proform_number = fields.Char()
    proform_date = fields.Date()
    proform_incoterm = fields.Selection(selection=[("exw","EXW"),
                                                    ("fca","FCA"),
                                                    ("fob","FOB"),
                                                    ("cif","CIF")],
                                        copy=False)

    proform_payment_method = fields.Selection(selection=[("deferred", "Deferred"),
                                                        ("anticipated", "Anticipated")],
                                                copy=False)

    proform_payment_date = fields.Date()
    proform_currency = fields.Float()
    proform_payment_terms = fields.Char()
    proform_merchandise_weight = fields.Integer()
    proform_packaging = fields.Char()

    proform_treatment = fields.Boolean()

    # DISPATCHER MENU
    dispatcher_not_required = fields.Boolean()
    dispatcher_dispatcher = fields.Many2one(comodel_name="purchase.dispatcher", ondelete="cascade")
    dispatcher_address = fields.Char(related="dispatcher_dispatcher.address")
    dispatcher_email = fields.Char(related="dispatcher_dispatcher.email")
    dispatcher_phone = fields.Char(related="dispatcher_dispatcher.phone")

    # IMPORT LICENSE MENU
    import_license_not_required = fields.Boolean()
    import_license_reference = fields.Char()
    import_license_officialization_date = fields.Date()
    import_license_bank = fields.Char()
    import_license_payment_form = fields.Selection(selection=[("deferred", "Deferred"),
                                                            ("anticipated", "Anticipated")],
                                                    copy=False)

    import_license_possible_payment_date = fields.Date()
    import_license_approval_date = fields.Date()
    import_license_simi = fields.Selection(selection=[("a", "A"),
                                                    ("b", "B"),
                                                    ("la", "LA"),
                                                    ("lna", "LNA")],
                                            copy=False)


    # DOCUMENTS MENU
    document_not_required = fields.Boolean()
    document_commercial_bill_number = fields.Char()
    document_bill_date = fields.Date()
    document_analysis_certificate_approval_date = fields.Date()
    document_original_documentation = fields.Char()
    
    document_origin_certificate = fields.Char()
    document_bl = fields.Boolean()
    document_crt = fields.Boolean()
    document_shipment_document_date = fields.Date()


    # ORIGINAL DOCUMENTATION MENU
    original_not_required = fields.Boolean()
    original_reception_date = fields.Date()
    original_reference = fields.Char()
    original_dispatcher_sending_date = fields.Date()
