+++
kind  = "proof"
of    = "sk-prop-nagata-sketch-comp-category"
uses = ["sk-lem-nagata-sketch-closure", "sk-thm-nagata-compactification"]
+++
For two compactifications take the schematic closure $Z$ of the diagonal
image of $X$ in $\overline X_1\times_S\overline X_2$. The map from $X$ is a
quasi-compact immersion: it is the graph over the open
$X\subseteq\overline X_1$, and the second factor is separated over $S$.
[sk-lem-nagata-sketch-closure] makes $X$ an open subscheme,
scheme-theoretically dense in $Z$. The product is proper over $S$, so $Z$
and its projections are proper.

Over $X\times_S\overline X_2$ the schematic closure is exactly the graph of
$X\to\overline X_2$: that graph is closed and already contains the entire
restriction of the original immersion. Thus the first projection has
inverse image of $X$ equal to $X$ and is the identity there. The second
projection has the same property. Induction gives the finite-family
assertion.

For a map $h:\overline X'\to\overline X$, properness follows by factoring
through its closed graph in $\overline X'\times_S\overline X$. Put
$V=h^{-1}(X)$. The inclusion $X\to V$ is a section of the separated map
$V\to X$ and is therefore closed, as well as open. Since $X$ is
schematically dense in $\overline X'$, it is schematically dense in $V$; a
closed subscheme containing it must be $V$. Hence $V=X$. Uniqueness is
[sk-lem-nagata-sketch-closure], so parallel morphisms are equal, and the
category is nonempty by Nagata's theorem
([sk-thm-nagata-compactification]).
