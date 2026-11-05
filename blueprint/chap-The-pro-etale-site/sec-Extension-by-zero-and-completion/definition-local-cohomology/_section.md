+++
id = "definition-local-cohomology"
kind = "definition"
title = "Local cohomology"
order = 204
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.closedSupport"]
uses = ["lemma-stability"]
+++
The *local cohomology functor*
$R\underline\Gamma_Z:D(X_{\mathrm{pro}\acute{e}t},\mathcal R)\to D(Z_{\mathrm{pro}\acute{e}t},i^*\mathcal R)$
is the right derived functor of the functor of sections supported on $Z$,

$$
F\longmapsto i^*\ker(F\longrightarrow j_*j^*F),
$$

where $F\to j_*j^*F$ is the unit of $j^*\dashv j_*$.
