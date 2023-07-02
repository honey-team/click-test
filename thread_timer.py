import threading
import time
from typing import Callable

import flet as ft

import utils.labels as labels


class Timer:
    def __init__(
        self,
        text_object: ft.Text,
        progress_bar: ft.ProgressBar,
        time: int = 1,
        on_end: Callable = None,
    ) -> None:
        self.endtime = time

        self.text = text_object
        self.text.value = labels.timer_label(time)

        self.progress = progress_bar

        self.on_end = on_end

    def start(self):
        def thread():
            start_time = self.endtime

            for i in range(self.endtime):
                time.sleep(1)
                self.endtime -= 1
                self.text.value = labels.timer_label(round(self.endtime, 2))
                self.progress.value -= 1 / start_time

                self.text.update()
                self.progress.update()
            else:
                self.text.value = labels.timer_label()
                self.text.update()

                if self.on_end:
                    self.on_end()

        th = threading.Thread(target=thread)
        th.start()

    def reset(self, time: int = 1, on_end: Callable = None):
        self.endtime = time

        self.text.value = labels.timer_label()

        self.on_end = on_end
