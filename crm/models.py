from django.db import models

from utils.db import tableNames

"""
1.创建表类，编写字段信息
2.在项目setting中注册++》INSTALLED_APPS下添加'crm.apps.CrmConfig'
3.生成迁移记录 python manage.py makemigrations crm
4.执行迁移记录 
"""


class Student(models.Model):
    """
    学生表
    """
    name = models.CharField('学生姓名', max_length=20)
    age = models.SmallIntegerField('年龄', default='')
    sex = models.SmallIntegerField('性别', default=1, )
    qq = models.CharField('QQ号', max_length=20, default='')
    phone = models.CharField('手机号', max_length=11, default='')
    c_time = models.DateTimeField('创建时间', auto_now_add=True)
    detail = models.OneToOneField('StudentDetail', on_delete=models.RESTRICT,null=True)  # 设置学生表与学生详情表一对一关系
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True)  # 设置学生表与班级表一对多关系

    def __str__(self):
        return '%s-%s' % (self.name, self.age)

    class Meta:
        db_table = tableNames.Student


class StudentDetail(models.Model):
    """
    学生信息详情表
    """
    idno = models.CharField('身份证号码', max_length=18, default='')
    college = models.CharField('毕业学校', max_length=48, default='')

    class Meta:
        db_table = tableNames.StudentDetail

    def __str__(self):
        return '%s-%s' % (self.idno, self.college)


class Grade(models.Model):
    """
    班级表
    """
    name = models.CharField('班级名称', max_length=20)
    num = models.CharField('班期', max_length=20)

    class Meta:
        db_table = tableNames.Grade

    def __str__(self):
        return '%s-%s' % (self.name, self.num)


class Course(models.Model):
    """
    课程表
    # 学生表与课程表多对多关系,会生成一个COURSE_student的关联表；
    # 如果关联关系放在Student中生成的表名为STUDENT_course；
    # 如果已经生成过关联表必须手动删除，并把django_migrations中对应的迁移记录也删除
    # student = models.ManyToManyField('Student')
    # 学生表与课程表多对多关系，通过through指定显示的创建关联模型Enroll(不是表名tableNames.Enroll),可以增加别的字段
    """
    name = models.CharField('课程名称', max_length=20)
    students = models.ManyToManyField('Student', through='Enroll')

    class Meta:
        db_table = tableNames.Course

    def __str__(self):
        return '%s' % (self.name)


class Enroll(models.Model):
    """
    报名表
    """
    student = models.ForeignKey('Student', on_delete=models.CASCADE)  #
    course = models.ForeignKey('Course', on_delete=models.CASCADE)  #
    pay = models.DecimalField('金额', max_digits=20, decimal_places=2)  # decimal_places指定小数位数
    c_time = models.DateTimeField('报名时间', auto_now_add=True)

    class Meta:
        db_table = tableNames.Enroll

    def __str__(self):
        return '%s-%s-%s' % (self.student, self.course, self.pay)
