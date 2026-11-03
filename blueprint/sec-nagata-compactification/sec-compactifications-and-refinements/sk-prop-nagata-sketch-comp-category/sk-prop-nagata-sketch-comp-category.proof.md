+++
kind = "proof"
of = "sk-prop-nagata-sketch-comp-category"
uses = ["sk-lem-nagata-sketch-closure", "sk-thm-nagata-compactification"]
+++
Given two compactifications, let $Z$ be the schematic closure of the
image of $X$ in $\overline X_1\times_S\overline X_2$ under the diagonal map.
The map from $X$ is a quasi-compact immersion, because over the open
$X\subseteq\overline X_1$ it is the graph of a morphism to $\overline X_2$, and $\overline X_2$ is
separated over $S$. By Lemma [sk-lem-nagata-sketch-closure], $X$ is an open
subscheme of $Z$ and is scheme-theoretically dense in $Z$. Since the
product is proper over $S$, the scheme $Z$ and its projections are proper.

The schematic closure may be computed on the open
$X\times_S\overline X_2$, since its formation commutes with restriction
to opens (proof of Lemma [sk-lem-nagata-sketch-closure]). There it is exactly
the graph of $X\to\overline X_2$, because this graph is closed and is
the whole restriction of the immersion. Thus the
inverse image of $X$ under the first projection is $X$, and the first
projection is the identity there. The same holds for the second
projection. The assertion for finite families follows by induction.

Let $h:\overline X'\to\overline X$ be a morphism. It is proper, since it
factors through its graph, which is closed in
$\overline X'\times_S\overline X$. The inclusion
$X\to h^{-1}(X)$ is a section of the separated map $h^{-1}(X)\to X$
and is therefore closed, as well as open. Since $X$ is schematically
dense in $\overline X'$, it is schematically dense in the open
$h^{-1}(X)$, and a closed subscheme containing it must be all of
$h^{-1}(X)$. Hence $h^{-1}(X)=X$. By
Lemma [sk-lem-nagata-sketch-closure], two parallel morphisms are equal. Finally,
the category is nonempty by Nagata's theorem, and together with the
existence of common refinements this shows that it is cofiltered.
