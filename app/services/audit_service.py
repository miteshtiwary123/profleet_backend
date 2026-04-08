from app.models.audit_log import AuditLog

def log_action(db, user_id, action, target_user_id=None):
    log = AuditLog(
        user_id=user_id,
        action=action,
        target_user_id=target_user_id
    )
    db.add(log)
    db.commit()
    