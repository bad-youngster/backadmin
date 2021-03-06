# Generated by Django 2.1.5 on 2019-02-13 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_at', models.DateTimeField(auto_created=True, blank=True)),
                ('cabinet_num', models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜号')),
                ('cabinet_order', models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜序号')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('trade_date', models.DateField(blank=True, null=True, verbose_name='购买时间')),
                ('expire_date', models.DateField(blank=True, null=True, verbose_name='过保修期')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='价格')),
                ('latest_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '资产总表',
                'verbose_name_plural': '资产总表',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='业务线')),
                ('memo', models.CharField(blank=True, max_length=64, verbose_name='备注')),
            ],
            options={
                'verbose_name': '业务线',
                'verbose_name_plural': '业务线',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='合同号')),
                ('name', models.CharField(max_length=64, verbose_name='合同名称')),
                ('cost', models.IntegerField(verbose_name='合同金额')),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('license_num', models.IntegerField(blank=True, null=True, verbose_name='license数量')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '合同',
                'verbose_name_plural': '合同',
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=64)),
                ('memo', models.CharField(blank=True, max_length=256, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updata_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '设备类型',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='磁盘名')),
                ('slot', models.CharField(blank=True, max_length=32, null=True, verbose_name='插槽位')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN号')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='磁盘型号')),
                ('capacity', models.FloatField(blank=True, null=True, verbose_name='磁盘容量GB')),
                ('pd_type', models.CharField(blank=True, choices=[('SATA', 'SATA'), ('SAS', 'SAS'), ('SCSI', 'SCSI'), ('SSD', 'SSD')], max_length=64, null=True, verbose_name='磁盘类型')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '硬盘',
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='HandleLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('asset_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Asset')),
            ],
            options={
                'verbose_name_plural': '资产变更日志',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=64, verbose_name='区域')),
                ('name', models.CharField(max_length=32, verbose_name='机房名称')),
                ('floor', models.IntegerField(default=1, verbose_name='楼层')),
                ('display', models.CharField(max_length=128)),
                ('memo', models.CharField(max_length=64, verbose_name='备注')),
            ],
            options={
                'verbose_name': '机房',
                'verbose_name_plural': '机房',
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(blank=True, max_length=32, verbose_name='插槽位')),
                ('manufactory', models.CharField(blank=True, max_length=32, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=64, verbose_name='型号')),
                ('capacity', models.FloatField(blank=True, verbose_name='容量MB')),
                ('sn', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '内存部件',
                'verbose_name_plural': '内存部件',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_asset_type', models.SmallIntegerField(choices=[(0, '路由器'), (1, '交换机'), (2, '无线AP'), (3, 'VPN设备')], default=0, verbose_name='设备类型')),
                ('management_ip', models.CharField(blank=True, max_length=64, null=True, verbose_name='管理IP')),
                ('vlan_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='SN号')),
                ('manufactory', models.CharField(blank=True, max_length=128, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('device_detail', models.TextField(blank=True, null=True, verbose_name='设置详细配置')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Asset')),
            ],
            options={
                'verbose_name': '网络设备',
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NewAssetApprovalZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='资产SN号')),
                ('device_type', models.CharField(blank=True, choices=[('server', '服务器'), ('switch', '交换机'), ('router', '路由器'), ('firewall', '防火墙'), ('wireless', '无线AP')], max_length=64, null=True)),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True)),
                ('model', models.CharField(blank=True, max_length=128, null=True)),
                ('ram_size', models.IntegerField(blank=True, null=True)),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True)),
                ('cpu_count', models.IntegerField(blank=True, null=True)),
                ('cpu_physical_count', models.IntegerField(blank=True, null=True)),
                ('os_platform', models.CharField(blank=True, max_length=64, null=True, verbose_name='系统类型')),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True, verbose_name='OS厂商')),
                ('os_version', models.CharField(blank=True, max_length=64, null=True, verbose_name='系统名称')),
                ('data', models.TextField(verbose_name='资产数据')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='汇报日期')),
                ('approved', models.BooleanField(default=False, verbose_name='已批准')),
                ('approved_date', models.DateTimeField(blank=True, null=True, verbose_name='批准日期')),
            ],
            options={
                'verbose_name': '新上线待批准资产',
                'verbose_name_plural': '新上线待批准资产',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, verbose_name='网卡名称')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='网卡型号')),
                ('hwaddr', models.CharField(max_length=64, verbose_name='网卡mac地址')),
                ('up', models.BooleanField(blank=True, default=False)),
                ('netmask', models.CharField(blank=True, max_length=64)),
                ('ipaddrs', models.CharField(max_length=256, null=True, verbose_name='ip地址')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('speed', models.CharField(blank=True, default='', max_length=64, null=True)),
            ],
            options={
                'verbose_name': '网卡部件',
                'verbose_name_plural': '网卡部件',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=128, null=True)),
                ('salt_name', models.CharField(blank=True, max_length=128, null=True)),
                ('service_sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='快速服务编码')),
                ('sn', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='SN号')),
                ('manufactory', models.CharField(blank=True, max_length=128, null=True, verbose_name='制造商')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号')),
                ('manage_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='管理IP')),
                ('business_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='业务IP')),
                ('os_platform', models.CharField(blank=True, max_length=64, null=True, verbose_name='系统类型')),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True, verbose_name='OS厂商')),
                ('os_version', models.CharField(blank=True, max_length=64, null=True, verbose_name='系统版本')),
                ('cpu_count', models.IntegerField(blank=True, null=True)),
                ('cpu_physical_count', models.IntegerField(blank=True, null=True)),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Asset')),
                ('hosted_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosted_on_server', to='cmdb.Server', verbose_name='宿主机')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
            },
        ),
        migrations.CreateModel(
            name='Server_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('memo', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': '服务器类型',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=64)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '状态',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('primary_mana', models.CharField(max_length=32)),
                ('secondary_mana', models.CharField(max_length=32)),
                ('three_mana', models.CharField(max_length=32)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '用户组',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superuser', models.CharField(max_length=32)),
                ('user', models.CharField(max_length=32)),
                ('approver', models.CharField(max_length=32)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '管理用户',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='sub_asset_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Server_Type'),
        ),
        migrations.AddField(
            model_name='nic',
            name='server_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Server'),
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserProfile', verbose_name='批准人'),
        ),
        migrations.AddField(
            model_name='memory',
            name='server_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Server'),
        ),
        migrations.AddField(
            model_name='handlelog',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserProfile'),
        ),
        migrations.AddField(
            model_name='disk',
            name='server_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.Server'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserProfile'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='user_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserGroup'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.BusinessUnit', verbose_name='属于的业务线'),
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Contract', verbose_name='合同'),
        ),
        migrations.AddField(
            model_name='asset',
            name='device_status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Status'),
        ),
        migrations.AddField(
            model_name='asset',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmdb.DeviceType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cmdb.IDC', verbose_name='IDC机房'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manage_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cmdb.UserProfile', verbose_name='管理员'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='cmdb.Tag'),
        ),
        migrations.AlterIndexTogether(
            name='server',
            index_together={('sn', 'asset')},
        ),
    ]
