"""My new command"""
from dataclasses import dataclass

from simple_parsing import choice
from uetools.core.command import Command, command_builder, newparser
from uetools.core.conf import editor_cmd, find_project, uat
from uetools.format.base import Formatter
from uetools.core.run import popen_with_format
from uetools.plugins.asset_dumper.dumper import Uasset, DataTable

@dataclass
class Arguments:
    """Arguments for my new command"""


class AssetDumper(Command):
    """Dump a UAsset"""

    name: str = "asset-dumper"

    @staticmethod
    def arguments(subparsers):
        """Add arguments to the parser"""
        parser = newparser(subparsers, AssetDumper)
        parser.add_argument(
            "file",
            type=str,
            help="Path to a uasset",
        )

    @staticmethod
    def execute(args):
        """Execute the command"""

    def check_dumper(args):
        asset = DataTable(args.file)
        print(asset.handles)
        print(asset.array_handles)
        print(asset.items)
        print('Unparsed:')
        print(asset.footer)
        