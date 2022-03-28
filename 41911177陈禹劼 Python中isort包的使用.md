# Python中isort包的使用

isort 可自动对 Python 的 import 语句进行排序和分段。可将大量的 import 结构转成非常适合阅读的排版。提供一个命令行工具、Python 库和 Kate 插件。

在使用isort之后，代码能够按照字母表顺序对 imports 进行排序，并自动按类型划分部分，使得代码的可阅读性变得更强。

举一个简单的例子，在使用isort前的代码可能是这样的:

```python
# Before isort
from my_lib import Object

import os

from my_lib import Object3

from my_lib import Object2

import sys

from third_party import lib15, lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10, lib11, lib12, lib13, lib14

import sys

from __future__ import absolute_import

from third_party import lib3

print("Hey")
print("yo")
```

那么在使用了isort之后代码就会变成下面这样：

```
# After isort
from __future__ import absolute_import

import os
import sys

from third_party import (lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8,
                         lib9, lib10, lib11, lib12, lib13, lib14, lib15)

from my_lib import Object, Object2, Object3

print("Hey")
print("yo")
```

这样一来，代码就变得更加易读了，其可阅读性的增加使得不单单只有编写者能清楚代码内容，而其他人也能方便的进行阅读和修改
