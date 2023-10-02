from dendropy import Tree, TaxonNamespace


def create_tree(words: list) -> Tree:
    taxon_namespace = TaxonNamespace(list("abcdefghijklmnoprqstuvwyxz"))
    tree = Tree(taxon_namespace=taxon_namespace)

    words = set(words)
    nodes = {}

    for word in words:
        parent = tree.seed_node
        length = len(word)

        for i in range(length, -1, -1):
            root = word[:i]
            if root in nodes:
                parent = nodes[root]
                break

        name = root
        for letter in word[i:]:
            name += letter
            node = parent.new_child()
            node.taxon = taxon_namespace.get_taxon(letter)
            nodes[name] = node

            parent = node

    return tree


def main():
    words = [
        "asdf",
        "adgg",
        "adpg",
        "asdd",
        "asfd",
        "sdaf",
        "sadf",
        "fdsa",
        "sdsaf",
        "dfas",
        "fdsa",
        "asdf",
        "dsaf",
        "sadf",
        "dfsa",
        "sdaf",
        "sfda",
    ]
    tree = create_tree(words)
    print(
        tree.as_ascii_plot(
            show_internal_node_labels=True,
            leaf_spacing_factor=2,
            width=(len(words) + 1) * 3,
        )
    )


if __name__ == "__main__":
    main()
