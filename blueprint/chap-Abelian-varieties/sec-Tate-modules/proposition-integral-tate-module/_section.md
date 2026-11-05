+++
id = "proposition-integral-tate-module"
kind = "proposition"
title = "The integral Tate module"
order = 1509
lean = ["AlgebraicGeometry.nonempty_addEquiv_torsionBy", "AlgebraicGeometry.IsAbelianVariety.nonempty_linearEquiv_tateModule", "AlgebraicGeometry.IsAbelianVariety.geometricPointsAddEquiv", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme"]
uses = ["definition-abelian-variety", "lemma-abelian-variety-commutative", "definition-tate-module"]
+++
Let $A$ be an abelian variety of dimension $g$ over $k$, and let $\ell$
be a prime invertible in $k$. There are noncanonical isomorphisms

$$
A[\ell^n](\bar k)\simeq(\mathbf Z/\ell^n)^{2g},\qquad
T_\ell A\simeq\mathbf Z_\ell^{2g}.
$$

The canonical projection induces an isomorphism
$T_\ell A/\ell^nT_\ell A\simeq A[\ell^n](\bar k)$.
The groups $A[\ell^n](\bar k)$, the transition maps and the projections
from $T_\ell A$ are $\operatorname{Gal}(\bar k/k)$-equivariant, and they
do not change when $\bar k$ is replaced by a larger algebraically
closed field.
