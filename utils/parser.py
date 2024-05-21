def json_pars(json_array: dict, result_list: list = None) -> list:
    if result_list is None:
        result_list = []
    if isinstance(json_array, dict):
        for i in json_array.keys():
            array = json_array[i]["buttons"]
            if array: 
                result_list.extend([i for i in array.keys()])
                json_pars(json_array=array, result_list=result_list)
    return result_list

def json_search(json_array: dict, key: str) -> tuple[list, dict]:
    path = []
    for i in json_array.keys():
        if i == key: 
            path.insert(0, i)
            return (path, json_array[i])
        else:
            r = json_search(json_array=json_array[i]["buttons"], key=key)
            if r: 
                r[0].insert(0, i)
                return r
    return None