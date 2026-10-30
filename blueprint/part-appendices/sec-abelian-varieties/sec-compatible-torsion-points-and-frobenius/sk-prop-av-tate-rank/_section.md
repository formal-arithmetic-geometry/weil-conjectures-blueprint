+++
id = "sk-prop-av-tate-rank"
kind = "proposition"
title = "The integral Tate module"
order = 870
lean = ["AlgebraicGeometry.IsAbelianVariety.natCard_torsionBy_geometricPoints", "AlgebraicGeometry.IsAbelianVariety.nonempty_addEquiv_torsionBy_points", "AlgebraicGeometry.IsAbelianVariety.nonempty_linearEquiv_tateModule_of_natCast_ne_zero", "AlgebraicGeometry.IsAbelianVariety.galoisRepresentation"]
uses = ["sk-def-av", "sk-prop-av-isogeny", "sk-prop-av-mult-n-pullback"]
tags = ["sketch"]
+++
Let $A$ be an abelian variety of dimension $g$ over $k$, and let $\ell$
be a prime invertible in $k$. There are noncanonical isomorphisms

$$
A[\ell^n](\bar k)\simeq(\mathbf Z/\ell^n)^{2g},\qquad
T_\ell A:=\varprojlim_{[\ell]}A[\ell^n](\bar k)
\simeq\Zl^{2g}.
$$

The canonical projection induces an isomorphism
$T_\ell A/\ell^nT_\ell A\simeq A[\ell^n](\bar k)$.
The groups $A[\ell^n](\bar k)$, the transition maps and the projections
from $T_\ell A$ are $\operatorname{Gal}(\bar k/k)$-equivariant, and they
do not change when $\bar k$ is replaced by a larger algebraically
closed field.
