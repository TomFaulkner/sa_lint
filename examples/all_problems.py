class Boolean:
    pass


class Column:
    def __init__(self, type_=None):
        pass


class Integer:
    pass


class AllTheProblemsModel:
    __table_name__ = "all_the_problems"
    duplicate = Column(Integer)
    col_1 = Column(nullable=True)
    col_2 = Column(index=False)
    duplicate = Column(Boolean)


false_positive = True
false_positive = False
