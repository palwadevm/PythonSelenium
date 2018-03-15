from datetime import datetime as Time
from Framework.TestProperties.TestProperties import *
"""
*-------------------------------------------------------------------------------------------------------------
* Function Name                 - executeTest
*
* Function Description          - Execution Start for the Pytho Framework
*
* Function Parameters           - NA
*
* Function output               - Na
*
* Created By & Date             - Vaijnath Palwade 03/14/2018
*
* Modification History & Date   - NA
*
*-------------------------------------------------------------------------------------------------------------
"""
def executeTests():
    print("Automation Script Start - " + str(Time.now()))
    testProp = TestProperties("Resources/FrameworkConfig/TestDataConfig.prop")