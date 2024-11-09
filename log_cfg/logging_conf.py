import sys
from log_cfg.log_filters import DebugWarningLogFilter, CriticalLogFilter, ErrorLogFilter, InfoFilter
sstart='Бот запущен'

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_start': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - {BOT_START_WORK} - %(message)s'
        }

    },

    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
        'debug_warning_filter': {
            '()': DebugWarningLogFilter,
        },
        'info_filter': {
            '()': InfoFilter
        }
    },
    'handlers': { 'info_h': {
            'class': 'logging.FileHandler',
            'filename': 'files_log/info.log',
            'mode': 'w',
            'level': 'DEBUG',
            'formatter': 'formatter_start',
            'filters': ['error_filter']
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'filename': 'files_log/critical.log',
            'mode': 'w',
            'formatter': 'formatter_start',
            'filters': ['critical_filter']
        },
        'WARNING_file': {
            'class': 'logging.FileHandler',
            'filename': 'files_log/WARNING.log',
            'mode': 'w',
            'formatter': 'formatter_start',
            'filters': ['critical_filter']
        },
        'ERROR_file': {
            'class': 'logging.FileHandler',
            'filename': 'files_log/ERROR.log',
            'mode': 'w',
            'formatter': 'formatter_start',
            'filters': ['critical_filter']
        }
    },

    'loggers': {
        'log_cfg.mod_log': {
            'level': 'INFO',
            'handlers': ['info_h', 'critical_file', 'WARNING_file', 'ERROR_file']

        },
        'log_cfg.def_log': {
            'handlers': ['info_h']
        }
    },
    'root': {
        'formatters': 'formatter_start',
        'handlers': ['info_h']
    }
}