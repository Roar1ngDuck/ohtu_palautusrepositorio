from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query = All()):
        self._query = query

    def build(self):
        return self._query
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))
    
    def plays_in(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))
    
    def one_of(self, *matchers):
        return QueryBuilder(Or(*matchers))