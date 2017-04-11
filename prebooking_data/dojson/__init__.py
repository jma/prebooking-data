# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017 RERO.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, RERO does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Invenio module for pre booking."""


import dojson


prebooking = dojson.Overdo()


@prebooking.over('recid', '^001')
def control_number(self, key, value):
    """Record Identifier."""
    return value


@prebooking.over('rero_id', '^035__')
def rero_id(self, key, value):
    """Language Code."""
    return "http://data.rero.ch/01-" + value.get('a')


@prebooking.over('title', '^245__')
# @utils.filter_values
def title(self, key, value):
    """Other title Statement."""
    return {
        'maintitle': value.get('a'),
        'subtitle': value.get('b'),
        'full': myutils.concatenate(value, ['a', 'b']),
        'lang': lang2ln(value.get('9'))
    }
