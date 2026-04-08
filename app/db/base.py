from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ✅ Import ALL models so Alembic can detect them
from app.models.user import User
from app.models.token_blacklist import TokenBlacklist
from app.models.audit_log import AuditLog