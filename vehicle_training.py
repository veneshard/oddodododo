from odoo import models, fields

class VehicleTraining(models.Model):
    _name = 'vehicle.training'
    _description = 'Training Kendaraan'

    name = fields.Char(string="Nama Training", required=True)
    vehicle_type = fields.Selection([
        ('car', 'Mobil'),
        ('motorcycle', 'Motor'),
        ('truck', 'Truk'),
    ], string="Jenis Kendaraan")
    trainer = fields.Char(string="Instruktur")
    date = fields.Date(string="Tanggal Training")
    notes = fields.Text(string="Catatan")
