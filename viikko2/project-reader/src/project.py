class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify(self, items):
        return "\n- ".join(items) if len(items) > 0 else "\n"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n\nAuthors: {self._stringify(self.authors)}"
            f"\n\nDependencies: {self._stringify(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify(self.dev_dependencies)}"
        )
