# -*- coding: utf-8 -*-
"""
/***************************************************************************
 csv2points
                                 A QGIS plugin
 csv2points
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-11-05
        copyright            : (C) 2020 by gistechs
        email                : gistechs9@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load csv2points class from file csv2points.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .csv2points import csv2points
    return csv2points(iface)
