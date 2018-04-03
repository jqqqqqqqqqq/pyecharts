class Line(object):

    def __init__(
        self,
        width,
        opacity,
        curve,
        line_type,
        color,
        chart_type=None,
        chart_instance=None,
    ):
        if color is None and chart_type == 'graph':
            color = '#aaa'
        self.config = {
            "width": width,
            "opacity": opacity,
            "curveness": curve,
            "type": line_type,
            "color": color,
        }
