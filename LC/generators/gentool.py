def lc_printf(o):
    print(lc_format(o))


def lc_format(o) -> str:
    if isinstance(o, str):
        return '"' + o + '"'
    elif isinstance(o, list):
        return "[" + ", ".join([lc_format(s) for s in o]) + "]"
    elif isinstance(o, int):
        return str(o)
    else:
        raise ValueError(f"Unsupported type {type(o)}")
