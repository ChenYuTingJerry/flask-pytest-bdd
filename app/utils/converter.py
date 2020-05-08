import re


class StringConverter:
    @staticmethod
    def to_snake_case(text):
        str1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", text)
        return re.sub("([a-z])([A-Z])", r"\1_\2", str1).lower()

    @staticmethod
    def to_lower_camel_case(text):
        components = text.split("_")
        return components[0] + "".join(x.capitalize() for x in components[1:])

    @staticmethod
    def to_upper_camel_case(text):
        components = text.split("_")
        return "".join(x.capitalize() for x in components)
