from pysalt import Pillar, Grains

p = Pillar()
g = Grains()

print(p)

print(g['os_family'])

g['roles'] = 'zabbix_server'
