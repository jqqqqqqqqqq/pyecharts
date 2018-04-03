import types


class Label(object):

    def __init__(
        self,
        visibility,
        position,
        text_color,
        text_size,
        formatter=None,
        chart_type=None,
        chart_instance=None,
    ):
        if position is None:
            position = "outside" if chart_type in ["pie", "graph"] else "top"
        self.config = {
            "show": visibility,
            "position": position,
            "textStyle": {"color": text_color, "fontSize": text_size},
        }

        if chart_type != 'graph':
            _tmp_formatter = formatter
            if formatter is None:
                if type == "pie":
                    _tmp_formatter = "{b}: {d}%"
            elif isinstance(formatter, types.FunctionType):
                _tmp_formatter = chart_instance._add_a_python_function(
                    formatter
                )
            self.config['formatter'] = _tmp_formatter
