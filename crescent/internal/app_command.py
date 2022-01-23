from __future__ import annotations

from enum import IntEnum
from typing import TYPE_CHECKING

from attr import define
from hikari import UNDEFINED, CommandOption

if TYPE_CHECKING:
    from typing import Optional, Sequence
    from hikari import Snowflake, UndefinedOr, UndefinedNoneOr


@define(hash=True)
class Unique:
    name: str
    guild_id: UndefinedNoneOr[Snowflake]
    group: UndefinedNoneOr[str]
    sub_group: UndefinedNoneOr[str]

    def __post_init__(self):
        if self.guild_id is UNDEFINED:
            self.guild_id = None
        if self.group is UNDEFINED:
            self.group = None
        if self.sub_group is UNDEFINED:
            self.sub_group = None


__all__: Sequence[str] = (
    "AppCommandMeta",
    "AppCommand",
)


class AppCommandType(IntEnum):
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3


@define
class AppCommand:
    """Local representation of an Application Command"""
    type: AppCommandType
    name: str
    description: str
    guild_id: Optional[Snowflake]
    options: Optional[Sequence[CommandOption]]
    default_permission: UndefinedOr[bool]

    id: Optional[Snowflake] = None

    __eq__props: Sequence[str] = (
        "type",
        "name",
        "description",
        "guild_id",
        "options"
    )

    def __eq__(self, __o: object) -> bool:
        for prop in self.__eq__props:
            my_attr = getattr(self, prop)
            o_attr = getattr(__o, prop)

            if my_attr != o_attr and my_attr and o_attr:
                return False

        return True

    def is_same_command(self, o: AppCommand):
        return all(
            (
                self.guild_id == o.guild_id,
                self.name == o.name,
                self.type == o.type
            )
        )


@define
class AppCommandMeta:
    app: AppCommand
    group: Optional[str] = None
    sub_group: Optional[str] = None

    @property
    def unique(self) -> Unique:
        return Unique(
            self.app.name,
            self.app.guild_id,
            self.group,
            self.sub_group,
        )
