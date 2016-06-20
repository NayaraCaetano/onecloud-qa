#!/usr/bin/env python
import os
import sys
import signal

settings_arg = [arg for arg in sys.argv if arg.startswith('--settings=')]


if settings_arg and 'functional_test' in settings_arg[0]:
    from coverage import coverage
    cov = coverage(omit='*/.envs/*.*')
    cov.start()


def signal_handler(signal, frame):
    if settings_arg and 'functional_test' in settings_arg[0]:
        cov.stop()
        cov.save()
    exit()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.base")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
