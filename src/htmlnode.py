class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented("not implemented yet")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        props_text = "".join(f" {k}=\"{v}\"" for k, v in self.props.items())
        return props_text
    
    def __eq__(self, other):
        return (self.tag == other.tag) and (self.value == other.value) and (self.children == other.children) and (self.props == other.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("all leaf nodes must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("all parent nodes must have a tag")
        if not self.children:
            raise ValueError("all parent nodes must have children")
        inner_html = ""
        for child in self.children:
            inner_html += child.to_html()
        html = f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
        return html
