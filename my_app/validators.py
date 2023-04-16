from django.core.validators import RegexValidator


class NamePartsValidator:
    # Сообщения об ошибках
    _CYRILLIC_CHARS_ERROR_MESSAGE = 'Доступны только кириллические символы'
    _LATIN_CHARS_ERROR_MESSAGE = 'Доступны только латинские символы'

    # Регулярки
    _CYRILLIC_REGEX = r'^[А-Яа-яЁё]+$'
    _LATIN_REGEX = r'^[a-zA-Z]+$'

    # Валидаторы
    validate_cyrillic = RegexValidator(regex=_CYRILLIC_REGEX, message=_CYRILLIC_CHARS_ERROR_MESSAGE)
    validate_latin = RegexValidator(regex=_LATIN_REGEX, message=_LATIN_CHARS_ERROR_MESSAGE)

    # verbose_name
    NOMINATIVE_VERBOSE_NAME = 'Именительный'
    GENITIVE_VERBOSE_NAME = 'Родительный'
    DATIVE_VERBOSE_NAME = 'Дательный'
    ACCUSATIVE_VERBOSE_NAME = 'Винительный'
    INSTRUMENTAL_VERBOSE_NAME = 'Творительный'
    PREPOSITIONAL_VERBOSE_NAME = 'Предложный'
    LATIN_VERBOSE_NAME = 'Латиница'

    # help_text
    NOMINATIVE_HELP_TEXT = 'Например, "Дмитрий"'
    GENITIVE_HELP_TEXT = 'Например, "Дмитрия"'
    DATIVE_HELP_TEXT = 'Например, "Дмитрию"'
    ACCUSATIVE_HELP_TEXT = 'Например, "Дмитрия"'
    INSTRUMENTAL_HELP_TEXT = 'Например, "Дмитрием"'
    PREPOSITIONAL_HELP_TEXT = 'Например, "Дмитрии"'
    LATIN_HELP_TEXT = 'Например, "Dmitry"'


class RoleValidator:
    # verbose_name
    ROLE_VERBOSE_NAME = 'Роль'


class PassportValidator:
    # Сообщения об ошибках
    _PASSPORT_SERIES_ERROR_MESSAGE = 'Серия паспорта должна состоять из 4 цифр'
    _PASSPORT_NUMBER_ERROR_MESSAGE = 'Номер паспорта должен состоять из 6 цифр'
    _PASSPORT_ISSUED_BY_ERROR_MESSAGE = 'Некорректное значение'
    _PASSPORT_DEPARTMENT_CODE_ERROR_MESSAGE = 'Код подразделения должен иметь формат XXX-XXX'

    # Регулярки
    _PASSPORT_SERIES_REGEX = r'^\d{4}$'
    _PASSPORT_NUMBER_REGEX = r'^\d{6}$'
    _PASSPORT_ISSUED_BY_REGEX = r'^[А-Яа-я\s\d.,/-]+$'
    _PASSPORT_DEPARTMENT_CODE_REGEX = r'^\d{3}-\d{3}$'

    # Валидаторы
    validate_passport_series = RegexValidator(regex=_PASSPORT_SERIES_REGEX, message=_PASSPORT_SERIES_ERROR_MESSAGE)
    validate_passport_number = RegexValidator(regex=_PASSPORT_NUMBER_REGEX, message=_PASSPORT_NUMBER_ERROR_MESSAGE)
    validate_passport_issued_by = RegexValidator(regex=_PASSPORT_ISSUED_BY_REGEX, message=_PASSPORT_ISSUED_BY_ERROR_MESSAGE)
    validate_passport_department_code = RegexValidator(regex=_PASSPORT_DEPARTMENT_CODE_REGEX, message=_PASSPORT_DEPARTMENT_CODE_ERROR_MESSAGE)

    # verbose_name
    SERIES_VERBOSE_NAME = 'Серия'
    NUMBER_VERBOSE_NAME = 'Номер'
    ISSUED_DATE_VERBOSE_NAME = 'Дата выдачи'
    ISSUED_BY_VERBOSE_NAME = 'Кем выдан'
    DEPARTMENT_CODE_VERBOSE_NAME = 'Код подразделения'

    # help_text
    SERIES_HELP_TEXT = 'Например, "1234"'
    NUMBER_HELP_TEXT = 'Например, "123456"'
    ISSUED_BY_HELP_TEXT = 'Например, "ГУ МВД РОССИИ ПО СВЕРДЛОВСКОЙ ОБЛАСТИ"'
    DEPARTMENT_CODE_HELP_TEXT = 'Например, "123-456"'


class SnilsValidator:
    # Сообщения об ошибках
    _SNILS_NUMBER_ERROR_MESSAGE = 'Номер СНИЛС должен иметь формат XXX-XXX-XXX XX'

    # Регулярки
    _SNILS_NUMBER_REGEX = r'^\d{3}-\d{3}-\d{3} \d{2}$'

    # Валидаторы
    validate_snils_number = RegexValidator(regex=_SNILS_NUMBER_REGEX, message=_SNILS_NUMBER_ERROR_MESSAGE)

    # verbose_name
    SNILS_NUMBER_VERBOSE_NAME = 'Номер СНИЛС'

    # help_text
    SNILS_NUMBER_HELP_TEXT = 'Например, "123-456-789 00"'


class MemberValidator:
    # Сообщения об ошибках
    _PHONE_NUMBER_ERROR_MESSAGE = 'Номер телефона должен быть в формате "+7XXXXXXXXXX"'

    # Регулярки
    _PHONE_NUMBER_REGEX = r'^\+7\d{10}$'

    # Валидаторы
    validate_phone_number = RegexValidator(regex=_PHONE_NUMBER_REGEX, message=_PHONE_NUMBER_ERROR_MESSAGE)

    # verbose_name
    NAME_VERBOSE_NAME = 'Имя'
    SURNAME_VERBOSE_NAME = 'Фамилия'
    PATRONYMIC_VERBOSE_NAME = 'Отчество'
    ROLE_VERBOSE_NAME = 'Роль'
    PASSPORT_VERBOSE_NAME = 'Паспорт'
    SNILS_VERBOSE_NAME = 'Снилс'
    EMAIL_VERBOSE_NAME = 'Email'
    PHONE_NUMBER_VERBOSE_NAME = 'Номер телефона'
    BIRTHDAY_VERBOSE_NAME = 'Дата рождения'
    IS_ACTUAL_VERBOSE_NAME = 'Актуальность'

    # help_text
    EMAIL_HELP_TEXT = 'Например, "worktrackerapp@gmail.com"'
    PHONE_NUMBER_HELP_TEXT = 'Например, "+79122414074"'


class ProjectValidator:
    # verbose_name
    NAME_VERBOSE_NAME = 'Объект работы'


class DataValidator:
    OBJECT_VERBOSE_NAME = 'Объект работы'
    MEMBER_VERBOSE_NAME = 'Работник'
    START_TIME_VERBOSE_NAME = 'Начало работы'
    END_TIME_VERBOSE_NAME = 'Конец работы'
    LUNCH_BREAK_VERBOSE_NAME = 'Продолжительность обеда'