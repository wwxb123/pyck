from django.db import models

from utils.db import tableNames


class Project(models.Model):
    """
    项目模型表
    """
    name = models.CharField('项目名称',max_length=200,unique=True,help_text='项目名称')
    leader = models.CharField('负责人',max_length=48,help_text='负责人')
    desc = models.CharField('项目简述',max_length=48,null=True,blank=True,help_text='项目简述')
    c_time = models.DateTimeField('创建时间',auto_now_add=True)

    class Meta:
        db_table = tableNames.Project #指定当前模型创建的表名,如果不指定表名，默认为类名Project
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name
        ordering = ['-c_time']

    def __str__(self):
        #方便调式，如果不写此方法，默认返回project的一个对象
        return self.name
class Environment(models.Model):
    """
    环境模型表
    """
    name = models.CharField('环境名称',max_length=128,help_text='环境名称')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,help_text='所属项目')#通过外键设置级联删除
    host = models.URLField('主机地址',help_text='主机地址')
    db_config = models.JSONField('数据库设置',default=dict,blank=True,help_text='数据库设置')

    class Meta:
        db_table = tableNames.Environment
        verbose_name = '项目环境'
        verbose_name_plural = verbose_name
        constraints = [#设置联合索引唯一(环境名和项目)
            models.UniqueConstraint(fields=['name','project'],name='unique_env_name')
        ]

    def __str__(self):
        return self.name