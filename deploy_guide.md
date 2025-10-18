# Railway Deployment Guide for HopeBridge

## Prerequisites
1. Railway account (https://railway.app)
2. PostgreSQL database (Railway provides this)
3. MongoDB Atlas account (for MongoDB)
4. Google OAuth credentials

## Environment Variables Setup

### Required Environment Variables in Railway:

```bash
# Django Settings
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.railway.app,localhost,127.0.0.1

# Database Settings (Railway will provide these)
DB_NAME=railway
DB_USER=postgres
DB_PASSWORD=your-railway-db-password
DB_HOST=your-railway-db-host
DB_PORT=5432

# MongoDB Settings (MongoDB Atlas)
MONGODB_DATABASE=donation_management_db
MONGODB_HOST=your-mongodb-atlas-cluster.mongodb.net
MONGODB_PORT=27017

# Email Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=HopeBridge <your-email@gmail.com>
ADMIN_CONTACT_EMAIL=your-email@gmail.com

# Google OAuth Settings
GOOGLE_OAUTH2_CLIENT_ID=your-google-client-id
GOOGLE_OAUTH2_CLIENT_SECRET=your-google-client-secret

# Security Settings
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_BROWSER_XSS_FILTER=True
X_FRAME_OPTIONS=DENY
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True

# Django Settings Module
DJANGO_SETTINGS_MODULE=settings_production
```

## Deployment Steps

### 1. Prepare Your Repository
```bash
# Make sure all files are committed
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 2. Deploy to Railway
1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub repo"
4. Choose your repository
5. Railway will automatically detect it's a Django project

### 3. Add PostgreSQL Database
1. In your Railway project dashboard
2. Click "New" → "Database" → "PostgreSQL"
3. Railway will automatically set the database environment variables

### 4. Set Environment Variables
1. Go to your service settings
2. Click "Variables" tab
3. Add all the environment variables listed above

### 5. Configure MongoDB Atlas
1. Create a MongoDB Atlas account
2. Create a new cluster
3. Get your connection string
4. Update MONGODB_HOST with your Atlas cluster URL

### 6. Configure Google OAuth
1. Go to Google Cloud Console
2. Create OAuth 2.0 credentials
3. Add your Railway domain to authorized origins
4. Set the redirect URI to: `https://your-app.railway.app/accounts/google/login/callback/`

### 7. Deploy
Railway will automatically build and deploy your application. The build process will:
- Install Python dependencies
- Run database migrations
- Collect static files
- Start the application with Gunicorn

## Post-Deployment

### 1. Create Superuser
```bash
# Connect to your Railway service terminal
railway run python manage.py createsuperuser --settings=settings_production
```

### 2. Verify Deployment
- Check your app URL
- Test user registration
- Test Google OAuth login
- Verify all functionality

## Security Checklist
- ✅ Secret keys moved to environment variables
- ✅ DEBUG=False in production
- ✅ ALLOWED_HOSTS properly configured
- ✅ SSL/HTTPS enabled
- ✅ Security headers configured
- ✅ Database credentials secured
- ✅ Email credentials secured
- ✅ OAuth credentials secured

## Monitoring
- Check Railway logs for any errors
- Monitor database connections
- Set up error tracking (optional)

## Troubleshooting
- Check Railway logs if deployment fails
- Verify all environment variables are set
- Ensure database is accessible
- Check MongoDB Atlas connection
- Verify Google OAuth configuration
