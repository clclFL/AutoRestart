import os

from mcdreforged.minecraft.rtext.style import RColor
from mcdreforged.minecraft.rtext.text import RTextBase
from mcdreforged.plugin.si.plugin_server_interface import PluginServerInterface
from ruamel.yaml import YAML

ENABLE = False  # 插件状态
AVOID = []  # 退出码列表，当退出码为区间当中的值时不进行自动重启


def init_config(server: PluginServerInterface, info):
    config_path = os.path.join(server.get_data_folder(), 'config.yml')
    if not os.path.exists(config_path):
        with open(config_path, 'w') as file_handler:
            file_handler.write('enable:  false\n')
            file_handler.write('avoid_restart_on_exit_code:  \n')
            file_handler.write('  - 0')

    with open(os.path.join(server.get_data_folder(), 'config.yml'), 'r') as file_handler:
        yaml = YAML()
        config = yaml.load(file_handler)
        global ENABLE, AVOID
        ENABLE = config['enable']
        AVOID = config['avoid_restart_on_exit_code']

    text = RTextBase.from_any('Successfully load plugin configuration').set_color(RColor.gold)
    server.logger.info(text.to_colored_text())


def is_enable():
    global ENABLE
    return ENABLE


def get_exitcode_whitelist() -> str:
    global AVOID
    if AVOID is None:
        return 'Any'
    return ', '.join(str(code) for code in AVOID)


def should_restart(code: int) -> bool:
    global AVOID
    if AVOID is None:
        return True
    return code not in AVOID


