import time

from mcdreforged.plugin.server_interface import PluginServerInterface
from auto_restart import plugin_config


def on_server_stop(server: PluginServerInterface, info: int):
    if plugin_config.is_enable():
        server.logger.info('detected server shutting down, try restart in 3 seconds')
        # try_restart(server)
        time.sleep(plugin_config.get_delay())
        server.start()
