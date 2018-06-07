#!/usr/bin/env python
import little_app
import bson
import sys

from kaiju.arguments import ObjectId
from kaiju.cli import KaijuCLI

cli = KaijuCLI(little_app.trilotest.operations,
                            description="Little test app")
gargs, opargs = cli.parse_args(sys.argv[1:])

little_app.trilotest.handle_kaiju_arguments(gargs)

result = little_app.trilotest.execute(gargs["operation"], opargs)
if isinstance(result, bson.objectid.ObjectId):
    print(result)
else:
    for x in result:
        print(x)


