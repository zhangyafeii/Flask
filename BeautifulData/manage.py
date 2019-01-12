# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/1
@Author: Zhang Yafei
"""
from BeautifulData import create_app
from flask_script import Manager
from Admin import admin_setup

admin_setup.admin_auto_discover()

app = create_app()
# manager = Manager(app)

if __name__ == '__main__':
    app.run()
    # manager.run()