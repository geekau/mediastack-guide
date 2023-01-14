# Welcome to MediaStack.Guide

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commandssesss.

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

```diagram
graph TB
    c1-->a2
    subgraph one
    a1-->a2
    end
    subgraph two
    b1-->b2
    end
    subgraph three
    c1-->c2
    end
```



![Image title](https://dummyimage.com/600x400/eee/aaa){ loading=lazy,align=left }

++ctrl+alt+del++

<figure markdown>
  ![Image title](https://dummyimage.com/600x400/){ width="300" }
  <figcaption>Image caption</figcaption>
</figure>

!!! attention

    This is an Attention field... copy this example

---

!!! important

    This is an Important field... copy this example

---

!!! info

    This is an Info field... copy this example

---