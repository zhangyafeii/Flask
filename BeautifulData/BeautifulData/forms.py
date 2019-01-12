# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/1
@Author: Zhang Yafei
"""
from datetime import timedelta

from wtforms import Form, widgets, validators
from wtforms.fields import simple
from settings import USERNAME, PASSWORD
from flask import session


class LoginForm(Form):
    username = simple.StringField(render_kw={'placeholder':'请输入用户名','class':'form-control'},
                                  label='用户名',
                                  validators=[
                                      validators.DataRequired(message='用户名不能为空.'),
                                      validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
                                  ],
                                  )
    pwd = simple.PasswordField(render_kw={'placeholder':'请输入密码','class':'form-control'},
                               label='密码',
                               # validators=[
                               #     validators.DataRequired(message='密码不能为空.'),
                               #     validators.Length(min=8, message='用户名长度必须大于%(min)d'),
                               #     validators.Regexp(
                               #         regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                               #         message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')
                               #
                               # ],
                               )
    remember = simple.BooleanField(widget=widgets.CheckboxInput(),
                                   render_kw={'style':"width:10%;height:12px;"}
                                   )

    def validate_username(self, field):
        """
        自定义name字段规则
        :param field:
        :return:
        """
        # 最开始初始化时，self.data中已经有所有的值
        # print('钩子函数获取的值', field.data)
        # print('所有的值',self.data)
        print(self.data['username'],self.data['pwd'])
        print(USERNAME,PASSWORD)
        if not all([self.data['username'] == USERNAME, self.data['pwd'] == PASSWORD]):
            raise validators.StopValidation("用户名或密码不正确")

    def validate_remember(self, field):
        if field.data:
            from BeautifulData.views.account import ac
            session.permanent = True
            ac.permanent_session_lifetime = timedelta(days=31)