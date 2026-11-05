+++
id = "definition-local-cohomology"
kind = "definition"
title = "Local cohomology"
order = 204
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.closedSupport", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_fiber"]
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-affines-form-basis", "lemma-inverse-image-coefficient-sheaves", "lemma-local-cohomology-right-adjoint"]
+++
The *local cohomology functor*
$R\underline\Gamma_Z:D(X_{\mathrm{pro}\acute{e}t},\mathcal R)\to D(Z_{\mathrm{pro}\acute{e}t},i^*\mathcal R)$
is

$$
R\underline\Gamma_ZK
=i^*\fib(K\longrightarrow Rj_*j^*K),
$$

where $K\to Rj_*j^*K$ is the unit of $j^*\dashv Rj_*$.
