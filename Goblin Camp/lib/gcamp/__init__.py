# Copyright 2010-2011 Ilkka Halila
# This file is part of Goblin Camp.
# 
# Goblin Camp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Goblin Camp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License 
# along with Goblin Camp. If not, see <http://www.gnu.org/licenses/>.
#
from . import log, events, utils, config, ui, entities
import _gcampapi

getVersionString = _gcampapi.getVersionString
getVersionString.__doc__ = 'Returns Goblin Camp version as a string'

isDebugBuild = _gcampapi.isDebugBuild
isDebugBuild.__doc__ = 'Returns True if running a debug build'

isDevMode = _gcampapi.isDevMode
isDevMode.__doc__ = 'Returns True if running in a devmode'

delay = _gcampapi.delay
delay.__doc__ = 'Run a function after a delay'
