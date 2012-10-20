from models.movement import Movement
from models.tag import Tag


class Expense(Movement):

    not_empty_fields = Movement.not_empty_fields

    def validate(self):
        super(Expense, self).validate()
        self.validate_existance('tag_id', Tag)

    @classmethod
    def top(cls, tag=None, **kwargs):
        if tag is not None:
            kwargs['tag_id'] = Tag.get(name=tag)['_id']

        expenses = sorted(cls.all(**kwargs), key=lambda x: float(x['cost']), reversed=True)

        return expenses[:5]

