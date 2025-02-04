import os.path
from configobj import ConfigObj

config_file_name = 'helper_config'
path_helper = (os.path.abspath(os.getcwd()))
path_config_file_name = path_helper + '/' + config_file_name

config = ConfigObj(path_config_file_name, encoding='utf8')

if os.path.exists(path_config_file_name) == False:

    config['Setting_helper'] = {'path_db': ''}

    config['Helper_export'] = {'path_export': path_helper}

    config['User'] = {
        'checkBox_branch':'False',
        'checkBox_department':'False',
        'checkBox_system':'False',
        'checkBox_szi':'False',

        'checked_branch': '',
        'checked_department':'',
        'checked_system':'',
        'checked_szi':'',

        'checkB_statusOn':'True',
        'checkB_statusOff':'True',

        'current_indexPage':'',

        'defolt_branch':'',
        'defolt_department':''
        }

    config['Usb'] = {
        'checkBox_branch':'False',
        'checkBox_department':'False',

        'checked_branch': '',
        'checked_department':'',

        'checkB_statusOn':'True',
        'checkB_statusOff':'True',

        'current_indexPage':'',

        'defolt_branch':'',
        'defolt_department':''
        }

    config['Equipment'] = {
        'checkBox_branch':'False',
        'checkBox_department':'False',

        'checked_branch': '',
        'checked_department':'',

        'checkB_statusOn':'True',
        'checkB_statusOff':'True',

        'current_indexPage':'',

        'defolt_branch':'',
        'defolt_department':''
        }

    config['Skr'] = {
        'checkBox_branch':'False',
        'checkBox_department':'False',

        'checked_branch': '',
        'checked_department':'',

        'checkB_statusOn':'True',
        'checkB_statusOff':'True',

        'current_indexPage':'',

        'defolt_branch':'',
        'defolt_department':''
        }

    config['Szi'] = {
        'checkBox_all_Branch': 'False',
        'checkBox_all_Department': 'False',
        'checkBox_all_Szi':'False',
        'checkBox_all_User': 'False',
        'checkBox_all_Equipment': 'False',

        'checked_item_Branch': '',
        'checked_item_Department': '',
        'checked_item_Szi':'',
        'checked_item_User': '',
        'checked_item_Equipment': '',

        'checkB_statusOn': 'True',
        'checkB_statusOff': 'True',

        'current_indexPage': '',

        'defolt_branch': '',
        'defolt_department': ''
    }

    config.write()
