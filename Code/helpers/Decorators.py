from typing import Callable

from pyrogram import Client
from pyrogram.types import Message

from Code import TELEGRAM_SUDO_ID as SUDO_USERS


def authorized_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return decorator
