# 1º - Import the ibm_db library
import ibm_db

# 2º - Replace with your actual database credentials
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "<database>"            # e.g. "BLUDB"
dsn_hostname = "<hostname>" # e.g.: "awh-yp-small03.services.dal.bluemix.net"
dsn_port = "<port>"                # e.g. "50000" 
dsn_protocol = "<protocol>"            # i.e. "TCPIP"
dsn_uid = "<username>"        # e.g. "dash104434"
dsn_pwd = "<password>"

# 3º - Create database connection
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected!")

except:
    print ("Unable to connect to database") 