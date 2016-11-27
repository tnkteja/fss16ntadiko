#!/usr/bin/python
# coding:utf8

import logging
import logging.config


logging.config.dictConfig({
	    "formatters": {
	        "verbose": {
	            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
	        },
	        "simple": {
	            "format": "%(asctime)s %(levelname)s %(message)s"
	        },
	    },
	    "filters": {
	    },
	    "handlers": {
	        "null": {
	            "level":"DEBUG",
	            "class":"logging.NullHandler",
	        },
	        "console":{
	            "level":"DEBUG",
	            "class":"logging.StreamHandler",
	            "formatter": "simple"
	        }
	    },
	    "loggers": {
	        "dsl": {
	            "handlers":["console"],
	            "propagate": True,
	            "level":"INFO",
	        },
	        "optimizers": {
	            "handlers": ["console"],
	            "level": "INFO",
	            "propagate": False,
	        },
	        "problems": {
	            "handlers": ["console"],
	            "level": "INFO",
	        }
	    }
	}
	})