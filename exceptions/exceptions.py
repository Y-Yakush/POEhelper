class ExitException(Exception):
    def __str__(self):
        return f'Нажата комбинация клавиш для завершения программы. Перезапустите программу снова!'