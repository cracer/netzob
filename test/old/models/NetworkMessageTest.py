#!/usr/bin/python
# -*- coding: utf-8 -*-

#+---------------------------------------------------------------------------+
#|          01001110 01100101 01110100 01111010 01101111 01100010            |
#|                                                                           |
#|               Netzob : Inferring communication protocols                  |
#+---------------------------------------------------------------------------+
#| Copyright (C) 2011 Georges Bossert and Frédéric Guihéry                   |
#| This program is free software: you can redistribute it and/or modify      |
#| it under the terms of the GNU General Public License as published by      |
#| the Free Software Foundation, either version 3 of the License, or         |
#| (at your option) any later version.                                       |
#|                                                                           |
#| This program is distributed in the hope that it will be useful,           |
#| but WITHOUT ANY WARRANTY; without even the implied warranty of            |
#| MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              |
#| GNU General Public License for more details.                              |
#|                                                                           |
#| You should have received a copy of the GNU General Public License         |
#| along with this program. If not, see <http://www.gnu.org/licenses/>.      |
#+---------------------------------------------------------------------------+
#| @url      : http://www.netzob.org                                         |
#| @contact  : contact@netzob.org                                            |
#| @sponsors : Amossys, http://www.amossys.fr                                |
#|             Supélec, http://www.rennes.supelec.fr/ren/rd/cidre/           |
#+---------------------------------------------------------------------------+

#+---------------------------------------------------------------------------+ 
#| Standard library imports
#+---------------------------------------------------------------------------+
import unittest
from netzob.Common.Models.NetworkMessage import NetworkMessage
from netzob.Common.Models.Factories.NetworkMessageFactory import NetworkMessageFactory
import uuid

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+
from xml.etree import ElementTree

#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+

class NetworkMessageTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_saveInXML(self):
        id = str(uuid.uuid4())
        timestamp = 10 
        ipSource = "192.168.0.10"
        ipTarget = "192.168.0.20"
        protocol = "TCP"
        l4SourcePort = 5799
        l4TargetPort = 80
        strData = "NETwork protocol modeliZatiOn By reverse engineering"
        data = str(bytearray(strData)).encode('hex')
        
        message = NetworkMessage()
        message.setID(id)
        message.setTimestamp(timestamp)
        message.setIPSource(ipSource)
        message.setIPTarget(ipTarget)
        message.setProtocol(protocol)
        message.setL4SourcePort(l4SourcePort)
        message.setL4TargetPort(l4TargetPort)
        message.setData(data)
        
        outputXml = message.getFactory().saveInXML(message)
        
        rootElement2 = ElementTree.XML(outputXml)
        self.message2 = NetworkMessageFactory.loadFromXML(rootElement2)       
        
        self.assertEqual(id, self.message2.getID())
        self.assertEqual(timestamp, self.message2.getTimestamp())
        self.assertEqual(ipSource, self.message2.getIPSource())
        self.assertEqual(ipTarget, self.message2.getIPTarget())
        self.assertEqual(l4SourcePort, self.message2.getL4SourcePort())
        self.assertEqual(l4TargetPort, self.message2.getL4TargetPort())
        self.assertEqual(bytearray(strData.encode('hex')), self.message2.getData())
        
        
    
    def test_loadFromXml(self):        
        id = str(uuid.uuid4()) 
        timestamp = 10 
        ipSource = "192.168.0.10"
        ipTarget = "192.168.0.20"
        protocol = "TCP"
        l4SourcePort = 5799
        l4TargetPort = 80
        strData = "NETwork protocol modeliZatiOn By reverse engineering"
        data = str(bytearray(strData)).encode('hex')
        
        xml = '''
        <message type="network" id="{0}">            
            <timestamp>{1}</timestamp>
            <ipSource>{2}</ipSource>
            <ipTarget>{3}</ipTarget>
            <protocol>{4}</protocol>
            <l4SourcePort>{5}</l4SourcePort>
            <l4TargetPort>{6}</l4TargetPort>
            <data>{7}</data>
        </message>
        '''.format(id, timestamp, ipSource, ipTarget, protocol, l4SourcePort, l4TargetPort, data)
        
        
        rootElement = ElementTree.XML(xml)
        self.message = NetworkMessageFactory.loadFromXML(rootElement)
        
        self.assertEqual(id, self.message.getID())
        self.assertEqual(timestamp, self.message.getTimestamp())
        self.assertEqual(ipSource, self.message.getIPSource())
        self.assertEqual(ipTarget, self.message.getIPTarget())
        self.assertEqual(l4SourcePort, self.message.getL4SourcePort())
        self.assertEqual(l4TargetPort, self.message.getL4TargetPort())
        self.assertEqual(bytearray(strData.encode('hex')), self.message.getData())
        
    
