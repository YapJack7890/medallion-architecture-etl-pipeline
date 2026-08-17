from models.validation_result import ValidationResult


class SchemaValidationRule:

    def validate_missing(self, df, schema):

        result = ValidationResult()

        for column in schema.columns.values():

            if (
                column.critical
                and column.name not in df.columns
            ):

                result.missing.append(column.name)

                if column.critical:
                    result.critical_missing.append(column.name)
                else:
                    result.optional_missing.append(column.name)

        return result

    
    def validate_unexpected(self, df, schema):

        expected_columns = set(schema.columns.keys())
        actual_columns = set(df.columns)

        unexpected = list(actual_columns - expected_columns)

        return unexpected