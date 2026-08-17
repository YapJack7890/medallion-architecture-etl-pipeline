import pandas as pd

from models.schemas import TableSchema


class DataIntegrityRule:

    def _check_null_columns(
        self,
        df: pd.DataFrame,
        columns: list[str]
    ) -> dict:
        """
        Generic NULL validation for a list of columns.

        Returns:
            {
                "passed": bool,
                "null_columns": list[str],
                "null_counts": dict[str, int],
                "null_rows": DataFrame | None
            }
        """

        null_columns = []
        null_counts = {}
        null_rows = []

        for column in columns:

            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found in DataFrame.")

            null_count = int(df[column].isna().sum())

            if null_count > 0:
                null_columns.append(column)
                null_counts[column] = null_count
                null_rows.append(df[df[column].isna()])

        if null_rows:
            null_rows = pd.concat(null_rows).drop_duplicates()
        else:
            null_rows = None

        return {
            "passed": len(null_columns) == 0,
            "null_columns": null_columns,
            "null_counts": null_counts,
            "null_rows": null_rows,
        }

    def check_null_pk(self, df: pd.DataFrame, schema: TableSchema):

        pk_columns = schema.get_primary_key()

        if not pk_columns:
            raise ValueError(
                f"No primary key defined for table '{schema.table_name}'."
            )

        result = self._check_null_columns(df, pk_columns)

        return {
            "passed": result["passed"],
            "primary_key": pk_columns,
            "null_count": sum(result["null_counts"].values()),
            "null_rows": result["null_rows"],
        }

    def check_null_critical(self, df: pd.DataFrame, schema: TableSchema):

        critical_columns = schema.get_critical_columns()

        if not critical_columns:
            raise ValueError(
                f"No critical columns defined for table '{schema.table_name}'."
            )

        result = self._check_null_columns(df, critical_columns)

        return {
            "passed": result["passed"],
            "critical_columns": critical_columns,
            "null_count": sum(result["null_counts"].values()),
            "null_rows": result["null_rows"],
        }

    def check_duplicate_pk(self, df: pd.DataFrame, schema: TableSchema):
        """
        Check whether the primary key contains duplicate values.

        Returns:
            dict:
            {
                "passed": bool,
                "primary_key": list[str],
                "duplicate_count": int,
                "duplicate_rows": DataFrame
            }
        """

        pk_columns = schema.get_primary_key()

        if not pk_columns:
            raise ValueError(
                f"No primary key defined for table '{schema.table_name}'."
            )

        for column in pk_columns:
            if column not in df.columns:
                raise ValueError(
                    f"Primary key column '{column}' not found in DataFrame."
                )

        duplicate_rows = df[
            df.duplicated(subset=pk_columns, keep=False)
        ]

        return {
            "passed": duplicate_rows.empty,
            "primary_key": pk_columns,
            "duplicate_count": len(duplicate_rows),
            "duplicate_rows": duplicate_rows
        }

    def check_duplicate_rows(self, df: pd.DataFrame):
        """
        Check whether required columns contain duplicate values.

        Returns:
            {
                "passed": bool,
                "duplicate_counts": dict[str, int],
                "duplicate_rows": DataFrame | None
            }
        """

        duplicate_counts = 0

        duplicate_count = int(df.duplicated().sum())

        duplicated_rows = df[df.duplicated(keep=False)] if duplicate_count > 0 else None

        return {
            "passed": duplicate_counts == 0,
            "duplicate_counts": duplicate_counts,
            "duplicate_rows": duplicated_rows
        }

    def remove_null_rows(self, df, schema):
        """
        Remove rows containing NULL values in required (non-nullable) columns.

        Returns:
            cleaned_df
        """

        required_columns = [
            column.name
            for column in schema.columns.values()
            if not column.nullable
        ]

        cleaned_df = df.dropna(subset=required_columns)

        return cleaned_df

    def remove_duplicate_rows(self, df):
        """
        Remove duplicate rows.

        Returns:
            cleaned_df
        """

        cleaned_df = df.drop_duplicates()

        return cleaned_df

