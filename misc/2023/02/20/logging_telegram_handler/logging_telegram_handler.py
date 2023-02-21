import logging
import sys
import time

import telegram
from telegram.error import TelegramError

ANTISPAM_DELAY_SEC = 5 * 60

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler(sys.stdout))


class TelegramHandler(logging.Handler):
    """Log to telegram chat via Bot API."""

    def __init__(self, level, token: str, chat_id: str) -> None:  # noqa: D107
        super().__init__(level)
        self.bot = None
        self.chat_id = chat_id
        try:
            # an independent instance of a telegram bot object
            self.bot = telegram.Bot(token)
        except TelegramError as ex:
            logger.error(
                "Failed to create a Bot instance. "
                "Logging to Telegram won't work.\n"
                f"TelegramError: {ex}"
            )

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
            logger.debug(
                f"The same message in less, than {ANTISPAM_DELAY_SEC} secs. "
                "Sending to Telegram chat was suppressed."
            )
            return
        try:
            self.bot.send_message(chat_id=self.chat_id, text=msg)
            self.prev_msg = msg
            self.prev_msg_time = time.time()
        except TelegramError as ex:
            logger.error(
                "An error occured while sanding log-message "
                f"to telegram chat: {ex}"
            )
