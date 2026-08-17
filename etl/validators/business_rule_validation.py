import pandas as pd


class BusinessRuleValidation:

    VALID_BRAZIL_STATES = {
        "AC", "AL", "AP", "AM", "BA", "CE", "DF",
        "ES", "GO", "MA", "MT", "MS", "MG", "PA",
        "PB", "PR", "PE", "PI", "RJ", "RN", "RS",
        "RO", "RR", "SC", "SP", "SE", "TO"
    }

    def validate_state_codes(self, df: pd.DataFrame):

        # if "geolocation_state" not in df.columns:
        #     return {"passed": True, "invalid_rows": []}

        invalid = df[
            ~df["geolocation_state"].isin(self.VALID_BRAZIL_STATES)
        ]

        return {
            "passed": invalid.empty,
            "invalid_rows": invalid.index.tolist()
        }

    def validate_zip_codes(self, df: pd.DataFrame):

        if "geolocation_zip_code_prefix" not in df.columns:
            return {"passed": True, "invalid_rows": []}

        invalid = df[
            (df["geolocation_zip_code_prefix"] < 1000) |
            (df["geolocation_zip_code_prefix"] > 99999)
        ]

        return {
            "passed": invalid.empty,
            "invalid_rows": invalid.index.tolist()
        }

    def validate_payment_amount(self, df: pd.DataFrame):

        if "payment_value" not in df.columns:
            return {"passed": True, "invalid_rows": []}

        invalid = df[
            df["payment_value"] < 0
        ]

        return {
            "passed": invalid.empty,
            "invalid_rows": invalid.index.tolist()
        }

    def validate_review_score(self, df: pd.DataFrame):

        if "review_score" not in df.columns:
            return {"passed": True, "invalid_rows": []}

        invalid = df[
            ~df["review_score"].between(1, 5)
        ]

        return {
            "passed": invalid.empty,
            "invalid_rows": invalid.index.tolist()
        }

    def validate_delivery_dates(self, df: pd.DataFrame):

        required = {
            "order_purchase_timestamp",
            "order_delivered_customer_date"
        }

        if not required.issubset(df.columns):
            return {"passed": True, "invalid_rows": []}

        purchase = pd.to_datetime(
            df["order_purchase_timestamp"]
        )

        delivery = pd.to_datetime(
            df["order_delivered_customer_date"]
        )

        invalid = df[
            delivery < purchase
        ]

        return {
            "passed": invalid.empty,
            "invalid_rows": invalid.index.tolist()
        }