+++
kind = "proof"
of = "det-thm-restriction-glue"
+++
(1) *Boundedness.* Cohomology sheaves are computed locally, so
$\mathcal H^q(M)$ vanishes as soon as all $\mathcal H^q(M|_{U_\alpha})$ do;
hence $M$ has cohomology in the union of the finitely many bounded intervals
of the $M|_{U_\alpha}$. *Constructibility.* For each $\alpha$ choose a finite
partition of $U_\alpha$ into locally closed subsets on which all cohomology
sheaves of $M|_{U_\alpha}$ are lisse. Each piece is locally closed in $X$,
and together with the complements $X\smallsetminus U_\alpha$ these give finitely
many finite partitions of $X$ into locally closed subsets. Their common
refinement is a finite partition of $X$ into locally closed subsets, each
contained in some piece of each partition; on a piece $S$ contained in
$U_\alpha$, the restriction of $\mathcal H^q(M)$ is the restriction of a lisse
sheaf from a piece of the partition of $U_\alpha$, hence lisse. Each piece
$S$ of the refinement is contained in $U_\alpha$ or in
$X\smallsetminus U_\alpha$ for every $\alpha$, and since the $U_\alpha$ cover
$X$, it is contained in at least one $U_\alpha$.
Thus all cohomology sheaves of $M$ are lisse on the strata, and
$M\in\Dbc(X,\Lambda)$.

(2) By [det-thm-restriction-local], $X$ has a finite cover by affine opens
$u:U\hookrightarrow X$ with $u^*f^!K\in\Dbc(U,\Lambda)$; by (1),
$f^!K\in\Dbc(X,\Lambda)$. By [sk-prop-sf-comp-coherence], $Rf_!A\in\Dbc(Y,\Lambda)$
for $A\in\Dbc(X,\Lambda)$. The bijection
$\Hom(Rf_!A,K)\simeq\Hom(A,f^!K)$ of [sk-prop-sf-existence] is between Hom
groups in $\Loc(\Dbc(-,\Lambda))$, and since the inclusions
$\Dbc(-,\Lambda)\subset\Loc(\Dbc(-,\Lambda))$ are full, these are the Hom
groups in $\Dbc(Y,\Lambda)$ and $\Dbc(X,\Lambda)$. Naturality in $A$ and $K$
is inherited, so the restrictions of $Rf_!$ and $f^!$ are adjoint.
