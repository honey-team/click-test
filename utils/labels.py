from utils.annotations import Strable


# helpers
def dev(s: str) -> str:
    s += ' (DEV)'
    return s

def timer_label(time: Strable = '0') -> str:
    return f'Времени осталось: {time}'

# Constants


# Settings

# History
DONT_WRITE_HISTORY = 'Не записывать историю'
RESET_HISTORY = 'Сбросить историю'

HISTORY_RESETED = 'История успешно сброшена'

# Personalization
LIGHT_THEME = 'Светлая тема'
DARK_THEME = 'Темная тема'

# DEV
LINECHART = dev('График')

# Categories names
HISTORY = 'История'
PERSONALIZATION = 'Персонализация'
DEV = 'Для разработчиков'
