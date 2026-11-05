+++
id = "theorem-sp-qbar--1"
kind = "theorem"
title = "The two purity maps with coefficients in $\\overline{\\mathbf Q}_\\ell$"
name_showing = false
order = 790001
aliases = ["bp-r238-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_upperShriekUnitTensorMap_of_smooth", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_smoothPurityMap"]
uses = ["theorem-exceptional-inverse-image", "definition-relative-dualizing-complex", "definition-tate-twists", "definition-trace-map", "proposition-projection-formula-rational-coefficients"]
+++
Let $\ell$ be prime, let $k$ be a field of characteristic $p>0$ with
$p\ne\ell$, and let $f:X\to Y$ be a smooth morphism of separated schemes
of finite type over $k$. Work on the pro-étale sites with coefficients
$\Lambda=\overline{\mathbf Q}_\ell$, and put $\omega_f=f^!\Lambda_Y$ as in
Definition [definition-relative-dualizing-complex].

1. For every $K\in\Dbc(Y,\Lambda)$ the map
   $$
   \mu_{f,K}:f^*K\otimes^{\mathbf L}_{\Lambda_X}\omega_f
   \longrightarrow f^!K
   $$
   is an isomorphism. Here $\mu_{f,K}$ is the adjoint, for
   $Rf_!\dashv f^!$, of the composite
   $$
   Rf_!\bigl(f^*K\otimes^{\mathbf L}_{\Lambda_X}\omega_f\bigr)
   \simeq Rf_!\omega_f\otimes^{\mathbf L}_{\Lambda_Y}K
   \xrightarrow{\ \varepsilon_f(\Lambda_Y)\otimes\id\ }K,
   $$
   using tensor symmetry, the projection formula and the tensor unit
   isomorphism. This is `upperShriekUnitTensorMap`.
2. If $f$ has pure relative dimension $d\in\mathbf N$, the adjoint
   $$
   \theta_f:\Lambda_X(d)[2d]\longrightarrow f^!\Lambda_Y
   $$
   of the chosen smooth trace
   $\operatorname{Tr}^{\mathrm{sm}}_f:Rf_!\Lambda_X(d)[2d]\to\Lambda_Y$
   is an isomorphism. Here the trace is `smoothTrace`, the composite of
   $Rf_!$ of the chosen orientation `smoothOrientation` with the counit,
   and $\theta_f$ is `smoothPurityMap`.
