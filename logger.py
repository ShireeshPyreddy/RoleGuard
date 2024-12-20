import logging

logging.basicConfig(level=logging.DEBUG, filename='audit_log.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class IgnoreWerkzeugFilter(logging.Filter):
    def filter(self, record):
        # Return False to ignore logs from werkzeug, True to process them
        return not record.name.startswith('werkzeug')


logging.getLogger().addFilter(IgnoreWerkzeugFilter())

logging.getLogger('werkzeug').propagate = False
