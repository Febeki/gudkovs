from django.db import models
from .validators import (
    NamePartsValidator,
    RoleValidator,
    PassportValidator,
    SnilsValidator,
    MemberValidator,
    ProjectValidator,
    DataValidator
)


# Базовая длина для полей типа 'name', 'surname' и тд.
BASE_LENGTH = 16


class CyrillicCharField(models.CharField):
    default_validators = [NamePartsValidator.validate_cyrillic]


class NameParts(models.Model):
    nominative = CyrillicCharField(
        max_length=BASE_LENGTH,
        help_text=NamePartsValidator.NOMINATIVE_HELP_TEXT,
        verbose_name=NamePartsValidator.NOMINATIVE_VERBOSE_NAME
    )

    genitive = CyrillicCharField(
        max_length=BASE_LENGTH,
        blank=True,
        null=True,
        help_text=NamePartsValidator.GENITIVE_HELP_TEXT,
        verbose_name=NamePartsValidator.GENITIVE_VERBOSE_NAME
    )

    dative = CyrillicCharField(
        max_length=BASE_LENGTH,
        blank=True,
        null=True,
        help_text=NamePartsValidator.DATIVE_HELP_TEXT,
        verbose_name=NamePartsValidator.DATIVE_VERBOSE_NAME
    )

    accusative = CyrillicCharField(
        max_length=BASE_LENGTH,
        blank=True,
        null=True,
        help_text=NamePartsValidator.ACCUSATIVE_HELP_TEXT,
        verbose_name=NamePartsValidator.ACCUSATIVE_VERBOSE_NAME
    )

    instrumental = CyrillicCharField(
        max_length=BASE_LENGTH,
        blank=True,
        null=True,
        help_text=NamePartsValidator.INSTRUMENTAL_HELP_TEXT,
        verbose_name=NamePartsValidator.INSTRUMENTAL_VERBOSE_NAME
    )

    prepositional = CyrillicCharField(
        max_length=BASE_LENGTH,
        blank=True,
        null=True,
        help_text=NamePartsValidator.PREPOSITIONAL_HELP_TEXT,
        verbose_name=NamePartsValidator.PREPOSITIONAL_VERBOSE_NAME
    )

    latin = models.CharField(
        max_length=BASE_LENGTH,
        blank=True,
        null=True,
        validators=[NamePartsValidator.validate_latin],
        help_text=NamePartsValidator.LATIN_HELP_TEXT,
        verbose_name=NamePartsValidator.LATIN_VERBOSE_NAME
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.nominative


class FirstName(NameParts):
    pass


class LastName(NameParts):
    pass


class Patronymic(NameParts):
    pass


class Role(models.Model):
    role = CyrillicCharField(
        max_length=BASE_LENGTH,
        verbose_name=RoleValidator.ROLE_VERBOSE_NAME
    )

    def __str__(self):
        return self.role


class Passport(models.Model):
    series = models.CharField(
        max_length=4,
        validators=[PassportValidator.validate_passport_series],
        help_text=PassportValidator.SERIES_HELP_TEXT,
        verbose_name=PassportValidator.SERIES_VERBOSE_NAME
    )
    number = models.CharField(
        max_length=6,
        validators=[PassportValidator.validate_passport_number],
        help_text=PassportValidator.NUMBER_HELP_TEXT,
        verbose_name=PassportValidator.NUMBER_VERBOSE_NAME
    )
    issued_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=PassportValidator.ISSUED_DATE_VERBOSE_NAME
    )
    issued_by = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        validators=[PassportValidator.validate_passport_issued_by],
        help_text=PassportValidator.ISSUED_BY_HELP_TEXT,
        verbose_name=PassportValidator.ISSUED_BY_VERBOSE_NAME
    )
    department_code = models.CharField(
        max_length=7,
        blank=True,
        null=True,
        validators=[PassportValidator.validate_passport_department_code],
        help_text=PassportValidator.DEPARTMENT_CODE_HELP_TEXT,
        verbose_name=PassportValidator.DEPARTMENT_CODE_VERBOSE_NAME
    )

    def __str__(self):
        return f'{self.series} {self.number}'


class Snils(models.Model):
    number = models.CharField(
        max_length=14,
        validators=[SnilsValidator.validate_snils_number],
        help_text=SnilsValidator.SNILS_NUMBER_HELP_TEXT,
        verbose_name=SnilsValidator.SNILS_NUMBER_VERBOSE_NAME
    )

    def __str__(self):
        return self.number


class Member(models.Model):
    name = models.ForeignKey(
        FirstName,
        on_delete=models.PROTECT,
        verbose_name=MemberValidator.NAME_VERBOSE_NAME
    )
    surname = models.ForeignKey(
        LastName,
        on_delete=models.PROTECT,
        verbose_name=MemberValidator.SURNAME_VERBOSE_NAME
    )
    patronymic = models.ForeignKey(
        Patronymic,
        on_delete=models.PROTECT,
        verbose_name=MemberValidator.PATRONYMIC_VERBOSE_NAME
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        verbose_name=MemberValidator.ROLE_VERBOSE_NAME
    )
    passport = models.OneToOneField(
        Passport,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=MemberValidator.PASSPORT_VERBOSE_NAME
    )
    snils = models.OneToOneField(
        Snils,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name=MemberValidator.SNILS_VERBOSE_NAME
    )
    email = models.EmailField(
        max_length=32,
        blank=True,
        null=True,
        help_text=MemberValidator.EMAIL_HELP_TEXT,
        verbose_name=MemberValidator.EMAIL_VERBOSE_NAME
    )
    phone_number = models.CharField(
        max_length=12,
        blank=True,
        null=True,
        validators=[MemberValidator.validate_phone_number],
        help_text=MemberValidator.PHONE_NUMBER_HELP_TEXT,
        verbose_name=MemberValidator.PHONE_NUMBER_VERBOSE_NAME
    )
    birthday = models.DateField(
        blank=True,
        null=True,
        verbose_name=MemberValidator.BIRTHDAY_VERBOSE_NAME
    )
    is_actual = models.BooleanField(
        default=True,
        verbose_name=MemberValidator.IS_ACTUAL_VERBOSE_NAME
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class Project(models.Model):
    name = models.CharField(max_length=32, verbose_name=ProjectValidator.NAME_VERBOSE_NAME)

    def __str__(self):
        return self.name


class Data(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.PROTECT,
        verbose_name=DataValidator.MEMBER_VERBOSE_NAME
    )
    start_time = models.TimeField(verbose_name=DataValidator.START_TIME_VERBOSE_NAME)
    end_time = models.TimeField(verbose_name=DataValidator.END_TIME_VERBOSE_NAME)
    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        verbose_name=DataValidator.OBJECT_VERBOSE_NAME
    )
    lunch_break = models.DurationField(verbose_name=DataValidator.LUNCH_BREAK_VERBOSE_NAME)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.member} {self.date}'
