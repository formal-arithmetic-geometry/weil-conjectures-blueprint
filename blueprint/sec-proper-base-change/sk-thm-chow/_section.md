+++
id = "sk-thm-chow"
kind = "section"
title = "Chow"
order = 1051
lean = ["AlgebraicGeometry.ChowModification.nonempty_data", "AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpace"]
uses = ["sk-def-conv"]
+++
*Theorem (sketch).*

Let $Y$ be a noetherian scheme and $f:X\to Y$ a separated morphism of finite
type. There exist a proper surjection $\pi:\widetilde X\to X$ which is an
isomorphism over a dense open subscheme of $X$, and an immersion
$i:\widetilde X\hookrightarrow\Pqn_Y$ into a projective space whose homogeneous
coordinates are indexed by a finite set, with $f\circ\pi=p\circ i$, where
$p:\Pqn_Y\to Y$. If $f$ is proper, $i$ is a closed immersion.

## Proof

Cover $X$ by finitely many affine opens $U_1,\dots,U_m$ all of which
contain the generic points of all irreducible components, so
$U=\bigcap_iU_i$ is dense; embed the $U_i$ in projective spaces,
take the diagonal model $\widetilde X$ (the closure of $U$ in
$\prod_iZ_i$, $Z_i$ the closure of $U_i$ in $\Pm_{Y}$), glue the
projections $p_i:\widetilde X\to Z_i$ into $\pi:\widetilde X\to X$
(they agree on the dense $U$); $\pi$ is proper and surjective. The
Segre composite $\widetilde X\hookrightarrow\prod_i\Pm_{Y} \hookrightarrow\Pqn_Y$ is a closed immersion, because $\widetilde X$
is proper over $Y$ and a proper immersion in the sense of
[sk-def-conv] is closed.
