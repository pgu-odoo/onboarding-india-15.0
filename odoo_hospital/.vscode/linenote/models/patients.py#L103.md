# reference = fields.Char(string='Seq Number', default=lambda self:self._get_next_patientname(), readonly=True)

    # @api.model
    # def _get_next_patientname(self):
    #     sequence = self.env['ir.sequence'].search([('code','=','patient.sequence')])
    #     next= sequence.get_next_char(sequence.number_next_actual)
    #     return next

    # @api.model
    # def create(self, vals):
    #     # import pdb
    #     # pdb.set_trace()
    #     vals['reference'] = self.env['ir.sequence'].next_by_code('patient.sequence')
    #     result = super(HospitalPatients, self).create(vals)
    #     return result