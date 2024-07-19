from mcdreforged.api.all import *

from auto_restart import plugin_commands
from auto_restart import plugin_logic
from auto_restart import plugin_config


def on_load(server: PluginServerInterface, old_module):
    # server.logger.info(msg)
    server.register_event_listener(MCDRPluginEvents.PLUGIN_LOADED, plugin_commands.register)
    server.register_event_listener(MCDRPluginEvents.PLUGIN_LOADED, plugin_config.init_config)
    server.register_event_listener(MCDRPluginEvents.SERVER_STOP, plugin_logic.on_server_stop)



