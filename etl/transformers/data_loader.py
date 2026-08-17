import pandas as pd


class SilverLoader:

    def __init__(self, engine, source_table_configs, target_table_configs):
        """
        Parameters
        ----------
        engine : SQLAlchemy Engine
            PostgreSQL connection engine.
        """
        self.engine = engine
        self.source_table_configs = source_table_configs
        self.target_table_configs = target_table_configs

    def transform(self):

        # Generic transformations
        for table in [
            "orders",
            "order_items",
            "order_payments",
            "order_reviews",
            "geolocation"
        ]:
            self.transform_generic(table)

        # Table-specific transformations
        self.transform_customers()
        self.transform_sellers()
        self.transform_products()

        return self.target_table_configs

    def transform_generic(self, table_name):
        df, _ = self.source_table_configs[table_name]
        _, schema = self.target_table_configs[table_name]

        df = self._select_schema_columns(df, schema)

        self.target_table_configs[table_name] = (df, schema)

    def transform_customers(self):
        df, _ = self.source_table_configs["customers"]
        _, schema = self.target_table_configs["customers"]

        df = df.drop(
            columns=["customer_city", "customer_state"],
            errors="ignore"
        )

        df = self._select_schema_columns(df, schema)

        self.target_table_configs["customers"] = (df, schema)

    def transform_sellers(self):
        df, _ = self.source_table_configs["sellers"]
        _, schema = self.target_table_configs["sellers"]

        df = df.drop(
            columns=["seller_city", "seller_state"],
            errors="ignore"
        )

        df = self._select_schema_columns(df, schema)

        self.target_table_configs["sellers"] = (df, schema)


    def transform_products(self):
        products_df, _ = self.source_table_configs["products"]
        translation_df, _ = self.source_table_configs["product_category_translation"]
        _, silver_schema = self.target_table_configs["products"]

        products_df = (
            products_df
            .merge(
                translation_df,
                on="product_category_name",
                how="left",
            )
            .drop(columns=["product_category_name"])
            # .rename(
            #     columns={
            #         "product_category_name_english": "product_category_name"
            #     }
            # )
        )

        products_df = self._select_schema_columns(
            products_df,
            silver_schema,
        )

        self.target_table_configs["products"] = (
            products_df,
            silver_schema,
        )


    def _select_schema_columns(self, df, schema):
        """
        Keep only columns defined in the Silver schema.
        """

        columns = list(schema.columns)

        missing = set(columns) - set(df.columns)
        if missing:
            raise ValueError(
                f"Schema expects columns {missing}, "
                f"but DataFrame only has {df.columns.tolist()}"
            )


        return df[columns]

    def load(self, df: pd.DataFrame, target_table: str):
        """
        Load transformed dataframe into the specified table.
        """

        df.to_sql(
            name=target_table,
            con=self.engine,
            schema="silver",
            if_exists="append",
            index=False
        )

    def run(self, load_sequence: list):
        """
        Full Bronze → Silver pipeline for customers.
        """

        transformed_configs = self.transform()

        for table_name in load_sequence:
            df, _ = transformed_configs[table_name]
            self.load(df, table_name)

            print(f"Loaded {len(df)} rows into {table_name}.")