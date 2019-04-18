from django.db import models

# Create your models here.


class TUser(models.Model):
    uid = models.BigAutoField(primary_key=True)
    role = models.IntegerField(blank=True, null=True)
    country_id = models.BigIntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    login_pwd = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=128, blank=True, null=True)
    middle_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    birth_date = models.BigIntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=256, blank=True, null=True)
    nationality = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    street = models.CharField(max_length=1024, blank=True, null=True)
    occupation = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=512, blank=True, null=True)
    email_status = models.IntegerField(blank=True, null=True)
    facebook = models.CharField(max_length=1280, blank=True, null=True)
    linkedin = models.CharField(max_length=10000, blank=True, null=True)
    education_level = models.IntegerField(blank=True, null=True)
    referrer = models.BigIntegerField(blank=True, null=True)
    reject_msg = models.CharField(max_length=256, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    auth_source = models.IntegerField(blank=True, null=True)
    create_time = models.BigIntegerField(blank=True, null=True)
    last_login_time = models.BigIntegerField(blank=True, null=True)
    active_time = models.BigIntegerField(blank=True, null=True)
    channel = models.CharField(max_length=1536, blank=True, null=True)
    application_time = models.BigIntegerField(blank=True, null=True)
    lang = models.CharField(max_length=10, blank=True, null=True)
    call_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'
        unique_together = (('country_id', 'phone_number'),)


class RApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.BigIntegerField()
    country_id = models.IntegerField()
    occupation = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    reject_type = models.IntegerField(blank=True, null=True)
    reject_msg = models.CharField(max_length=256, blank=True, null=True)
    application_time = models.BigIntegerField(blank=True, null=True)
    created_at = models.BigIntegerField(blank=True, null=True)
    is_wl_processed = models.IntegerField(blank=True, null=True)
    is_model_processed = models.IntegerField()
    is_notified = models.IntegerField()
    limit_amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    completed_time = models.BigIntegerField(blank=True, null=True)
    auth_source = models.IntegerField(blank=True, null=True)
    risk_mode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_application'
