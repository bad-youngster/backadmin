# -*- coding: utf-8 -*-

from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    memo = models.TextField(u'备注', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "状态"


class DeviceType(models.Model):
    '''设备类型'''
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)
    memo = models.CharField(max_length=256, null=True, blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    updata_at = models.DateTimeField(blank=True, auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "设备类型"

class UserProfile(models.Model):
    '''后台管理用户'''
    superuser = models.CharField(max_length=32)
    user = models.CharField(max_length=32)
    approver = models.CharField(max_length=32)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)

    def __unicode__(self):
        return self.create_at
    class Meta:
        verbose_name_plural = "管理用户"


class Asset(models.Model):
    '''资产总表'''
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE)
    device_status = models.ForeignKey('Status', default=1, null=True, blank=True, on_delete=models.CASCADE)
    cabinet_num = models.CharField(u'机柜号', max_length=30, null=True, blank=True)
    cabinet_order = models.CharField(u'机柜序号', max_length=30, null=True, blank=True)
    memo = models.TextField(u'备注', null=True, blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_created=True)
    idc = models.ForeignKey('IDC', verbose_name=u'IDC机房', null=True, blank=True, on_delete=models.CASCADE)
    contract = models.ForeignKey('Contract', verbose_name=u'合同', null=True, blank=True)
    trade_date = models.DateField(u'购买时间', null=True, blank=True)
    expire_date = models.DateField(u'过保修期', null=True, blank=True)
    price = models.FloatField(u'价格', null=True, blank=True)
    business_unit = models.ForeignKey('BusinessUnit', verbose_name=u'属于的业务线', null=True, blank=True)
    manage_user = models.ForeignKey('UserProfile', verbose_name=u'管理员', related_name='+', null=True, blank=True)
    tag = models.ManyToManyField('Tag', null=True, blank=True)
    latest_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"

    def __unicode__(self):
        return self.server.sn


class Server_Type(models.Model):
    '''服务器类型'''
    name = models.CharField(max_length=128)
    memo = models.CharField(max_length=256, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "服务器类型"


class Server(models.Model):
    '''服务器信息'''
    asset = models.OneToOneField('Asset')
    sub_asset_type = models.ForeignKey('Server_Type')
    hostname = models.CharField(max_length=128, blank=True, null=True)
    salt_name = models.CharField(max_length=128, blank=True, null=True)
    hosted_on = models.ForeignKey('self', related_name='hosted_on_server', blank=True, null=True,
                                  verbose_name=u'宿主机')  # 虚拟机关联宿主机
    service_sn = models.CharField(u'快速服务编码', max_length=128, blank=True, null=True)
    sn = models.CharField(u'SN号', max_length=64, blank=True, null=True, unique=True)
    manufactory = models.CharField(verbose_name=u'制造商', max_length=128, null=True, blank=True)
    model = models.CharField(u'型号', max_length=128, null=True, blank=True)
    manage_ip = models.GenericIPAddressField(u'管理IP', null=True, blank=True)
    business_ip = models.GenericIPAddressField(u'业务IP', null=True, blank=True)
    os_platform = models.CharField(u'系统类型', max_length=64, null=True, blank=True)
    os_distribution = models.CharField(u'OS厂商', max_length=64, blank=True, null=True)
    os_version = models.CharField(u'系统版本', max_length=64, null=True, blank=True)
    cpu_count = models.IntegerField(null=True, blank=True)
    cpu_physical_count = models.IntegerField(null=True, blank=True)
    cpu_model = models.CharField(max_length=128, null=True, blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = "服务器"
        index_together = ["sn", "asset"]

    def __unicode__(self):
        return '<id:%s>' % (self.id)


class NetworkDevice(models.Model):
    '''网络设备'''
    asset = models.OneToOneField('Asset')
    sub_assset_type_choices = ((0, '路由器'), (1, '交换机'), (2, '无线AP'), (3, 'VPN设备'),)
    sub_asset_type = models.SmallIntegerField(choices=sub_assset_type_choices, verbose_name="设备类型", default=0)
    management_ip = models.CharField(u'管理IP', max_length=64, blank=True, null=True)
    vlan_ip = models.GenericIPAddressField(u'VlanIP', blank=True, null=True)
    intranet_ip = models.GenericIPAddressField(u'内网IP', blank=True, null=True)
    sn = models.CharField(u'SN号', max_length=128, unique=True)
    manufactory = models.CharField(verbose_name=u'制造商', max_length=128, null=True, blank=True)
    model = models.CharField(u'型号', max_length=128, null=True, blank=True)
    port_num = models.SmallIntegerField(u'端口个数', null=True, blank=True)
    device_detail = models.TextField(u'设置详细配置', null=True, blank=True)

    class Meta:
        verbose_name = '网络设备'
        verbose_name_plural = "网络设备"


class Memory(models.Model):
    slot = models.CharField(u'插槽位', max_length=32, blank=True)
    manufactory = models.CharField(u'制造商', max_length=32, null=True, blank=True)
    model = models.CharField(u'型号', max_length=64, blank=True)
    capacity = models.FloatField(u'容量MB', blank=True)
    sn = models.CharField(max_length=256, null=True, blank=True, default='')
    memo = models.TextField(u'备注', null=True, blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    server_info = models.ForeignKey('Server',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '内存部件'
        verbose_name_plural = "内存部件"

    def __unicode__(self):
        return '%s: %sGB ' % (self.slot, self.capacity)


class NIC(models.Model):
    name = models.CharField(u'网卡名称', max_length=128, blank=True)
    model = models.CharField(u'网卡型号', max_length=128, blank=True, null=True)
    hwaddr = models.CharField(u'网卡mac地址', max_length=64)
    up = models.BooleanField(default=False, blank=True)
    netmask = models.CharField(max_length=64, blank=True)
    ipaddrs = models.CharField(u'ip地址', max_length=256, null=True)
    memo = models.TextField(u'备注', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    server_info = models.ForeignKey('server')
    speed = models.CharField(max_length=64, null=True, blank=True, default='')

    class Meta:
        verbose_name = '网卡部件'
        verbose_name_plural = "网卡部件"

    def __unicode__(self):
        return u'网卡%s --> MAC:%s;IP%s;up:%s;netmask:%s' % (self.name, self.hwaddr, self.ipaddrs, self.up, self.netmask)


class Disk(models.Model):
    name = models.CharField(u'磁盘名', max_length=32, blank=True, null=True)
    slot = models.CharField(u'插槽位', max_length=32, blank=True, null=True)
    sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
    model = models.CharField(u'磁盘型号', max_length=128, blank=True, null=True)
    capacity = models.FloatField(u'磁盘容量GB', blank=True, null=True)
    disk_iface_choice = (('SATA', 'SATA'), ('SAS', 'SAS'), ('SCSI', 'SCSI'), ('SSD', 'SSD'),)
    pd_type = models.CharField(u'磁盘类型', choices=disk_iface_choice, max_length=64, blank=True, null=True)
    memo = models.TextField(u'备注', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    server_info = models.ForeignKey('server')

    def __unicode__(self):
        return 'slot:%s size:%s' % (self.slot, self.capacity)

    class Meta:
        verbose_name_plural = "硬盘"


class IDC(models.Model):
    region = models.CharField(u'区域', max_length=64)
    name = models.CharField(u'机房名称', max_length=32)
    floor = models.IntegerField(u'楼层', default=1)
    display = models.CharField(max_length=128)
    memo = models.CharField(u'备注', max_length=64)

    def __unicode__(self):
        return 'region:%s idc:%s floor:%s' % (self.region, self.name, self.floor)

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = '机房'


class Contract(models.Model):
    sn = models.CharField(u'合同号', max_length=64, unique=True)
    name = models.CharField(u'合同名称', max_length=64)
    cost = models.IntegerField(u'合同金额')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    license_num = models.IntegerField(u'license数量', null=True, blank=True)
    memo = models.TextField(u'备注', null=True, blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = '合同'

    def __unicode__(self):
        return self.name


class BusinessUnit(models.Model):
    name = models.CharField(u'业务线', max_length=64, unique=True)
    contact = models.ForeignKey('UserProfile')
    user_group = models.ForeignKey('UserGroup', null=True, blank=True)
    memo = models.CharField(u'备注', max_length=64, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = "业务线"


class HandleLog(models.Model):
    asset_info = models.ForeignKey('Asset')
    content = models.TextField(null=True, blank=True)
    creator = models.ForeignKey('UserProfile')
    create_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content

    class Meta:
        verbose_name_plural = "资产变更日志"


class ErrorLog(models.Model):
    name = models.CharField(max_length=256)


class NewAssetApprovalZone(models.Model):
    '''没有注册的资产，允许自动汇报，但是不入库。放到待批准表里临时存储'''
    sn = models.CharField(u'资产SN号', max_length=128, unique=True)  # 资产不能重复汇报,一个资产批准前只能汇报一次
    asset_type_choices = (
        ('server', u'服务器'), ('switch', u'交换机'), ('router', u'路由器'), ('firewall', u'防火墙'), ('wireless', u'无线AP'),)
    device_type = models.CharField(choices=asset_type_choices, max_length=64, blank=True, null=True)
    manufactory = models.CharField(max_length=64, blank=True, null=True)  # 厂商
    model = models.CharField(max_length=128, blank=True, null=True)
    ram_size = models.IntegerField(blank=True, null=True)
    cpu_model = models.CharField(max_length=128, blank=True, null=True)
    cpu_count = models.IntegerField(blank=True, null=True)
    # cpu_core_count = models.IntegerField(blank=True,null=True)
    cpu_physical_count = models.IntegerField(blank=True, null=True)
    # os_type = models.CharField(max_length=64,blank=True,null=True)
    os_platform = models.CharField(u'系统类型', max_length=64, blank=True, null=True)
    os_distribution = models.CharField(u'OS厂商', max_length=64, blank=True, null=True)
    # os_release = models.CharField(max_length=64,blank=True,null=True)
    os_version = models.CharField(u'系统名称', max_length=64, blank=True, null=True)
    data = models.TextField(u'资产数据')  # 这里才是真正详细的数据，批准后存入正式表里面
    date = models.DateTimeField(u'汇报日期', auto_now_add=True)
    approved = models.BooleanField(u'已批准', default=False)
    approved_by = models.ForeignKey('UserProfile', verbose_name=u'批准人', blank=True, null=True)
    approved_date = models.DateTimeField(u'批准日期', blank=True, null=True)

    def __str__(self):
        return self.sn

    class Meta:
        verbose_name = '新上线待批准资产'
        verbose_name_plural = "新上线待批准资产"
        ordering = ['-id']
