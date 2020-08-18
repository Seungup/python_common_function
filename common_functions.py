def __class_attr_to_str__(_class: object) -> str:
    """
    return class __init__ attributes and conditions to string

    :param _class: object
    :return: {class_name} = [{attr}: {attr_data_type}={attr_value}, ...]
    """
    return_value: str = str(_class.__class__.__name__) + " = ["

    class_dict: dict = _class.__dict__

    for item in class_dict:
        attr_name = item
        attr_type = type(class_dict[item]).__name__
        attr_value = '"' + class_dict[item] + '"' if type(class_dict[item]) is str else class_dict[item]
        return_value += f'{attr_name}: {attr_type}={attr_value}, '

    return return_value[0:len(return_value) - 2] + "]"
