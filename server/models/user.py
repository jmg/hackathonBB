from models.base import BaseModel
from models.tag import Tag


class User(BaseModel):

    __PRIMARY_KEY__ = 'username'

    not_empty_fields = ['username', 'password', 'email']

    def progress(self):
        from models.expense import Expense
        from models.expectation import Expectation

        expenses = Expense.all(user_id=self['_id'])
        savings = [ x for x in expenses if Tag.get(_id=x['tag_id'])['name'] == 'saving' ]
        expectation = Expectation.get(user_id=self['_id'])

        total_savings = sum(float(x['cost']) for x in savings)

        return int((float(expectation['cost']) - total_savings * 100) / float(expectation['cost']))
