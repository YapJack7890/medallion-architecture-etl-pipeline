class ValidationResult:

    def __init__(self):
        self.missing = []
        self.critical_missing = []
        self.optional_missing = []

    @property
    def has_errors(self):
        return len(self.critical_missing) > 0