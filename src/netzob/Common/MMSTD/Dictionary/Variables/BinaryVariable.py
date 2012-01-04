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
import logging
from lxml.etree import ElementTree
from lxml import etree

#+---------------------------------------------------------------------------+
#| Related third party imports
#+---------------------------------------------------------------------------+


#+---------------------------------------------------------------------------+
#| Local application imports
#+---------------------------------------------------------------------------+
from netzob.Common.MMSTD.Dictionary.Variable import Variable
from netzob.Common.TypeConvertor import TypeConvertor



#+---------------------------------------------------------------------------+
#| BinaryVarible :
#|     Definition of a binary variable
#+---------------------------------------------------------------------------+
class BinaryVariable(Variable):
    
    def __init__(self, id, name, mutable, value):
        Variable.__init__(self, "Binary", id, name, mutable)
        self.log = logging.getLogger('netzob.Common.MMSTD.Dictionary.Variables.BinaryVariable.py')
        
        
        if value == "" or value == None :
            self.binVal = None
            self.strVal = None
        else :
            self.strVal = str(value)
            self.binVal = value
            
    def getDescription(self):
        if self.isMutable() :
            mut = "[M]"
        else :
            mut = "[!M]"
        return "BinaryVariable " + mut + " (" + self.strVal + ")"
      
    def save(self, root, namespace):
        xmlVariable = etree.SubElement(root, "{" + namespace + "}variable")
        # Header specific to the definition of a variable
        xmlVariable.set("id", str(self.getID()))
        xmlVariable.set("name", str(self.getName()))
        xmlVariable.set("mutable", TypeConvertor.bool2str(self.isMutable()))
        xmlVariable.set("{http://www.w3.org/2001/XMLSchema-instance}type", "netzob:BinaryVariable")
        
        # Definition of a word variable
        xmlWordVariableValue = etree.SubElement(xmlVariable, "{" + namespace + "}value")
        xmlWordVariableValue.text = str(TypeConvertor.binaryToNetzobRaw(self.binVal))
        
    
