# -*- coding: utf-8 -*-

from django.db import models

class status(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    memo = models.TextField(u'备注',null=True,blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "状态"

class DeviceType(models.Model):
    '''设备类型'''
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)
    memo = models.CharField(max_length=256,null=True,blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    updata_at = models.DateTimeField(blank=True,auto_now=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "设备类型"

class Asset(models.Model):
    '''资产总表'''
    device_type = models.ForeignKey('DeviceType',on_delete=models.CASCADE)
    device_status = models.ForeignKey('status',default=1,null=True,blank=True,on_delete=models.CASCADE)
    cabinet_num = models.CharField(u'机柜号',max_length=30,null=True,blank=True)
    cabinet_order = models.CharField(u'机柜序号',max_length=30,null=True,blank=True)
    memo = models.TextField(u'备注',null=True,blank=True)
    create_at = models.DateTimeField(blank=True,auto_now_add=True)
    update_at = models.DateTimeField(blank=True,auto_created=True)
    idc = models.ForeignKey('IDC',verbose_name=u'IDC机房',null=True,blank=True,on_delete=models.CASCADE)


class IDC(models.Model):
    region = models.CharField(u'区域',max_length=64)
    name = models.CharField(u'机房名称',max_length=32)
    floor = models.IntegerField(u'楼层',default=1)
    display = models.CharField(max_length=128)
    memo = models.CharField(u'备注',max_length=64)
    def __unicode__(self):
        return 'region:%s idc:%s floor:%s' % (self.region,self.name,self.floor)

    class Meta:
        verbose_name = '机房'
        verbose_name_plural = '机房'
