from base import BaseModel


class User(BaseModel):
    __PRIMARY_KEY__ = 'username'

    def validate(self):
        for field in ['username', 'password']:
            self.validate_not_empty(field)
            self.validate_field(field, self.validate_min_length, 6)
            self.validate_field(field, self.validate_max_length, 30)
            self.validate_field(field, self.validate_valid_characters)

        self.validate_not_empty('email')

    def validate_min_length(self, field, min_length):
        return len(self[field]) >= min_length

    def validate_max_length(self, field, max_length):
        return len(self[field]) <= max_length

    def validate_valid_characters(self, field):
        lowercase = [ chr(x) for x in range(97,123) ]
        uppercase = [ x.upper() for x in lowercase ]
        numbers = [ str(x) for x in range(10) ]
        simbols = ["_", "-", "/", "!", "@"]

        valid_chars = lowercase + uppercase + numbers + simbols

        for l in self[field]:
            if l not in valid_chars:
                return False

        return True

