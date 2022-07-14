from hikari import Permissions, UNDEFINED, User, Message
from crescent import command, Context, user_command, message_command


def test_defaults():
    @command
    async def test_command(ctx: Context):
        ...

    assert test_command.metadata.app.name == "test_command"
    assert test_command.metadata.app.guild_id is None
    assert test_command.metadata.app.description == "No Description"
    assert test_command.metadata.app.default_member_permissions is UNDEFINED
    assert test_command.metadata.app.is_dm_enabled


def test_user_command_defaults():
    @user_command
    async def test_command(ctx: Context, user: User):
        ...
    assert test_command.metadata.app.name == "test_command"
    assert test_command.metadata.app.guild_id is None
    assert test_command.metadata.app.default_member_permissions is UNDEFINED
    assert test_command.metadata.app.is_dm_enabled


def test_message_command_defaults():
    @user_command
    async def test_command(ctx: Context, user: Message):
        ...

    assert test_command.metadata.app.name == "test_command"
    assert test_command.metadata.app.guild_id is None
    assert test_command.metadata.app.default_member_permissions is UNDEFINED
    assert test_command.metadata.app.is_dm_enabled


def test_not_default():
    @command(
        name="test_name",
        guild=123456,
        description="test description",
        default_member_permissions=Permissions.BAN_MEMBERS,
        dm_enabled=False,
    )
    async def test_command(ctx: Context):
        ...

    assert test_command.metadata.app.name == "test_name"
    assert test_command.metadata.app.guild_id == 123456
    assert test_command.metadata.app.description == "test description"
    assert test_command.metadata.app.default_member_permissions is Permissions.BAN_MEMBERS
    assert not test_command.metadata.app.is_dm_enabled


def test_message_command_not_default():
    @message_command(
        name="Test Name",
        guild=123456,
        default_member_permissions=Permissions.BAN_MEMBERS,
        dm_enabled=False,
    )
    async def test_command(ctx: Context):
        ...

    assert test_command.metadata.app.name == "Test Name"
    assert test_command.metadata.app.guild_id == 123456
    assert test_command.metadata.app.default_member_permissions is Permissions.BAN_MEMBERS
    assert not test_command.metadata.app.is_dm_enabled


def test_user_command_not_default():
    @user_command(
        name="Test Name",
        guild=123456,
        default_member_permissions=Permissions.BAN_MEMBERS,
        dm_enabled=False,
    )
    async def test_command(ctx: Context):
        ...

    assert test_command.metadata.app.name == "Test Name"
    assert test_command.metadata.app.guild_id == 123456
    assert test_command.metadata.app.default_member_permissions is Permissions.BAN_MEMBERS
    assert not test_command.metadata.app.is_dm_enabled
