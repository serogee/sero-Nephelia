import discord
from types import NoneType
from typing import Union

class Flags(tuple):

    def __new__(cls, flags_list, flags_raw):
        return super(Flags, cls).__new__(cls, tuple(flags_list))

    def __init__(self, flags_list, flags_raw) -> None:
        self.raw = flags_raw

    def __str__(self) -> str:
        return self.raw
    
    def __repr__(self) -> str:
        return f"<flags_raw: {self.raw}, activated_flags: {super().__str__()}>"

class Context:

    def __init__(self, origin, command, prefix, invoker, flags: Union[Flags, NoneType]) -> None:
        self.origin = origin
        self.command = command
        self.prefix = prefix
        self.invoker = invoker
        self.flags = flags

    async def reply(self, *args, **kwargs) -> None:
        pass

    async def send(self, *args, **kwargs) -> None:
        pass

    async def delete(self, *args, **kwargs) -> None:
        pass

    async def get_reference(self) -> discord.Message:
        return None

    def get_author(self) -> discord.Member:
        return None
    
    def get_channel(self):
        return None

    def get_guild(self) -> discord.Guild:
        return None