# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dongjun(models.Model):
    name = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20, blank=True, null=True)
    height = models.SmallIntegerField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dongjun'


class FrequentzonechildAccident(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    occur = models.IntegerField(blank=True, null=True)
    death_injury = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    s_injury = models.IntegerField(blank=True, null=True)
    l_injury = models.IntegerField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequentzonechild_accident'


class FrequentzonechildKeywordsearch(models.Model):
    year = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    center = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequentzonechild_keywordsearch'


class FrequentzonelgAccident(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    occur = models.IntegerField(blank=True, null=True)
    death_injury = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    s_injury = models.IntegerField(blank=True, null=True)
    l_injury = models.IntegerField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequentzonelg_accident'


class FrequentzoneoldmanAccident(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    occur = models.IntegerField(blank=True, null=True)
    death_injury = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    s_injury = models.IntegerField(blank=True, null=True)
    l_injury = models.IntegerField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequentzoneoldman_accident'


class FrequentzonetmzonAccident(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    occur = models.IntegerField(blank=True, null=True)
    death_injury = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    s_injury = models.IntegerField(blank=True, null=True)
    l_injury = models.IntegerField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequentzonetmzon_accident'


class FrequentzonetmzonKeywordsearch(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    center = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'frequentzonetmzon_keywordsearch'


class InfCarAcc(models.Model):
    id = models.IntegerField(primary_key=True)
    cg = models.TextField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sum = models.IntegerField(blank=True, null=True)
    ctop = models.IntegerField(db_column='CtoP', blank=True, null=True)  # Field name made lowercase.
    ctoc = models.IntegerField(db_column='CtoC', blank=True, null=True)  # Field name made lowercase.
    calone = models.IntegerField(db_column='CAlone', blank=True, null=True)  # Field name made lowercase.
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_car_acc'


class InfChildZone(models.Model):
    id = models.IntegerField(primary_key=True)
    gugun = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    sname = models.TextField(blank=True, null=True)
    stype = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_child_zone'


class InfEleDisplay(models.Model):
    id = models.IntegerField(primary_key=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_ele_display'


class InfPopulation(models.Model):
    id = models.IntegerField(primary_key=True)
    year_code = models.IntegerField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    household = models.IntegerField(blank=True, null=True)
    pop_sum = models.IntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    female = models.IntegerField(blank=True, null=True)
    sumkor = models.IntegerField(db_column='sumKor', blank=True, null=True)  # Field name made lowercase.
    korm = models.IntegerField(db_column='korM', blank=True, null=True)  # Field name made lowercase.
    korf = models.IntegerField(db_column='korF', blank=True, null=True)  # Field name made lowercase.
    sumfor = models.IntegerField(db_column='sumFor', blank=True, null=True)  # Field name made lowercase.
    form = models.IntegerField(db_column='forM', blank=True, null=True)  # Field name made lowercase.
    forf = models.IntegerField(db_column='forF', blank=True, null=True)  # Field name made lowercase.
    houseperperson = models.FloatField(db_column='HousePerPerson', blank=True, null=True)  # Field name made lowercase.
    over65 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_population'


class InfSmartCross(models.Model):
    id = models.IntegerField(primary_key=True)
    year_code = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_smart_cross'


class InfSmartLamp(models.Model):
    id = models.IntegerField(primary_key=True)
    gugun = models.TextField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_smart_lamp'


class InfSpeedBump(models.Model):
    id = models.IntegerField(primary_key=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    year_code = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_speed_bump'


class InfUnCamera(models.Model):
    id = models.IntegerField(primary_key=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    gubun = models.IntegerField(blank=True, null=True)
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    year_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_un_camera'


class InfYellowcarpet(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    year_code = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inf_yellowcarpet'


class JaywalkingAccident(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    occur = models.IntegerField(blank=True, null=True)
    death_injury = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    s_injury = models.IntegerField(blank=True, null=True)
    l_injury = models.IntegerField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jaywalking_accident'


class JaywalkingKeywordsearch(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    center = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jaywalking_keywordsearch'


class SchoolzonechildAccident(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    occur = models.IntegerField(blank=True, null=True)
    death_injury = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    s_injury = models.IntegerField(blank=True, null=True)
    l_injury = models.IntegerField(blank=True, null=True)
    lot = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schoolzonechild_accident'


class SchoolzonechildKeywordsearch(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    sido = models.TextField(blank=True, null=True)
    gugun = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    center = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schoolzonechild_keywordsearch'


class Year(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'year'
