from django.db import models

class Master_Clients(models.Model):

    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Name'),
        help_text=_('Name of CLient'),
        db_index=True
    )

    stage = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Stage'),
        help_text=_('Name of Stage'),
        db_index=True
    )
    detail =  models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_('Detail'),
        help_text=_('Client Details.')
    )
    pocs = models.ForeignKey(
        Client_Pocs,
        on_delete=models.CASCADE,
        null=True,
        related_name='client_pocs',
        verbose_name=_('client_pocs'),
        help_text=_('client_pocs')
    )

    links =models.ForeignKey(
        Client_Document_Links,
        on_delete=models.CASCADE,
        null=True,
        related_name='client_pocs',
        verbose_name=_('client_pocs'),
        help_text=_('client_pocs')
    )

    files = models.ForeignKey(
        Client_Document_Files,
        on_delete=models.CASCADE,
        null=True,
        related_name='client_pocs',
        verbose_name=_('client_pocs'),
        help_text=_('client_pocs')
    )

    industries = models.ForeignKey(
        Client_Industry_Map,
        on_delete=models.CASCADE,
        null=True,
        related_name='client_pocs',
        verbose_name=_('client_pocs'),
        help_text=_('client_pocs')
    )

    client_type = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Client Type'),
        help_text=_('Client Type'),
        db_index=True
    )
    client_industry = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Client Industry'),
        help_text=_('Client Industry'),
        db_index=True
    )
    client_location = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Client Location'),
        help_text=_('Client Location'),
        db_index=True
    )

class Client_Industries(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Client Industry Name'),
        help_text=_('Client Industry Name'),
        db_index=True
    )



class Client_Industry_Map(Base, BelongsToClient):
    industry_model= models.ForeignKey(
        ClientIndustryMap,
        on_delete=models.CASCADE,
        null=True,
        related_name='industry_model',
        verbose_name=_('industry_model'),
        help_text=_('industry_model')
    )


class Client_Alternate_Mobiles(models.Model):
    phone = models.CharField(max_length=15, blank=True, null=True)


class Client_Cities(models.Model):
    city = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Client cities'),
        help_text=_('Client cities'),
        db_index=True
    )


class Client_Pocs(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_('Client Pocs Name'),
        help_text=_('Client Pocs Name'),
        db_index=True
    )
    email = models.EmailField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_('Email'),
        help_text=_('Email')
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    calling_code = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        db_index=True,
        verbose_name=_('Calling Code'),
        help_text=_('Calling Code.')
    )
    designation = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Designation'),
        help_text=_('Designation'),
        db_index=True
    )

class Client_Document_Links(models.Model):
    name =  models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Client Docs name'),
        help_text=_('Client Docs name'),
        db_index=True
    )
    link =  models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Client Docs Links'),
        help_text=_('Client Docs Links'),
        db_index=True
    )


class Client_Document_Files(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Client Docs File Name'),
        help_text=_('Client Docs File Name'),
        db_index=True
    )
    link = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Client Docs File Links'),
        help_text=_('Client Docs File Links'),
        db_index=True
    )