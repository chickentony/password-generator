from typing import Dict
from string import ascii_lowercase, ascii_uppercase, punctuation


class CheckPasswordComplexity:
    STRENGTH_PASSWORD_LENGTH = 8

    def __init__(self):
        self._password_complexity = {
            "weak": False,
            "normal": False,
            "strength": False
        }

    # @property
    # def password_complexity(self):
    #     return self._password_complexity

    # @password_complexity.setter
    def set_password_complexity(self, key, value):
        self._password_complexity[key] = value

    # @password_complexity.getter
    def get_password_complexity(self) -> str:
        for password_complexity_value, yes_or_no in self._password_complexity.items():
            if yes_or_no:
                return password_complexity_value

    def reset_password_complexity(self) -> None:
        self._password_complexity["weak"] = False
        self._password_complexity["normal"] = False
        self._password_complexity["strength"] = False

    def validate_rules_for_strength_complexity(
            self,
            password_length: int,
            possible_password_chars: Dict[str, bool]
    ) -> None:
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and
                possible_password_chars["special_chars"] and
                possible_password_chars["lowercase_letters"] and
                possible_password_chars["uppercase_letters"] and
                possible_password_chars["numbers"]
        ):
            self.set_password_complexity("strength", True)

    def validate_rules_for_normal_complexity(
            self,
            password_length: int,
            possible_password_chars: Dict[str, bool]
    ) -> None:
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and
                possible_password_chars["lowercase_letters"] and
                possible_password_chars["uppercase_letters"] and
                possible_password_chars["numbers"] and not
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("normal", True)
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and
                possible_password_chars["lowercase_letters"] and
                possible_password_chars["numbers"] and not
                possible_password_chars["uppercase_letters"] and not
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("normal", True)

    def validate_rules_for_weak_complexity(self, password_length, possible_password_chars) -> None:
        if (
                password_length < self.STRENGTH_PASSWORD_LENGTH and not
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("weak", True)

    def validate_password(self, password: str):
        password_complexity = {
            "special_chars": any(char in punctuation for char in password),
            "numbers": any(
                char in ["0", "1", "2", "3", "4", "5", "6", "7", '8', "9"] for char in password
            ),
            "uppercase_letters": any(char in ascii_uppercase for char in password),
            "lowercase_letters": any(char in ascii_lowercase for char in password)
        }
        password_length = len(password)

        self.validate_rules_for_strength_complexity(password_length, password_complexity)
        self.validate_rules_for_normal_complexity(password_length, password_complexity)
        self.validate_rules_for_weak_complexity(password_length, password_complexity)

        print(f"Debug: {self._password_complexity}")

        return self.get_password_complexity()
