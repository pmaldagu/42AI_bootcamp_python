def ft_filter(function_to_apply, list_of_inputs):
    lst_result = []
    for x in list_of_inputs:
        if function_to_apply(x) is True:
            lst_result.append(x)
    return lst_result
