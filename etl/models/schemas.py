class ColumnSchema:
    def __init__(
        self,
        name,
        dtype=None,
        critical=False,
        nullable=True,
        standardizable=False
    ):
        self.name = name
        self.dtype = dtype
        self.nullable = nullable
        self.critical = critical
        self.standardizable = standardizable

    # @property
    # def name(self):
    #     return self._name

    # @property
    # def dtype(self):
    #     return self._dtype

    # @property
    # def nullable(self):
    #     return self._nullable

    # @property
    # def critical(self):
    #     return self._critical

    # @property
    # def standardizable(self):
    #     return self._standardizable


class TableSchema:

    def __init__(
            self, 
            table_name, 
            columns, 
            primary_key
            ):
        
        self.table_name = table_name

        self.columns = {
            column.name: column
            for column in columns
        }

        self.primary_key = primary_key

    # @property
    # def table_name(self):
    #     return self._table_name

    # @property
    # def columns(self):
    #     return self._columns

    # @property
    # def primary_key(self):
    #     return self._primary_key



    # def get_column(self, name):
    #     return self.columns.get(name)

    def get_critical_columns(self):
        return [
            column.name
            for column in self.columns.values()
            if column.critical
        ]

    def get_primary_key(self):
        return self.primary_key

    def get_standardizable_columns(self):
        return [
            column.name
            for column in self.columns.values()
            if column.standardizable
        ]