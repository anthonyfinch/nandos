"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.db import connection


class SimpleTest(TestCase):
    def test_basic_addition(self):
        cursor = connection.cursor()
        cursor.execute("SELECT PostGIS_full_version()")
        row = cursor.fetchone()
        self.assertEqual(row, (u'POSTGIS="1.5.3" GEOS="3.3.3-CAPI-1.7.4" PROJ="Rel. 4.7.1, 23 September 2009" LIBXML="2.8.0" USE_STATS',))
