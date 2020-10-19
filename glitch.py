"""
Among Us Impostor Glitch
Copyright (C) 2020  OPtimal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from time import sleep
import subprocess
import json
from random import choice

print("""
Among Us Impostor Glitch  Copyright (C) 2020  OPtimal
This program comes with ABSOLUTELY NO WARRANTY; See LICENSE.md for details.
This is free software, and you are welcome to redistribute it
under certain conditions; See LICENSE.md for details.
""")

list = []

with open("positions.json", "r") as file:
	list = [tuple(x) for x in json.load(file)]

lastchoice=(0, 0)

while True:
	i = choice(list)
	if i == lastchoice: continue
	subprocess.call(["xdotool", "mousemove", i[0], i[1]])
	subprocess.call(["xdotool", "click", "1"])
	lastchoice = tuple(i)
