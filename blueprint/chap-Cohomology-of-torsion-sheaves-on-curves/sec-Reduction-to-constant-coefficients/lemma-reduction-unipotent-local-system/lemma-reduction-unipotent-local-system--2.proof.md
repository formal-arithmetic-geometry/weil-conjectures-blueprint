+++
kind = "proof"
of = "lemma-reduction-unipotent-local-system--2"
order = 1610004
uses = []
+++
The finite étale trace is a $\mathbf F_\ell$-linear morphism
$\operatorname{Tr}:v_*v^*G\to G$ satisfying

$$
\operatorname{Tr}\circ\eta_G=d\,\id_G
$$

by `AlgebraicGeometry.Etale.exists_finiteEtaleModuleTrace_degree`.
Indeed, étale locally the cover is a disjoint union of $d$ copies of
the base, the unit is the diagonal, and the trace adds the entries.
The sum is unchanged by permuting the copies, so these local maps glue.
Since $\ell\nmid d$, the scalar $d$ is nonzero in $\mathbf F_\ell$.
Set $r=d^{-1}\operatorname{Tr}$; linearity and $d^{-1}d=1$ give
$r\circ\eta_G=\id_G$.
