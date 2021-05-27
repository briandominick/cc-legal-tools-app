# Generated by Django 2.2.20 on 2021-05-27 17:12

# Third-party
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LegalCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        help_text="E.g. 'en', 'en-ca', 'sr-Latn', or 'x-i18n'."
                        " Case-sensitive? This is the language code used by"
                        " CC, which might be a little different from the"
                        " Django language code.",
                        max_length=8,
                    ),
                ),
                (
                    "html_file",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="HTML file we got this from",
                        max_length=300,
                    ),
                ),
                (
                    "translation_last_update",
                    models.DateTimeField(
                        default=None,
                        help_text="The last_updated field from Transifex for"
                        " this translation",
                        null=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="License title in this language, e.g."
                        " 'Attribution-NonCommercial-NoDerivs 3.0 Unported'",
                        max_length=112,
                    ),
                ),
                ("html", models.TextField(blank=True, default="")),
                ("license_url", models.URLField(default=None, null=True)),
                ("deed_url", models.URLField(unique=True)),
                ("plain_text_url", models.URLField(default=None, null=True)),
            ],
            options={
                "ordering": ["license", "language_code"],
            },
        ),
        migrations.CreateModel(
            name="TranslationBranch",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("branch_name", models.CharField(max_length=40)),
                (
                    "version",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="E.g. '4.0'. Not required.",
                        max_length=3,
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        help_text="E.g. 'en', 'en-ca', 'sr-Latn', or 'x-i18n'."
                        " Case-sensitive? This is a CC language code, which"
                        " might differ from Django.",
                        max_length=8,
                    ),
                ),
                (
                    "last_transifex_update",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Time when last updated on Transifex.",
                    ),
                ),
                ("complete", models.BooleanField(default=False)),
                (
                    "legalcodes",
                    models.ManyToManyField(to="licenses.LegalCode"),
                ),
            ],
            options={
                "verbose_name_plural": "translation branches",
            },
        ),
        migrations.CreateModel(
            name="License",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "canonical_url",
                    models.URLField(
                        help_text="The license's unique identifier, e.g."
                        " 'https://creativecommons.org/licenses/by-nd/2.0/"
                        "br/'",
                        unique=True,
                        verbose_name="Canonical URL",
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        help_text="shorthand representation for which class of"
                        " licenses this falls into. E.g. 'by-nc-sa', or 'MIT',"
                        " 'nc-sampling+', 'devnations', ...",
                        max_length=40,
                    ),
                ),
                (
                    "version",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="E.g. '4.0'. Not required.",
                        max_length=3,
                    ),
                ),
                (
                    "jurisdiction_code",
                    models.CharField(blank=True, default="", max_length=9),
                ),
                (
                    "creator_url",
                    models.URLField(
                        blank=True,
                        default="",
                        help_text="E.g. https://creativecommons.org",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="'licenses' or 'publicdomain'",
                        max_length=13,
                    ),
                ),
                (
                    "title_english",
                    models.TextField(
                        blank=True,
                        default="",
                        help_text="License title in English, e.g."
                        " 'Attribution-NonCommercial-NoDerivs 3.0 Unported'",
                    ),
                ),
                (
                    "deprecated_on",
                    models.DateField(
                        help_text="if set, the date on which this license was"
                        " deprecated",
                        null=True,
                    ),
                ),
                ("permits_derivative_works", models.BooleanField()),
                ("permits_reproduction", models.BooleanField()),
                ("permits_distribution", models.BooleanField()),
                ("permits_sharing", models.BooleanField()),
                ("requires_share_alike", models.BooleanField()),
                ("requires_notice", models.BooleanField()),
                ("requires_attribution", models.BooleanField()),
                ("requires_source_code", models.BooleanField()),
                ("prohibits_commercial_use", models.BooleanField()),
                ("prohibits_high_income_nation_use", models.BooleanField()),
                (
                    "is_based_on",
                    models.ForeignKey(
                        blank=True,
                        help_text="another license that this one is based on",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="base_of",
                        to="licenses.License",
                    ),
                ),
                (
                    "is_replaced_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="another license that has replaced this one",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replaces",
                        to="licenses.License",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        blank=True,
                        help_text="another license that this is the"
                        " translation of",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source_of",
                        to="licenses.License",
                    ),
                ),
            ],
            options={
                "ordering": ["-version", "unit", "jurisdiction_code"],
            },
        ),
        migrations.AddField(
            model_name="legalcode",
            name="license",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="legal_codes",
                to="licenses.License",
            ),
        ),
    ]
