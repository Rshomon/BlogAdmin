from django.db import models
from mptt.models import MPTTModel
from datetime import datetime
# Create your models here.
class Tag(models.Model):
    name = models.CharField(verbose_name='文章标签', max_length=20)
    number = models.IntegerField(verbose_name='标签数目', default=1)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Category(MPTTModel):
    name = models.CharField('文章分类', max_length=50, unique=True)
    parent_name = models.ForeignKey('self', verbose_name='上级分类', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='分类数目', default=1)
    class Meta:
        db_table = 'category'
        verbose_name = verbose_name_plural = '文章分类'

    class MPTTMeta:
        parent_attr = 'parent_name'


    def __str__(self):
        return self.name

# class Detail_content(models.Model):
#     """
#     博客详细内容
#     """


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField(verbose_name='标题', max_length=100)
    abstract = models.TextField(verbose_name='摘要', max_length=200, default='', blank=True)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    content = models.TextField()
    # content_id = models.IntegerField(verbose_name='文章id',default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now())
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')


    class Meta:
        verbose_name = '我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title