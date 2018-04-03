import types


class AxisLabel:

    def __init__(
        self,
        interval,
        rotate,
        margin,
        text_size,
        text_color,
        formatter,
        chart_instance=None,
    ):
        self.config = {
            "interval": interval,
            "formatter": formatter,
            "rotate": rotate,
            "margin": margin,
            "formatter": formatter,
            "textStyle": {"fontSize": text_size, "color": text_color},
        }


class XAxisLabel(AxisLabel):

    def __init__(
        self,
        interval,
        rotate,
        margin,
        text_size,
        text_color,
        formatter,
        chart_instance=None,
    ):
        if isinstance(formatter, types.FunctionType):
            formatter = chart_instance._add_a_python_function(formatter)
        super(XAxisLabel, self).__init__(
            interval,
            rotate,
            margin,
            text_size,
            text_color,
            formatter,
            chart_instance,
        )


class YAxisLabel(AxisLabel):

    def __init__(
        self,
        interval,
        rotate,
        margin,
        text_size,
        text_color,
        formatter,
        chart_instance=None,
    ):
        if isinstance(formatter, types.FunctionType):
            formatter = chart_instance._add_a_python_function(formatter)
        else:
            formatter = "{value} " + formatter
        super(YAxisLabel, self).__init__(
            interval,
            rotate,
            margin,
            text_size,
            text_color,
            formatter,
            chart_instance,
        )


class Axis(object):

    def __init__(
        self,
        name,
        visibility,
        name_location,
        name_gap,
        name_size,
        position,
        boundary_gap,
        label_alignment,
        inverse,
        split_line=False,
        value_range=None,
        axis_type=None,
        chart_type=None,
        chart_instance=None,
    ):
        if axis_type is None:
            axis_type = "value" if chart_type == "scatter" else "category"
        self.config = {
            "name": name,
            "show": visibility,
            "nameLocation": name_location,
            "nameGap": name_gap,
            "nameTextStyle": {"fontSize": name_size},
            "axisTick": {"alignWithLabel": label_alignment},
            "inverse": inverse,
            "position": position,
            "boundaryGap": boundary_gap,
            "min": value_range[0],
            "max": value_range[1],
            "type": axis_type,
            "splitLine": {"show": splitline},
        }


class XAxis(object):

    def __init__(
        self,
        name,
        visibility,
        name_location,
        name_gap,
        name_size,
        position,
        boundary_gap,
        label_alignment,
        inverse,
        split_line=False,
        value_range=None,
        axis_type=None,
        chart_type=None,
        chart_instance=None,
    ):
        if axis_type is None:
            axis_type = "value" if chart_type == "scatter" else "category"

        super(XAxis, self).__init__(
            self,
            name,
            visibility,
            name_location,
            name_gap,
            name_size,
            position,
            boundary_gap,
            label_alignment,
            inverse,
            split_line=False,
            value_range=None,
            axis_type=None,
            chart_type=None,
            chart_instance=None,
        )


class YAxis(object):

    def __init__(
        self,
        name,
        visibility,
        name_location,
        name_gap,
        name_size,
        position,
        boundary_gap,
        label_alignment,
        inverse,
        split_line=False,
        value_range=None,
        axis_type=None,
        chart_type=None,
        chart_instance=None,
    ):
        if axis_type is None:
            axis_type = "value"

        super(YAxis, self).__init__(
            self,
            name,
            visibility,
            name_location,
            name_gap,
            name_size,
            position,
            boundary_gap,
            label_alignment,
            inverse,
            split_line=False,
            value_range=None,
            axis_type=None,
            chart_type=None,
            chart_instance=None,
        )
