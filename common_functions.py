def __class_attr_to_str__(_class) -> str:
    """
    return class __init__ attributes name and conditions to string

    :param _class: class
    :return: "{class_name} = [{attr}: {attr_data_type}={attr_value}, ...]"
    """
    if type(_class) is type:
        return_value: str = str(_class.__name__) + " = ["
        _class = _class()
    else:
        return_value: str = str(_class.__class__.__name__) + " = ["

    class_dict: dict = _class.__dict__

    for item in class_dict:
        type_of: str = str(type(class_dict[item])).replace("<class ", "").replace(">", "").replace("\'", "")
        if type(class_dict[item]) is str:
            return_value += f'{item}: {type_of}="{class_dict[item]}", '
        else:
            return_value += f'{item}: {type_of}={class_dict[item]}, '

    return return_value[0:len(return_value) - 2] + "]"
