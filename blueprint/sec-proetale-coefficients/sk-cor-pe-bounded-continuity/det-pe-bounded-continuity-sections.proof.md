+++
kind = "proof"
of = "det-pe-bounded-continuity-sections"
+++
Put $K^\bullet=\varinjlim_iK_i^\bullet$, the termwise colimit of sheaves; it also vanishes
in degrees below $a$. Fix one hypercovering $W_\bullet\to U$ with every $W_r$ affine and
weakly contractible ([det-pe-hypercover-existence]); it does not depend on $i$. By
[det-pe-hypercover-complex], naturally in the complex,
$H^q(U,K_i^\bullet)=H^q\operatorname{Tot}(C_i)$ and $H^q(U,K^\bullet)=
H^q\operatorname{Tot}(C)$, with
$\operatorname{Tot}(C_i)^q=\bigoplus_{0\leq r\leq q-a}K_i^{q-r}(W_r)$ and similarly for $C$.
By [det-pe-sections-limits-colimits], $\varinjlim_iK_i^b(W_r)\to K^b(W_r)$ is an
isomorphism for all $r,b$. Finite direct sums commute with colimits, so
$\varinjlim_i\operatorname{Tot}(C_i)\to\operatorname{Tot}(C)$ is an isomorphism of
complexes (the differentials are induced by the same face maps and differentials).
Filtered colimits of abelian groups are exact, so cohomology commutes with them:
$\varinjlim_iH^q\operatorname{Tot}(C_i)\cong H^q\operatorname{Tot}(C)$. By naturality this
isomorphism is the canonical map of the statement.
