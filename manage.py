#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import importlib
import json
from eventbus_intializer import bus

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'c_hat_server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    load_plugins()
    bus.start()
    execute_from_command_line(sys.argv)

def load_plugins():
    plugins_json = json.load(open("plugins.json"))
    for plugin in plugins_json:
        module = importlib.import_module(f"plugins.{plugins_json[plugin]}.{plugins_json[plugin]}")
        module.initialize_event_bus(bus)
        print(f"Registered tasks for plugin {plugins_json[plugin]}")


if __name__ == '__main__':
    main()
