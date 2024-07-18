from mcdreforged.api.all import *


def register(server: PluginServerInterface):
	server.register_command(Literal('!!autorestart').runs(lambda src: src.reply('Now enable server auto restart action')))
	server.register_help_message('!!autorestart', 'Configure restart server')
