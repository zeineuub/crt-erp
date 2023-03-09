from odoo import models, fields, api
from odoo.exceptions import ValidationError
from validate_email import validate_email
class HR(models.Model):
    _name = "volunteer.management"
    _description ="Volunteers management in red crescent"
    cin = fields.Char(required=True,size=8)



    def _check_cin(self):
        for record in self:
            if not record.cin.isdigit() or len(record.cin) != 8:
                raise ValidationError("CIN must be a string of 8 digits")

    firstName = fields.Char(required=True)
    lastName = fields.Char(required=True)
    birthdate = fields.Date(required=True)
    DOMAINE_SELECTION = [
        ('computer science', 'Computer Science'),
        ('law', 'Law'),
        ('biology', 'Biology'),
        ('management', 'Management'),
        ('management', 'Management'),
        ('nursing sciences', 'Nursing Sciences'),
        ('high school students','High school students'),
        ('other specialties','Other Specialties')
    ]
    domain = fields.Selection(DOMAINE_SELECTION)
    membership = fields.Boolean(required=True)
    GENDER_SELECTION = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = fields.Selection(GENDER_SELECTION, widget='radio',)

    phoneNumber = fields.Char(required=True,size=8, index=True)
    @api.constrains('phoneNumber')
    def _check_phonenumber(self):
        for record in self:
            if not record.phoneNumber.isdigit() or len(record.phoneNumber) != 8:
                raise ValidationError("PhoneNumber must be a string of 8 digits")

    email = fields.Char(required=True)

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and not validate_email(record.email):
                raise ValidationError("The email address is invalid")
    def add_volunteer(self, volunteer_data):
        hr = self.create(volunteer_data)
        return hr

    def update_vonunteer(self, volunteer_data):
        self.write(volunteer_data)
        return True

    def delete_volunteer(self):
        self.unlink()
        return  True

    def save_volunteer(self):
        self.ensure_one()

        if self.id:
            self.update_volunteer({
                'cin': self.cin,
                'firstName': self.firstName,
                'lastname': self.lastname,
                'gender': self.gender,
                'phoneNumber': self.phoneNumber,
                'birthdate': self.birthdate,
                'email': self.email,
                'domain': self.domain,
                'membership': self.membership,
            })
        else:
            self.add_volunteer({
                'cin': self.cin,
                'firstName': self.firstName,
                'lastName': self.lastName,
                'gender': self.gender,
                'phoneNumber': self.phoneNumber,
                'birthdate': self.birthdate,
                'email': self.email,
                'domain': self.domain,
                'membership': self.membership,
            })
