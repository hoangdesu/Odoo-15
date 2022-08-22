from odoo import api, fields, models, tools

class HospitalPatient(models.Model):
    _name = "hospital.patient"  # odoo creates a db table with the name "hospital_patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender")
