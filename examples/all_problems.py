class Boolean:
    pass


class Column:
    def __init__(self, type_=None):
        pass


class Integer:
    pass


class RedefinedColumnsModel:
    __table_name__ = "redefined_columns_model"
    duplicate = Column(Integer, nullable=True, index=False)
    col_1 = Column()
    col_2 = Column()
    duplicate = Column(Boolean)


false_positive = True
false_positive = False
