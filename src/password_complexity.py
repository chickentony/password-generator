import logging
from typing import Dict
from string import ascii_lowercase, ascii_uppercase, punctuation

from src.constants import LOGGER_NAME


class CheckPasswordComplexity:
    """Check complexity for given password."""

    STRENGTH_PASSWORD_LENGTH = 8

    def __init__(self, password: str):
        """
        Set _password_complexity value after validating given password.

        :param password: generated password by user
        """

        self.logger = logging.getLogger(LOGGER_NAME)
        if not isinstance(password, str):
            self.logger.critical("Invalid argument type %s provided", type(password))
            raise ValueError("Argument must be a string type")
        if len(password) == 0:
            self.logger.critical("Password length are zero")
            raise ValueError("Password length must be bigger than zero")

        self._password_complexity = {
            "weak": False,
            "normal": False,
            "strength": False
        }
        self.validate_password(password)

    def set_password_complexity(self, password_complexity_name: str, yes_or_no: bool) -> None:
        """
        Set value of password_complexity dictionary by provided key.

        :param password_complexity_name: can be weak, normal or strength
        :param yes_or_no: set true or false
        :return: None
        """

        if not isinstance(password_complexity_name, str):
            self.logger.critical(
                "Invalid argument type %s provided", type(password_complexity_name)
            )
            raise ValueError("Argument must be string type")
        if not isinstance(yes_or_no, bool):
            self.logger.critical("Invalid argument type %s provided", type(yes_or_no))
            raise ValueError("Argument must be boolean type")
        if password_complexity_name not in ("weak", "normal", "strength"):
            self.logger.error("Invalid password complexity key name: %s", password_complexity_name)
            raise KeyError("Invalid complexity key name")

        self._password_complexity[password_complexity_name] = yes_or_no

    def get_password_complexity(self) -> str:
        """
        Return value of password_complexity dict keys if its value is true.
        If cant determine complexity return "Unknown" value.

        :return: value of password_complexity dict
        """

        password_complexity = "Unknown"

        for password_complexity_value, yes_or_no in self._password_complexity.items():
            if yes_or_no:
                password_complexity = password_complexity_value

        return password_complexity

    def validate_rules_for_strength_complexity(
            self,
            password_length: int,
            possible_password_chars: Dict[str, bool]
    ) -> None:
        """
        Check password for strength rule. Its valid if choose special chars, numbers, lowercase
        and upper case letters. Also, if password length are more than 8 chars.

        :param password_length:
        :param possible_password_chars: dict of possible password chars, can contains:
        letters, numbers, special chars
        :return: None
        """

        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and
                possible_password_chars["special_chars"] and
                possible_password_chars["lowercase_letters"] and
                possible_password_chars["uppercase_letters"] and
                possible_password_chars["numbers"]
        ):
            self.set_password_complexity("strength", True)
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and
                possible_password_chars["lowercase_letters"] and not
                possible_password_chars["uppercase_letters"] and
                possible_password_chars["numbers"] and
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("strength", True)
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and not
                possible_password_chars["lowercase_letters"] and
                possible_password_chars["uppercase_letters"] and
                possible_password_chars["numbers"] and
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("strength", True)

    def validate_rules_for_normal_complexity(
            self,
            password_length: int,
            possible_password_chars: Dict[str, bool]
    ) -> None:
        """
        Check password for normal rule. Its valid if:
        - chosen lower and uppercase letters, numbers and length >= 8
        - chosen lower or uppercase letters, special chars and length >= 8
        - chosen lower and upper case, numbers and length >= 8
        - chosen lower case and uppercase letters, special chars and length >= 8

        :param password_length:
        :param possible_password_chars: dict of possible password chars, can contains:
        letters, numbers, special chars
        :return: None
        """

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
                possible_password_chars["lowercase_letters"] and not
                possible_password_chars["uppercase_letters"] and
                possible_password_chars["numbers"] and
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("normal", True)
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and not
                possible_password_chars["lowercase_letters"] and not
                possible_password_chars["uppercase_letters"] and
                possible_password_chars["numbers"] and
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("normal", True)
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and not
                possible_password_chars["lowercase_letters"] and not
                possible_password_chars["uppercase_letters"] and not
                possible_password_chars["numbers"] and
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("normal", True)
        if (
                password_length >= self.STRENGTH_PASSWORD_LENGTH and
                possible_password_chars["lowercase_letters"] and
                possible_password_chars["uppercase_letters"] and not
                possible_password_chars["numbers"] and
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("normal", True)

    def validate_rules_for_weak_complexity(self, password_length, possible_password_chars) -> None:
        """
        Check password for weak rule. Its valid if length < 8 and not chosen special chars.

        :param password_length:
        :param possible_password_chars: dict of possible password chars, can contains:
        letters, numbers, special chars
        :return: None
        """

        if (
                password_length < self.STRENGTH_PASSWORD_LENGTH and not
                possible_password_chars["special_chars"]
        ):
            self.set_password_complexity("weak", True)

    def validate_password(self, password: str) -> None:
        """
        Check password for all three rules.

        :param password: generate password string
        :return: None
        """

        password_complexity = {
            "special_chars": any(char in punctuation for char in password),
            "numbers": any(
                char in ["0", "1", "2", "3", "4", "5", "6", "7", '8', "9"] for char in password
            ),
            "uppercase_letters": any(char in ascii_uppercase for char in password),
            "lowercase_letters": any(char in ascii_lowercase for char in password)
        }
        password_length = len(password)

        self.logger.debug(
            "Start validating password complexity for password consisting: length %s, complexity %s",
            password_length,
            password_complexity
        )
        self.validate_rules_for_strength_complexity(password_length, password_complexity)
        self.validate_rules_for_normal_complexity(password_length, password_complexity)
        self.validate_rules_for_weak_complexity(password_length, password_complexity)
        self.logger.info("Password complexity are: %s", self._password_complexity)

    def __eq__(self, other) -> bool:
        result = self._password_complexity == other._password_complexity

        return result
