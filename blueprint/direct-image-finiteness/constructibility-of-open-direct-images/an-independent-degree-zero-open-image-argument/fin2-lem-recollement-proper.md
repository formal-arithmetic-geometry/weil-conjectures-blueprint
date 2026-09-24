+++
id = "fin2-lem-recollement-proper"
kind = "lemma"
title = "The recollement sequence and the direct images"
order = 3216
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-geometric-stalks", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-geometric-stalk-conservative", "thm-constructible-serre"]
+++
Let $p:Y\to T$ be a morphism of schemes of finite type over $k$, let
$j:U\hookrightarrow Y$ be a
open immersion with closed
complement $i:Z\hookrightarrow Y$, and let $G$ be a $\Lambda$-sheaf on
$U_{{\mathrm{et}}}$ (all sheaves on mixed schemes being extended by
zero and pulled back by [def-weil-pbc-extension-by-zero] and
[def-weil-pbc-inverse-image]). The recollement sequence on
$Y_{{\mathrm{et}}}$

$$
0\longrightarrow j_!G\longrightarrow j_*G\longrightarrow
i_*i^*j_*G\longrightarrow0
$$

is exact, and for every $q\geq0$ the induced segment of the long exact
sequence of the higher direct images of [def-weil-pbc-direct-image]

$$
R^qp_*(j_!G)\longrightarrow R^qp_*j_*G\longrightarrow
R^q(p\circ i)_*(i^*j_*G)\longrightarrow R^{q+1}p_*(j_!G)
$$

is exact: the middle term is an extension of a quotient of
$R^qp_*(j_!G)$ by a submodule of $R^q(p\circ i)_*(i^*j_*G)$.
Consequently, if
$R^qp_*(j_!G)$ and $R^q(p\circ i)_*(i^*j_*G)$ are
constructible for
all $q$ and vanish for $q>2e$, then so is $R^qp_*j_*G$ for all $q$.

## Proof

The recollement sequence is exact on geometric stalks in the sense of
[def-weil-pbc-geometric-stalks]: at a geometric point $\bar y$ of
$U$ the first two maps are the identity of $G$ and the third term
vanishes, while at a geometric point $\bar y$ of $Z$ the first term
vanishes and the last two agree, by the stalk descriptions of
[def-weil-pbc-extension-by-zero] and of the inverse image of
[def-weil-pbc-inverse-image]; the geometric stalk functors are
jointly conservative ([lemma-weil-pbc-geometric-stalk-conservative]).
The long exact sequence of higher direct images of
[def-weil-pbc-direct-image] for the exact sequence gives the
displayed segment (the $R^q(p\circ i)_*$ appearing for the last term,
since $p\circ i$ is the composite). The extension description of the
middle term is the interpretation of exactness of a
three-term segment, and the submodule and quotient of constructible
sheaves are constructible by the weak-Serre closure of
[thm-constructible-serre]; the vanishing $q>2e$ of the
middle term follows from the vanishing of both outer terms at the
same $q$.
