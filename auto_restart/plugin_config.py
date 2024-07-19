import os

from mcdreforged.plugin.server_interface import PluginServerInterface
from ruamel.yaml import YAML
ENABLE = False  # 插件状态
DELAY = 3  # 重启间隔


def init_config(server: PluginServerInterface, info):
    config_path = os.path.join(server.get_data_folder(), 'config.yml')
    if not os.path.exists(config_path):
        with open(config_path, 'w') as file_handler:
            file_handler.write('enable:  false\n')
            file_handler.write('delay:  3\n')

    with open(os.path.join(server.get_data_folder(), 'config.yml'), 'r') as file_handler:
        yaml = YAML()
        config = yaml.load(file_handler)
        global ENABLE, DELAY
        ENABLE = config['enable']
        DELAY = config['delay']

    ensure_delay(server)
    server.logger.info(get_status_str())


def get_status_str() -> str:
    global ENABLE, DELAY
    return (f'AutoRestart status : \n'
            + f'ENABLE: {ENABLE} \n'
            + f'DELAY: {DELAY}')


def ensure_delay(server: PluginServerInterface) -> None:
    global DELAY
    if DELAY is None or DELAY < 0:
        DELAY = 3
    server.logger.info(f'Bad Argument for DELAY: {DELAY}, use default value: 3')


def is_enable():
    global ENABLE
    return ENABLE


def get_delay():
    global DELAY
    return DELAY

