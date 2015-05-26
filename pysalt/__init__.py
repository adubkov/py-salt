import logging
import salt.client
import salt.config
import salt.loader

try:
  import json
except:
  import simplejson as json

logger = logging.getLogger(__name__)

class Pillar(dict):
  """
  Get pillar data for localhost.

  Example:
    p = Pillar()
    p['zabbix']['user']
    >> 'admin'
  """
  def __init__(self):
    self.caller = salt.client.Caller()
    self.__pillar__ = self.caller.sminion.functions['pillar.items']()

  def __contains__(self, item):
    return item in self.__pillar__

  def __len__(self):
    return len(self.__pillar__)

  def __getitem__(self, item):
    return self.__pillar__.get(item)

  def __repr__(self):
    return json.dumps(self.__pillar__, sort_keys=True, indent=4, separators=(',', ': '))


class Grains(object):
  """
  Get or Set grains for localhost.

  Attributes:
    config (str):   Path to salt-minion config

  Example:
    g = Grains('/etc/salt/minion.config')
    g['os_family']
    >> RedHat

    g['roles'] = 'api'
    g['roles']
    >> api
  """
  def __init__(self, config = '/etc/salt/minion'):
    self.__opts__ = salt.config.minion_config(config)
    self.__grains__ = salt.loader.grains(self.__opts__)
    self.caller = salt.client.Caller()

  def __contains__(self, item):
    return item in self.__grains__

  def __len__(self):
    return len(self.__grains__)

  def __getitem__(self, item):
    return self.__grains__.get(item)

  def __setitem__(self, item, value):
    result = False
    try:
      self.caller.sminion.functions['grains.setval'](item, value)
      self.__grains__[item] = value
      result = True
    except:
      logger.critical("Could not set grains {0}:{1}".format(item, value))
    return result

  def __repr__(self):
    return json.dumps(self.__grains__, sort_keys=True, indent=4, separators=(',', ': '))
