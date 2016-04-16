from app.models import *
from app.config import string_generator
# from psycopg2 import IntegrityError
# from sqlalchemy.exc import IntegrityError
# from sqlalchemy import update

### Notes ###
# The following code is an example of a way that works to update a db value.
# user = User.query.filter_by(id='9').update(dict(username='newname'))

integrity_error = "* IntegrityError: {} - Exception occurred while trying to add 1+ default sets of values. Perhaps they already exist."
errors = []

# DB creation.
# - Creates DB schema if it does not already exist.
db.create_all()


# App config initialization.
# IMPORTANT! - Post-deployment, you will want to make sure that you change the secret key value in your database.
try:
    db.session.add(Config("App Name", "Just-a-Dash", permission_level=1, active=True))
    db.session.add(Config("App Icon", "glyphicon glyphicon-equalizer", permission_level=1, active=True))
    db.session.add(Config("App Title", "Just-a-Dash Enterprise Management System", permission_level=1, active=True))
    db.session.add(Config("App Short-Title", "Just-a-Dash", permission_level=1, active=True))
    db.session.add(Config("Secret Key", string_generator(size=24), permission_level=1, active=True))
    # db.session.add(Config("Secret Key", "\xa7\x16\x9b\x87\x80\x1aU&\x13Q\x1fL\xe7\xe1\x02\xb1", permission_level=1, active=True))
    db.session.commit()
except:
    errors.append(integrity_error.format("Config"))
    db.session.rollback()


# Module registry initialization.
# - By default, Just-a-Dash comes with the following pre-built modules: Operations, Customer Relations, Human Resources, Accounting, Marketing
try:
    db.session.add(Modules("Admin Control Panel", "App", description="Administrative control panel.", active=True))
    db.session.add(Modules("Operations", "OMS", description="Operations management system.", active=True))
    db.session.add(Modules("Customer Relations", "CRM", description="Customer relationship management system.", active=True))
    db.session.add(Modules("Human Resources", "HRM", description="Human resource management system.", active=True))
    db.session.add(Modules("Accounting", "AMS", description="Accounting management system.", active=True))
    db.session.add(Modules("Marketing", "MMS", description="Marketing management system.", active=True))
    db.session.commit()
except:
    errors.append(integrity_error.format("Modules"))
    db.session.rollback()


# Module config initializations.
# - OMS
try:
    db.session.add(OMS_Config("Module Name", "Operations", permission_level=1, active=True))
    db.session.add(OMS_Config("Module Abbreviation", "OMS", permission_level=1, active=True))
    db.session.add(OMS_Config("Module Icon", "fa fa-fort-awesome", permission_level=1, active=True))
    db.session.add(OMS_Config("Module Title", "Operations Management System", permission_level=1, active=True))
    db.session.add(OMS_Config("Module Short-Title", "Operations Management", permission_level=1, active=True))
    db.session.add(OMS_Config("Twilio Account SID", "", permission_level=1, active=True))
    db.session.add(OMS_Config("Twilio Auth Token", "", permission_level=1, active=True))
    db.session.add(OMS_Config("Twilio Phone Number", "+10000000000", permission_level=1, active=True))
    db.session.commit()
except:
    errors.append(integrity_error.format("Config"))
    db.session.rollback()
# - CRM
try:
    db.session.add(CRM_Config("Module Name", "Customer Relations", permission_level=1, active=True))
    db.session.add(CRM_Config("Module Abbreviation", "CRM", permission_level=1, active=True))
    db.session.add(CRM_Config("Module Icon", "ion-person-stalker", permission_level=1, active=True))
    db.session.add(CRM_Config("Module Title", "Customer Relationship Management System", permission_level=1, active=True))
    db.session.add(CRM_Config("Module Short-Title", "Customer Relations Management", permission_level=1, active=True))
    db.session.commit()
except:
    errors.append(integrity_error.format("Config"))
    db.session.rollback()
# - HRM
try:
    db.session.add(HRM_Config("Module Name", "Human Resources", permission_level=1, active=True))
    db.session.add(HRM_Config("Module Abbreviation", "HRM", permission_level=1, active=True))
    db.session.add(HRM_Config("Module Icon", "fa fa-users", permission_level=1, active=True))
    db.session.add(HRM_Config("Module Title", "Human Resource Management System", permission_level=1, active=True))
    db.session.add(HRM_Config("Module Short-Title", "Human Resources Management", permission_level=1, active=True))
    db.session.commit()
except:
    errors.append(integrity_error.format("Config"))
    db.session.rollback()
# - AMS
try:
    db.session.add(AMS_Config("Module Name", "Accounting", permission_level=1, active=True))
    db.session.add(AMS_Config("Module Abbreviation", "AMS", permission_level=1, active=True))
    db.session.add(AMS_Config("Module Icon", "fa fa-bar-chart", permission_level=1, active=True))
    db.session.add(AMS_Config("Module Title", "Accounting Management System", permission_level=1, active=True))
    db.session.add(AMS_Config("Module Short-Title", "Accounting Management", permission_level=1, active=True))
    db.session.commit()
except:
    errors.append(integrity_error.format("Config"))
    db.session.rollback()
# - MMS
try:
    db.session.add(MMS_Config("App Name", "Marketing", permission_level=1, active=True))
    db.session.add(MMS_Config("Module Abbreviation", "MMS", permission_level=1, active=True))
    db.session.add(MMS_Config("App Icon", "fa fa-line-chart", permission_level=1, active=True))
    db.session.add(MMS_Config("App Title", "Marketing Management System", permission_level=1, active=True))
    db.session.add(MMS_Config("App Short-Title", "Marketing Management", permission_level=1, active=True))

    db.session.commit()
except:
    errors.append(integrity_error.format("Config"))
    db.session.rollback()


# Default users initialization.
# - Initalizes the app with a user with master permissions. The app administrator should change the e-mail/password immediately. Also adds a basic admin and a basic user.
# IMPORTANT! - Post-deployment, you will want to make sure that you change these passwords (at least for 'master') in your database.
try:
    db.session.add(User("master", "master@not-a-real-email.com", password="master", admin_role="master", oms_role="super", crm_role="super", hrm_role="super", ams_role="super", mms_role="super"))
    db.session.add(User("super_admin", "super@not-a-real-email.com", password="super_admin", admin_role="super", oms_role="super", crm_role="super", hrm_role="super", ams_role="super", mms_role="super"))
    db.session.add(User("admin", "admin@not-a-real-email.com", password="admin", admin_role="basic", oms_role="basic", crm_role="basic", hrm_role="basic", ams_role="basic", mms_role="basic"))
    db.session.add(User("user", "user@not-a-real-email.com", password="user", admin_role="None", oms_role="None", crm_role="None", hrm_role="None", ams_role="None", mms_role="None"))
    db.session.add(User("demo", "demo@not-a-real-email.com", password="demo", admin_role="basic", oms_role="basic", crm_role="basic", hrm_role="basic", ams_role="basic", mms_role="basic"))
    db.session.add(User("oms_demo", "oms_demo@not-a-real-email.com", password="oms_demo", admin_role="None", oms_role="basic", crm_role="None", hrm_role="None", ams_role="None", mms_role="None"))
    db.session.add(User("crm_demo", "crm_demo@not-a-real-email.com", password="crm_demo", admin_role="None", oms_role="None", crm_role="basic", hrm_role="None", ams_role="None", mms_role="None"))
    db.session.add(User("hrm_demo", "hrm_demo@not-a-real-email.com", password="hrm_demo", admin_role="None", oms_role="None", crm_role="None", hrm_role="basic", ams_role="None", mms_role="None"))
    db.session.add(User("ams_demo", "ams_demo@not-a-real-email.com", password="ams_demo", admin_role="None", oms_role="None", crm_role="None", hrm_role="None", ams_role="basic", mms_role="None"))
    db.session.add(User("mms_demo", "mms_demo@not-a-real-email.com", password="mms_demo", admin_role="None", oms_role="None", crm_role="None", hrm_role="None", ams_role="None", mms_role="basic"))

    # - The below code seemed necessary when using Bcrypt, but am not using Werkzeug Security.
    # for item in db.session:
    #     item.password = item.password.decode("utf-8")

    db.session.commit()
# except IntegrityError as e:
except:
    errors.append(integrity_error.format("Users"))
    db.session.rollback()


# Roles initialization.
# - Initializes the app with admin/group roles.
try:
    db.session.add(Roles("App", "Master", permission_level=0))
    db.session.add(Roles("App", "Super", permission_level=1))
    db.session.add(Roles("App", "Basic", permission_level=2))
    db.session.add(Roles("App", "Custom1", permission_level=777))
    db.session.add(Roles("OMS", "Master", permission_level=0))
    db.session.add(Roles("OMS", "Super", permission_level=1))
    db.session.add(Roles("OMS", "Basic", permission_level=2))
    db.session.add(Roles("OMS", "Custom1", permission_level=777))
    db.session.add(Roles("CRM", "Master", permission_level=0))
    db.session.add(Roles("CRM", "Super", permission_level=1))
    db.session.add(Roles("CRM", "Basic", permission_level=2))
    db.session.add(Roles("CRM", "Custom1", permission_level=777))
    db.session.add(Roles("HRM", "Master", permission_level=0))
    db.session.add(Roles("HRM", "Super", permission_level=1))
    db.session.add(Roles("HRM", "Basic", permission_level=2))
    db.session.add(Roles("HRM", "Custom1", permission_level=777))
    db.session.add(Roles("AMS", "Master", permission_level=0))
    db.session.add(Roles("AMS", "Super", permission_level=1))
    db.session.add(Roles("AMS", "Basic", permission_level=2))
    db.session.add(Roles("AMS", "Custom1", permission_level=777))
    db.session.add(Roles("MMS", "Master", permission_level=0))
    db.session.add(Roles("MMS", "Super", permission_level=1))
    db.session.add(Roles("MMS", "Basic", permission_level=2))
    db.session.add(Roles("MMS", "Custom1", permission_level=777))
    db.session.commit()
except:
    errors.append(integrity_error.format("Roles"))
    db.session.rollback()


# Permissions initialization.
# - Initializes the app with admin roles.
# Parameters: role, module, permission, r(read), w(write), u(update), d(delete).
try:
    db.session.add(Permissions("Master", "ACP", "Master_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Super", "ACP", "Super_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Basic", "ACP", "Read_Only", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Read", "ACP", "Can_Read", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Write", "ACP", "Can_Write", r=False, w=True, u=False, d=False))
    db.session.add(Permissions("Update", "ACP", "Can_Update", r=False, w=False, u=True, d=False))
    db.session.add(Permissions("Delete", "ACP", "Can_Delete", r=False, w=False, u=False, d=True))

    db.session.add(Permissions("Master", "OMS", "Master_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Super", "OMS", "Super_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Basic", "OMS", "Read_Only", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Read", "OMS", "Can_Read", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Write", "OMS", "Can_Write", r=False, w=True, u=False, d=False))
    db.session.add(Permissions("Update", "OMS", "Can_Update", r=False, w=False, u=True, d=False))
    db.session.add(Permissions("Delete", "OMS", "Can_Delete", r=False, w=False, u=False, d=True))

    db.session.add(Permissions("Master", "CRM", "Master_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Super", "CRM", "Super_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Basic", "CRM", "Read_Only", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Read", "CRM", "Can_Read", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Write", "CRM", "Can_Write", r=False, w=True, u=False, d=False))
    db.session.add(Permissions("Update", "CRM", "Can_Update", r=False, w=False, u=True, d=False))
    db.session.add(Permissions("Delete", "CRM", "Can_Delete", r=False, w=False, u=False, d=True))

    db.session.add(Permissions("Master", "HRM", "Master_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Super", "HRM", "Super_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Basic", "HRM", "Read_Only", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Read", "HRM", "Can_Read", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Write", "HRM", "Can_Write", r=False, w=True, u=False, d=False))
    db.session.add(Permissions("Update", "HRM", "Can_Update", r=False, w=False, u=True, d=False))
    db.session.add(Permissions("Delete", "HRM", "Can_Delete", r=False, w=False, u=False, d=True))

    db.session.add(Permissions("Master", "AMS", "Master_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Super", "AMS", "Super_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Basic", "AMS", "Read_Only", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Read", "AMS", "Can_Read", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Write", "AMS", "Can_Write", r=False, w=True, u=False, d=False))
    db.session.add(Permissions("Update", "AMS", "Can_Update", r=False, w=False, u=True, d=False))
    db.session.add(Permissions("Delete", "AMS", "Can_Delete", r=False, w=False, u=False, d=True))

    db.session.add(Permissions("Master", "MMS", "Master_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Super", "MMS", "Super_All", r=True, w=True, u=True, d=True))
    db.session.add(Permissions("Basic", "MMS", "Read_Only", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Read", "MMS", "Can_Read", r=True, w=False, u=False, d=False))
    db.session.add(Permissions("Write", "MMS", "Can_Write", r=False, w=True, u=False, d=False))
    db.session.add(Permissions("Update", "MMS", "Can_Update", r=False, w=False, u=True, d=False))
    db.session.add(Permissions("Delete", "MMS", "Can_Delete", r=False, w=False, u=False, d=True))

    db.session.commit()
except:
    errors.append(integrity_error.format("Permissions"))
    db.session.rollback()


# Tutorial messages initialization.
# - Initializes the database creation with a first message to start the user off with an app tutorial.
try:
    # def __init__(self, message_type, subcategory, title, body, author, destinations, delivery_methods):
    db.session.add(AppNotifications(message_type="Notification", subcategory="Tutorial", title="Welcome to Just-a-Dash!",
                            body="Welcome to Just-a-Dash, the minimalist's dashboard application. I hope that you enjoy your experience. To get in touch with me for comment / question / feature request / whatever it may be, feel free to e-mail joeflack4@gmail.com, or check out my blog, joeflack.net. - Joe Flack, Creator of Just-a-Dash",
                            author="Joe Flack", destinations="Group:AllUsers", delivery_methods="WebApp, NativeApps, Email"))
    db.session.commit()
except:
    errors.append(integrity_error.format("App Notifications"))
    db.session.rollback()


# - Summary
print("")
print("# # # Database creation and initialization complete. # # #")
print("")
print("Summary of exceptions: ")
for error in errors:
    print(error)
print("")
