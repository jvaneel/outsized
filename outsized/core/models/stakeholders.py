from django.db import models


class Project_Stakeholders(models.Model):
    stakeholder_name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Name'),
        help_text=_('Name of Stakeholder'),
        db_index=True
    )
    stakeholder_email = models.EmailField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_('Email'),
        help_text=_('Email')
    )
    stakeholder_phone_number = models.CharField(max_length=15, blank=True, null=True)
    stakeholder_title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Title'),
        help_text=_('Title of Stakeholder'),
        db_index=True
    )
