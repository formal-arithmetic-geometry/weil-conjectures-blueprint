+++
id = "proposition-integral-tate-module"
kind = "proposition"
title = "The integral Tate module"
order = 1512
lean = ["AlgebraicGeometry.IsAbelianVariety.nonempty_addEquiv_torsionBy_points"]
uses = ["definition-abelian-variety", "lemma-abelian-variety-commutative", "definition-tate-module"]
+++
Let $A$ be an [abelian variety](@definition-abelian-variety) of dimension $g$ over $k$, and let $\ell$
be a prime invertible in $k$. There are noncanonical isomorphisms

$$
\href{@definition-abelian-variety}{A[\ell^n](\bar k)}\simeq(\mathbf Z/\ell^n)^{2g},\qquad
\href{@definition-tate-module}{T_\ell A}\simeq\mathbf Z_\ell^{2g}.
$$

The canonical projection induces an isomorphism
$\href{@definition-tate-module}{T_\ell A}/\ell^n\href{@definition-tate-module}{T_\ell A}\simeq \href{@definition-abelian-variety}{A[\ell^n](\bar k)}$.
The groups [$A[\ell^n](\bar k)$](@definition-abelian-variety), the transition maps and the projections
from [$T_\ell A$](@definition-tate-module) are $\operatorname{Gal}(\bar k/k)$-equivariant, and they
do not change when $\bar k$ is replaced by a larger algebraically
closed field.
