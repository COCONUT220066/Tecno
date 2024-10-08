from django.db import models


class Administrador(models.Model):
    idadmi = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    contacto = models.IntegerField()
    correo_electronico = models.CharField(unique=True, max_length=300)
    contraseña = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'administrador'


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
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
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


class Citas(models.Model):
    num_cita = models.IntegerField(primary_key=True)
    fecha_cita = models.DateTimeField(unique=True)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuario')
    idespecialistas = models.ForeignKey('Especialistas', models.DO_NOTHING, db_column='idespecialistas')

    class Meta:
        managed = False
        db_table = 'citas'


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


class Especialistas(models.Model):
    idespecialistas = models.IntegerField(primary_key=True)
    nombre_es = models.CharField(max_length=50)
    contacto_es = models.IntegerField()
    contraseña_e = models.CharField(max_length=30)
    correo_e = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'especialistas'


class MiaplicacionCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    is_especialista = models.IntegerField()
    is_usuario = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'miaplicacion_customuser'


class MiaplicacionCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(MiaplicacionCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'miaplicacion_customuser_groups'
        unique_together = (('customuser', 'group'),)


class MiaplicacionCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(MiaplicacionCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'miaplicacion_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contacto = models.IntegerField()
    idespecialistas = models.ForeignKey(Especialistas, models.DO_NOTHING, db_column='idespecialistas')
    ficha = models.IntegerField()
    contraseña = models.CharField(max_length=30)
    correo_u = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'usuario'