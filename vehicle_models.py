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

class VehicleData(models.Model):
    _name = 'vehicle.data'
    _description = 'Data Kendaraan'
    name = fields.Char('Model Kendaraan')
    license_plate = fields.Char('Plat No. Kendaraan')
    image = fields.Binary('Gambar')
    company_id = fields.Many2one('res.company', 'Perusahaan')
    division = fields.Char('Divisi')
    location = fields.Char('Lokasi Kendaraan')
    vehicle_type = fields.Char('Jenis Kendaraan')
    year = fields.Char('Tahun Kendaraan')
    driver = fields.Char('Pengemudi')
    chassis_number = fields.Char('No. Rangka')
    engine_number = fields.Char('No. Mesin')
    last_odometer = fields.Float('Odometer Terakhir')
    fuel_type = fields.Char('Bahan Bakar')
    transmission = fields.Char('Transmisi')
    purchase_date = fields.Char('Tanggal Pembelian')
    price = fields.Float('Harga Kendaraan')
    seats = fields.Integer('Tempat Duduk')
    doors = fields.Integer('Pintu')
    color = fields.Char('Warna')
    contract_ids = fields.One2many('vehicle.contract', 'vehicle_id', 'Contracts')
    cost_ids = fields.One2many('vehicle.cost', 'vehicle_id', 'Costs')
    service_ids = fields.One2many('vehicle.service', 'vehicle_id', 'Services')
    fuel_ids = fields.One2many('vehicle.fuel', 'vehicle_id', 'Fuel')
    odometer_ids = fields.One2many('vehicle.odometer', 'vehicle_id', 'Odometer')
    total_cost = fields.Float(string='Total Biaya', compute='_compute_total_cost', store=True)

    def _compute_total_cost(self):
        for record in self:
            record.total_cost = sum(record.cost_ids.mapped('amount'))

class VehicleContract(models.Model):
    _name = 'vehicle.contract'
    _description = 'Kontrak Kendaraan'
    contract_number = fields.Char('Nomor Kontrak')
    vehicle_id = fields.Many2one('vehicle.data', 'Kendaraan')
    start_date = fields.Date('Tanggal Mulai')
    end_date = fields.Date('Tanggal Selesai')
    partner_id = fields.Many2one('res.partner', 'Mitra')
    notes = fields.Text('Keterangan')
    attachment = fields.Binary('Lampiran')
    cost_ids = fields.One2many('vehicle.cost', 'vehicle_id', 'Costs')

class VehicleOdometer(models.Model):
    _name = 'vehicle.odometer'
    _description = 'Odometer Kendaraan'
    vehicle_id = fields.Many2one('vehicle.data', 'Kendaraan')
    odometer_value = fields.Float('Odometer')
    date = fields.Date('Tanggal')
    notes = fields.Text('Keterangan')
    cost_ids = fields.One2many('vehicle.cost', 'vehicle_id', 'Costs')

class VehicleFuel(models.Model):
    _name = 'vehicle.fuel'
    _description = 'Bahan Bakar Kendaraan'
    vehicle_id = fields.Many2one('vehicle.data', 'Kendaraan')
    fuel_type = fields.Char('Jenis Bahan Bakar')
    liter = fields.Float('Liter')
    price_per_liter = fields.Float('Harga per Liter')
    total_price = fields.Float('Total Harga')
    date = fields.Date('Tanggal')
    vendor_id = fields.Many2one('res.partner', 'Vendor')
    notes = fields.Text('Keterangan')
    cost_ids = fields.One2many('vehicle.cost', 'vehicle_id', 'Costs')

class VehicleService(models.Model):
    _name = 'vehicle.service'
    _description = 'Service Kendaraan'
    vehicle_id = fields.Many2one('vehicle.data', 'Kendaraan')
    service_type = fields.Char('Jenis Service')
    date = fields.Date('Tanggal')
    vendor_id = fields.Many2one('res.partner', 'Vendor')
    cost = fields.Float('Biaya Service')
    notes = fields.Text('Keterangan')
    cost_ids = fields.One2many('vehicle.cost', 'vehicle_id', 'Costs')

class VehicleCost(models.Model):
    _name = 'vehicle.cost'
    _description = 'Biaya-biaya Kendaraan'
    vehicle_id = fields.Many2one('vehicle.data', 'Kendaraan')
    cost_type = fields.Char('Jenis Biaya')
    amount = fields.Float('Jumlah')
    date = fields.Date('Tanggal')
    notes = fields.Text('Keterangan')
    company_id = fields.Many2one('res.company', string='Perusahaan', related='vehicle_id.company_id', store=True)
    division = fields.Char(string='Divisi', related='vehicle_id.division', store=True)
    kendaraan_name = fields.Char(string='Kendaraan', related='vehicle_id.name', store=True)
