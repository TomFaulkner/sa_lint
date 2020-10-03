class Boolean:
    pass


class Column:
    def __init__(self, type_=None):
        pass


class Integer:
    pass


class AllTheProblemsModel:
    __table_name__ = "all_the_problems"
    not_a_duplicate = Column(Integer)
    col_1 = Column()
    col_2 = Column()
    original = Column(Boolean)


false_positive = True
false_positive = False
