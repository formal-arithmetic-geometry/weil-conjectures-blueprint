+++
kind = "proof"
of = "lemma-schematic-closure-uniqueness--1"
uses = []
+++
The scheme $Z$ is the closed subscheme cut out by the kernel ideal
of $f$. For each affine open $V\subseteq T$, the open $k^{-1}(V)$
is affine, and the map
$$
\Gamma(k^{-1}(V),\mathcal O_Z)\longrightarrow
\Gamma(f^{-1}(V),\mathcal O_X)
$$
is injective: its source is the quotient of
$\Gamma(V,\mathcal O_T)$ by the kernel of the map to the target.
This is `AlgebraicGeometry.Scheme.Hom.toImage_app_injective`.
These affine opens cover $Z$, so the kernel ideal of $j$ vanishes
on an affine cover and therefore vanishes everywhere.

For an immersion $f$, choose the open $W\subseteq T$ in which
$f$ is a closed immersion. The square formed by $j$, $X\to W$,
$k$, and $W\to T$ is cartesian: the ideals of the two closed
subschemes agree on affine opens of $W$. This is
`AlgebraicGeometry.IsImmersion.isPullback_toImage_liftCoborder`.
Thus $j$ is the base change of the open immersion $W\to T$.
