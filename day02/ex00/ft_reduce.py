def ft_reduce(function_to_apply, list_of_inputs):
    first = list_of_inputs[0]
    for i in list_of_inputs[1:]:
        first = function_to_apply(first, i)
    return first
