import time

from mcdreforged.minecraft.rtext.style import RColor
from mcdreforged.minecraft.rtext.text import RTextBase, RText
from mcdreforged.plugin.si.plugin_server_interface import PluginServerInterface

from auto_restart import plugin_config


def on_server_stop(server: PluginServerInterface, code: int):
    if plugin_config.is_enable():
        text = RTextBase.from_any(f'Server exit with code : {code}').set_color(RColor.gold)
        server.logger.info(text.to_colored_text())
        if plugin_config.should_restart(code):
            text = RTextBase.from_any(f'Try restart server').set_color(RColor.blue)
            server.logger.info(text.to_colored_text())
            server.start()
        else:
            text = RTextBase.from_any(f'Code in exit code whitelist, pass restarting').set_color(RColor.blue)
            server.logger.info(text.to_colored_text())
