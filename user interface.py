# Creating customer data
# Import system module
import arcpy

arcpy.ImportToolbox(
    "C:\Program Files (x64)\ArcGIS\Desktop10.3\Business Analyst\ArcToolbox\Toolboxes\Business Analyst Tools.tbx")

try:
    # Acquire extension license
    arcpy.CheckOutExtension("Business")

    # Defines the parameters for the Setup Customers
    Input = 'C:/ArcGIS/Business Analyst/Ireland_2021/Datasets/sf_custs.dbf'
    OutFC = "C:/temp/sf_customers.shp"
    Locator = "C:/ArcGIS/Business Analyst/Ireland_2021/Data/customer Data/A & E automobile.loc"
    CustName = "NAME"
    companyId = "COMPANY_ID"
    FldCol = "Addr ADDRESS VISIBLE;City City VISIBLE;State State VISIBLE;ZIP ZIP VISIBLE"

    # Generate customer layers with data
    arcpy.SetupCustomersByTable_ba(Input, Locator, FldCol, CustName, StoreId, OutFC)

    # Release extension license
    arcpy.CheckInExtension("Business")

except:
    print
    arcpy.GetMessages(2)
