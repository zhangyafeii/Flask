from django.db import models


class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    #m = models.ManyToManyField('Role')

    class Meta:
        verbose_name_plural='用户表'

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色表
    """
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural='角色表'

    def __str__(self):
        return self.name


class UserinfoToRole(models.Model):
    """
    用户和角色之间是多对多关系
    """
    user = models.ForeignKey(to='UserInfo',on_delete=models.CASCADE)
    role = models.ForeignKey(to='Role',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='用户分配角色表'

    def __str__(self):
        return '{}-{}'.format(self.user.username,self.role.name)


class Action(models.Model):
    """
    每个url地址中的具体操作权限
    ?get        查询
    ?post       增
    ?put        改
    ?delete     删
    """
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural='操作表'

    def __str__(self):
        return self.caption


class Permission(models.Model):
    """
    url地址权限
    """

    caption = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    menu = models.ForeignKey('Menu',null=True,blank=True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural='URL表'

    def __str__(self):
        return '{}-{}'.format(self.caption,self.url)


class PermissionToAction(models.Model):
    """
    url权限与具体操作权限多对多关系
    """
    permission = models.ForeignKey(to='Permission',on_delete=models.CASCADE)
    action = models.ForeignKey(to='Action',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='权限表'

    def __str__(self):
        return '{}-{}:{}?t={}'.format(self.permission.caption,self.action.caption,self.permission.url,self.action.code)


class RoleToPremissionToAction(models.Model):
    """
    角色与权限是多对多关系
    """
    role = models.ForeignKey(to='Role',on_delete=models.CASCADE)
    p2a = models.ForeignKey(to='PermissionToAction',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='角色分配权限'

    def __str__(self):
        return '{}-{}'.format(self.role.name,self.p2a)


class Menu(models.Model):
    """
    1   菜单1     null
    2   菜单2     null
    3   菜单3     null
    4   菜单1.1    1
    5   菜单1.2    1
    6   菜单1.2.1  4
    无最后一层
    """
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self',related_name='p',null=True,blank=True,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='菜单表'

    def __str__(self):
        return self.caption