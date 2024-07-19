from mcdreforged.command.builder.common import CommandContext
from mcdreforged.command.builder.tools import SimpleCommandBuilder
from mcdreforged.command.command_source import CommandSource
from mcdreforged.minecraft.rtext.style import RColor, RStyle
from mcdreforged.minecraft.rtext.text import RTextBase
from mcdreforged.plugin.si.plugin_server_interface import PluginServerInterface

from auto_restart import plugin_config


def register(server: PluginServerInterface, info: int):
    builder = SimpleCommandBuilder()
    builder.command("!!autorestart", auto_restart)
    builder.register(server)
    server.register_help_message('!!autorestart', 'Config AutoRestart plugin for server')


def auto_restart(source: CommandSource, context: CommandContext):
    source.reply(RTextBase.from_any('=========== AutoRestart Plugin ===========').set_color(RColor.gold).to_colored_text())
    source.reply(RTextBase.from_any('Plugin Status:').set_color(RColor.blue).to_colored_text())
    source.reply(RTextBase.join(': ', (RTextBase.from_any('- Enable').set_color(RColor.gray).set_styles(RStyle.bold),
                                       plugin_config.is_enable())).to_colored_text())
    source.reply(RTextBase.join(': ', (RTextBase.from_any('- ExitCode Whitelist').set_color(RColor.gray).set_styles(RStyle.bold),
                                       plugin_config.get_exitcode_whitelist())).to_colored_text())

