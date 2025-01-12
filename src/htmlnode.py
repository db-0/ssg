class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        return "".join(list(map(lambda item: f" {item[0]}=\"{item[1]}\"", self.props.items())))

    def __eq__(self, other):
        return (self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)

    def __repr__(self):
        return f"HTMLNode(Tags: {self.tag}, Values: {self.value}, Children: {self.children}, Props: {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag argument")
        if not self.children:
            raise ValueError("ParentNode must have children.")
        html_string = ""
        if self.props:
            html_string += f"<{self.tag}{self.props_to_html()}>"
        else:
            html_string += f"<{self.tag}>"
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"

        return html_string
