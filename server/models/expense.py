from models.movement import Movement
from models.tag import Tag


class Expense(Movement):

    not_empty_fields = Movement.not_empty_fields

    def validate(self):
        super(Expense, self).validate()
        self.validate_existance('tag_id', Tag)

