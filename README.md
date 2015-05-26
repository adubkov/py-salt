# py-salt
Simple python interface for salt grains and pillars

# Install

You can install py-salt module with pip:
```
pip install py-salt
```



Example:
```python
from pysalt import Pillar, Grains

p = Pillar()
g = Grains()

# Print pillar list
print(p)

# Print `os_family` grain
print(g['os_family'])

# Set 'zabbix_server' roles in grain `roles`
g['roles'] = 'zabbix_server'
```
