import pandas as pd

from models.schemas import TableSchema


class DataStandardization:

    def trim_whitespace(self, df: pd.DataFrame):
        """
        Remove leading and trailing whitespace from all string columns.
        """

        df = df.copy()

        string_columns = df.select_dtypes(include=["object", "string"]).columns

        for column in string_columns:
            df[column] = df[column].str.strip()

        return df

    def convert_empty_strings_to_null(self, df: pd.DataFrame):
        """
        Replace empty strings and whitespace-only strings with NULL.
        """

        df = df.copy()

        string_columns = df.select_dtypes(include=["object", "string"]).columns

        for column in string_columns:
            df[column] = (
                df[column]
                .replace(r'^\s*$', pd.NA, regex=True)
            )

        return df

    def standardize_text_case(self, df: pd.DataFrame, schema: TableSchema):
        """
        Convert all string values to lowercase.
        """

        df = df.copy()

        standardizable_columns = schema.get_standardizable_columns()

        ss_columns = (
            df.select_dtypes(include=["object", "string"])
            .columns
            .intersection(standardizable_columns)
        )

        for column in ss_columns:
            df[column] = df[column].str.lower()

        return df

    def remove_duplicate_spaces(self, df: pd.DataFrame):
        """
        Replace multiple consecutive spaces with a single space.
        """

        df = df.copy()

        string_columns = df.select_dtypes(include=["object", "string"]).columns

        for column in string_columns:
            df[column] = (
                df[column]
                .str.replace(r"\s+", " ", regex=True)
            )

        return df