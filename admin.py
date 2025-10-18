# MongoDB Admin Configuration
# This file configures the MongoDB admin system

# Import the MongoDB admin configuration
from mongodb_admin import mongo_admin_dashboard, mongo_admin_user_management, \
    mongo_admin_donation_management, mongo_admin_activity_management, \
    mongo_admin_activity_logs, mongo_admin_delete_donation, mongo_admin_ship_donation, \
    mongo_admin_user_detail, mongo_admin_toggle_user_status, \
    mongo_admin_delete_user, mongo_admin_delete_activity, mongo_admin_export_data

# The MongoDB admin system provides:
# - Direct MongoDB integration
# - Custom views for all MongoDB collections
# - Statistics dashboard
# - Pagination support
# - User management
# - Donation management
# - Activity management

# Access the MongoDB admin at: http://localhost:8000/admin-dashboard/