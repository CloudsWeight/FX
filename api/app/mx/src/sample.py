#!/usr/bin/env python
from fed import Fed 
import json
fed = Fed()

data = fed.fxs('trade', '2004-01-01', '2024-10-10', 'japan')
print(json.dumps(data, indent=4))
x, y, c = fed.lists(data)
fed.plot(x, y, c)