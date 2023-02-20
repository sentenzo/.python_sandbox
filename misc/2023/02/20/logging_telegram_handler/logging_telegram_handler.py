import logging
import time

import telegram

ANTISPAM_DELAY_SEC = 5 * 60


class TelegramHandler(logging.Handler):
    """Log to telegram chat via Bot API."""

    def __init__(self, level, token: str, chat_id: str) -> None:  # noqa: D107
        super().__init__(level)
        self.bot = None
        self.chat_id = chat_id
        try:
            # an independent instance of a telegram bot object
            self.bot = telegram.Bot(token)
        except Exception:
            pass

        self.prev_msg = None
        self.prev_msg_time = 0

    def emit(self, record):  # noqa: D102
        if not self.bot:
            return
        msg = self.format(record)
        if (
            msg == self.prev_msg
            and self.prev_msg_time - time.time() < ANTISPAM_DELAY_SEC
        ):
            # we don't need the same message to be sent too often
            return
        try:
            self.bot.send_message(chat_id=self.chat_id, text=msg)
            self.prev_msg = msg
            self.prev_msg_time = time.time()
        except Exception:
            pass
