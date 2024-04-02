# Generated by Django 3.2.5 on 2024-03-31 13:53

import api.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('raw', models.BigIntegerField(blank=True, default=0, null=True, verbose_name='原料')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='编码')),
                ('type_code', models.IntegerField(blank=True, default=0, null=True, verbose_name='类型编码')),
                ('img', models.TextField(blank=True, null=True)),
                ('raw_detail', models.FloatField(blank=True, default=0, null=True, verbose_name='原料用量')),
                ('cookbook_make', models.FloatField(blank=True, null=True, verbose_name='制作方法')),
                ('crawler_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '食谱列表',
                'verbose_name_plural': '食谱列表',
                'db_table': 'foods',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recommendforallusers',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('recommendations', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '用户推荐',
                'verbose_name_plural': '用户推荐',
                'db_table': 'recommendforallusers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='姓名')),
                ('birth', models.DateField(null=True, verbose_name='生日')),
                ('genderCode', models.IntegerField(default='1', null=True, verbose_name='性别id 男 1 女 0')),
                ('genderTranslation', models.CharField(default='男', max_length=2, null=True, verbose_name='性别')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('photo', models.ImageField(blank=True, default='default/user.jpg', null=True, upload_to=api.models.user_directory_path, verbose_name='头像')),
                ('resume_id', models.IntegerField(blank=True, null=True)),
                ('init', models.BooleanField(blank=True, default=False, null=True, verbose_name='初始化')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserResume',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type1', models.IntegerField(blank=True, default=0, null=True, verbose_name='期望菜品类型id')),
                ('type1Translation', models.CharField(blank=True, max_length=20, null=True, verbose_name='期望菜品类型')),
                ('type2', models.IntegerField(blank=True, default=0, null=True, verbose_name='期望菜品类型2id')),
                ('type2Translation', models.CharField(blank=True, max_length=20, null=True, verbose_name='期望菜品类型2')),
                ('type3', models.IntegerField(blank=True, default=0, null=True, verbose_name='期望菜品类型3id')),
                ('type3Translation', models.CharField(blank=True, max_length=20, null=True, verbose_name='期望菜品类型3')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户画像信息',
                'verbose_name_plural': '用户画像信息',
                'db_table': 'resume',
            },
        ),
        migrations.CreateModel(
            name='Starfoods',
            fields=[
                ('sid', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.foods', verbose_name='景点')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
                'db_table': 'star',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('lid', models.BigAutoField(primary_key=True, serialize=False)),
                ('active', models.TextField(verbose_name='行为')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '操作日志',
                'verbose_name_plural': '操作日志',
                'db_table': 'logs',
            },
        ),
        migrations.CreateModel(
            name='Likefoods',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.foods', verbose_name='景点')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '喜欢',
                'verbose_name_plural': '喜欢',
                'db_table': 'like',
            },
        ),
        migrations.CreateModel(
            name='Commentfoods',
            fields=[
                ('cid', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('foods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.foods', verbose_name='景点')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'db_table': 'comment',
            },
        ),
    ]
