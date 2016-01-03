#coding=utf-8
__author__ = 'shuxieliu'

from oslo_config import cfg

opts = [
    cfg.StrOpt('bind_host', default='0.0.0.0'),
    cfg.IntOpt('bind_port', default=9292),
]

CONF = cfg.CONF
CONF(default_config_files='D://app.conf')