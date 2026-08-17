import pandas as pd

from models.schemas import TableSchema


class DataDeduplicator:
    def deduplicate(self, df: pd.DataFrame, schema: TableSchema) -> pd.DataFrame:
        """
        Deduplicate a table based on its schema.

        If a table has custom deduplication logic, use it.
        Otherwise, fall back to drop_duplicates().
        """

        handlers = {
            "geolocation": self._deduplicate_geolocation,
        }

        handler = handlers.get(schema.table_name)

        if handler:
            return handler(df)

        return df.drop_duplicates()

    def deduplicate_geolocation(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Deduplicate geolocation records by ZIP code.

        Multiple coordinates for the same ZIP code are averaged.
        The first city and state are retained.
        """

        return (
            df.groupby("geolocation_zip_code_prefix", as_index=False)
            .agg(
                geolocation_lat=("geolocation_lat", "mean"),
                geolocation_lng=("geolocation_lng", "mean"),
                geolocation_city=("geolocation_city", "first"),
                geolocation_state=("geolocation_state", "first"),
            )
        )