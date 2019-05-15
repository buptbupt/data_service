def check_create_obj_dict(obj_dict):
    if 'id' in obj_dict:
        raise '不可包含id字段'
