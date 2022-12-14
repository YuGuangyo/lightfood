from django.db import models

# Create your models here.
from django.db import models
__all__ = ['GoodSpu', 'Imgs', 'GoodsKinds', 'GoodSku', 'Shift']
# 34589
class GoodSpu(models.Model):
    type_id = models.AutoField(primary_key=True)  # 商品id主键
    type_name = models.CharField(max_length=32)  # 商品名称
    type_details = models.CharField(max_length=32)  # 商品详情
    # type_kinds_id = models.ForeignKey(to='GoodsKinds',on_delete=models.CASCADE,null=True,related_name='kinds')
    type_kinds_id = models.ForeignKey(to='GoodsKinds',on_delete=models.CASCADE,null=True,related_name='kinds')
    type_shift_id = models.ForeignKey(to= 'Shift',on_delete=models.CASCADE,null=True)
    type_path = models.CharField(max_length=128,default=1)    #spu的路径
class Imgs(models.Model):  # 菜品图片表
    img_id = models.AutoField(primary_key=True)  # 商品id主键
    img_name = models.CharField(max_length=32)  # 图片名称
    img_path = models.CharField(max_length=128)  # 图片路径
    img_type_id = models.ForeignKey(to='GoodSpu', on_delete=models.CASCADE,null=True)
class GoodsKinds(models.Model):
    goods_kinds_id = models.AutoField(primary_key=True)  # 商品id主键
    goods_kings_name = models.CharField(max_length=32)  # 商品种类名称

class GoodSku(models.Model):
    goods_id = models.AutoField(primary_key=True)  # 商品规格id主键
    goods_name = models.CharField(max_length=32)  # 名称
    goods_price = models.DecimalField(max_digits=5, decimal_places=2)  # 单价
    goods_rest = models.IntegerField()  # 库存
    CHOICES = ((1, "在售"), (2, "下架"))
    goods_statue = models.IntegerField(choices=CHOICES)  # 状态
    goods_type_id = models.ForeignKey(to= 'GoodSpu', on_delete=models.CASCADE,null=True)
    goods_SkuType_id = models.ForeignKey(to= 'SkuType',on_delete=models.CASCADE,null=True)
    goods_order_id = models.ForeignKey(to= 'app_shopping.OrderInfo',on_delete=models.CASCADE,null=True,blank=True)
class Shift(models.Model):
    shift_id = models.AutoField(primary_key=True)  #轮播id主键
    discount_url = models.CharField(max_length=32)
    discount_count = models.BooleanField(default=0)

class SkuType(models.Model):
    SkuType_id = models.AutoField(primary_key=True)
    SkuType_name = models.CharField(max_length=32)  # 名称