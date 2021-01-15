import logging


class ModuleFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        modulesToLog = ["us_data", "urllib3"]

        for module in modulesToLog:
            if record.name.startswith(module):
                return True

        return False