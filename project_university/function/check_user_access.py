def check_user_access(db_collection, username, password=None, role=None):

    # 1. جلب المستخدم من الداتابيز
    user = db_collection.find_one({"username": username})
    if not user:
        return "User not found"
    
    # 2. التحقق من كلمة السر إذا تم تمريرها
    if password is not None:
        if user.get("password") == password:
            return "Authenticated successfully"
        return "Invalid password"
        
    # 3. التحقق من الدور/الصلاحية إذا تم تمريرها
    elif role is not None:
        if user.get("role") == role:
            return f"Authorized as {role}"
        return "Role mismatch"
        
    return "Missing password or role"