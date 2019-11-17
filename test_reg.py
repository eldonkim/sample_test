#

import re

data = """
park 870123-1652432
kim  730705-1652416
"""


pat = re.compile(r'(\d{6})([-])\d{7}')
p_pat = re.compile(r'(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)')

print(pat.sub('\g<1>-*******',data))
print(p_pat.sub('\g<2> \g<1> ', 'kim 010-8141-8462'))