+++
kind = "proof"
of = "proposition-dense-compactifications-form-cofiltered-category"
order = 1411
uses = ["lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
A common refinement of two compactifications is the closure of $X$ in
their fibre product, as in the example of $\mathbf A^2$ above. The
properties of morphisms follow from density. A morphism is determined
by its restriction to the dense open $X$. Moreover, $X$ is closed in its
inverse image, being a section of a separated map, and it is dense
there; hence it is the whole inverse image.

Given two compactifications, let $Z$ be the schematic closure of the
image of $X$ in $\overline X_1\times_S\overline X_2$ under the diagonal map.
The map from $X$ is a quasi-compact immersion, because over the open
$X\subseteq\overline X_1$ it is the graph of a morphism to $\overline X_2$, and $\overline X_2$ is
separated over $S$. By Lemma [lemma-schematic-closure-uniqueness], $X$ is an open
subscheme of $Z$ and is scheme-theoretically dense in $Z$. Since the
product is proper over $S$, the scheme $Z$ and its projections are proper.

The projections are refinements, that is, $X$ is its own inverse image
in $Z$. By Lemma [lemma-schematic-closure-uniqueness] the
formation of the schematic closure commutes with restriction to opens.
Over $X\subseteq\overline X_1$ we may therefore compute it on the open
$X\times_S\overline X_2$. There the closure is exactly the graph of
$X\to\overline X_2$, since this graph is closed and is the whole
restriction of the immersion. This means that the inverse image of $X$
under the first projection is $X$, on which the first projection is the
identity. The same holds for the second projection. The assertion
for finite families follows by induction.

Let $h:\overline X'\to\overline X$ be a
morphism of dense compactifications restricting to the identity on
$X$. To see that $h$ is proper, note that it factors through its graph.
The graph is closed in $\overline X'\times_S\overline X$ because
$\overline X$ is separated over $S$. The projection of this product to
$\overline X$ is proper because $\overline X'$ is proper over $S$.

Next, the inclusion $X\to h^{-1}(X)$ is a section of the separated map
$h^{-1}(X)\to X$. It is therefore closed, as well as open. Since $X$ is
schematically dense in $\overline X'$, it is schematically dense in the
open $h^{-1}(X)$. A closed subscheme containing it must be all of
$h^{-1}(X)$, and we conclude that $h^{-1}(X)=X$. Two parallel morphisms
are equal by Lemma [lemma-uniqueness-maps-dense-open]. Finally, the
category is nonempty by Nagata's theorem. With the existence of common
refinements, this shows that it is cofiltered.
