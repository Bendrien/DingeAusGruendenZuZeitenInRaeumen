# This script converts a flat JSON structure to CSV.
# Copyright (C) 2017  Maximilian Wagenbach

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import json
import csv

with open("FinalData.json") as file:
    data = json.load(file)

with open("FinalData.csv", "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(data[0].keys())
    for item in data:
        csv_file.writerow(item.values())
