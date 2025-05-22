### Node Creation Tools
def text(value, **opts):
    return {"type": "text", "value": value, **opts}


def link(children, url, **opts):
    return {"type": "link", "url": url, "children": children, **opts}


def table(children, **opts):
    return {"type": "table", "children": children, **opts}


def table_cell(children, **opts):
    return {"type": "tableCell", "children": children, **opts}


def table_row(cells, **opts):
    return {"type": "tableRow", "children": cells, **opts}


def span(children, style, **opts):
    return {"type": "span", "children": children, "style": style, **opts}


def definition_list(children, **opts):
    return {"type": "definitionList", "children": children, **opts}


def definition_term(children, **opts):
    return {"type": "definitionTerm", "children": children, **opts}


def definition_description(children, **opts):
    return {"type": "definitionDescription", "children": children, **opts}


def list_(children, ordered=False, spread=False, **opts):
    return {
        "type": "list",
        "ordered": ordered,
        "spread": spread,
        "children": children,
        **opts,
    }


def list_item(children, spread=True, **opts):
    return {"type": "listItem", "spread": spread, "children": children, **opts}


def image(url, **opts):
    return {"type": "image", "url": url, **opts}


def grid(columns, children, **opts):
    return {"type": "grid", "columns": columns, "children": children, **opts}


def div(children, **opts):
    return {"type": "div", "children": children, **opts}


def find_all_by_type(parent: dict, type_: str):
    for node in parent["children"]:
        if node["type"] == type_:
            yield node
        if "children" not in node:
            continue
        yield from find_all_by_type(node, type_)
