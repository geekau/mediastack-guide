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

``` mermaid
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

!!! danger

    === "C"

        ``` c
        #include <stdio.h>

        int main(void) {
        printf("Hello world!\n");
        return 0;
        }
        ```

    === "C++"

        ``` c++
        #include <iostream>

        int main(void) {
        std::cout << "Hello world!" << std::endl;
        return 0;
        }
        ```



![Image title](https://dummyimage.com/600x400/eee/aaa){ loading=lazy,align=left }

++ctrl+alt+del++

<figure markdown>
  ![Image title](https://dummyimage.com/600x400/){ width="300" }
  <figcaption>Image caption</figcaption>
</figure>

!!! note

    This is a Note field... copy this example

---

!!! abstract

    This is an Abstract field... copy this example

---

!!! info

    This is an Info field... copy this example

    === "Linux Shell"

    ``` shell
    This is linux code
    ```
    === "Windows Prompt"

    ``` powershell
    This is linux code
    ```

    === "Synology SSH"

    ``` putty
    This is linux code
    ```

---

!!! tip

    This is a Tip field... copy this example

---

!!! success

    This is a Success field... copy this example

---

!!! question

    This is a Question field... copy this example

---

!!! warning

    This is a Warning field... copy this example

---

!!! failure

    This is a Failure field... copy this example

---

!!! danger

    This is a Danger field... copy this example

---

!!! bug

    This is a Bug field... copy this example

---

!!! example

    This is an Example field... copy this example

---

!!! quote

    This is a Quote field... copy this example

---


