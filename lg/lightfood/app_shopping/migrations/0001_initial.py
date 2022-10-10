# Generated by Django 3.2 on 2022-10-10 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_time', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('order_money', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('order_quantity', models.IntegerField()),
                ('order_paytype', models.CharField(choices=[(1, '微信'), (2, '支付宝'), (3, '银行卡')], max_length=32)),
                ('order_state', models.BooleanField(default=0)),
                ('order_freight', models.IntegerField(default=0)),
                ('order_evaluate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_order.orderevaluate')),
            ],
        ),
    ]
