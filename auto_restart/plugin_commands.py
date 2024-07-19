from mcdreforged.command.builder.common import CommandContext
from mcdreforged.command.builder.tools import SimpleCommandBuilder
from mcdreforged.command.command_source import CommandSource
from mcdreforged.plugin.server_interface import PluginServerInterface
from auto_restart.plugin_config import get_status_str


def register(server: PluginServerInterface):
    builder = SimpleCommandBuilder()
    builder.command("!!autorestart", auto_restart)
    builder.register(server)


def auto_restart(source: CommandSource, context: CommandContext):
    source.reply(get_status_str())
