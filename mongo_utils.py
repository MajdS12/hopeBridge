from mongoengine import connect, disconnect
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def connect_to_mongodb():
    """Connect to MongoDB using settings from Django configuration"""
    try:
        # Try using connection string first (for Railway)
        if hasattr(settings, 'MONGODB_URI') and settings.MONGODB_URI:
            connect(host=settings.MONGODB_URI, alias='default')
            logger.info(f"Connected to MongoDB using URI: {settings.MONGODB_URI}")
            return True
        
        # Fallback to individual parameters
        connection_params = {
            'db': settings.MONGODB_DATABASE,
            'host': settings.MONGODB_HOST,
            'port': settings.MONGODB_PORT,
            'alias': 'default'
        }
        
        # Add authentication if credentials are available
        if hasattr(settings, 'MONGODB_USER') and settings.MONGODB_USER:
            connection_params['username'] = settings.MONGODB_USER
        if hasattr(settings, 'MONGODB_PASSWORD') and settings.MONGODB_PASSWORD:
            connection_params['password'] = settings.MONGODB_PASSWORD
            
        connect(**connection_params)
        logger.info(f"Connected to MongoDB: {settings.MONGODB_DATABASE}")
        return True
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        return False

def disconnect_from_mongodb():
    """Disconnect from MongoDB"""
    try:
        disconnect()
        logger.info("Disconnected from MongoDB")
        return True
    except Exception as e:
        logger.error(f"Failed to disconnect from MongoDB: {e}")
        return False

def get_mongodb_connection():
    """Get MongoDB connection status"""
    try:
        from mongoengine import get_connection
        connection = get_connection()
        return connection is not None
    except:
        return False
