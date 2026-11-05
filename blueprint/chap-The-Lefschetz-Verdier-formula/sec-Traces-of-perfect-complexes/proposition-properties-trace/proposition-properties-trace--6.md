+++
id = "proposition-properties-trace--6"
kind = "proposition"
title = "Cohomological trace"
order = 895007
aliases = ["bp-r270-6"]
lean = ["DerivedCategory.trace_eq_singleFunctor_map_superTrace", "AlgebraicGeometry.ProEtale.CondensedRing.trace_eq_homologyUnitEndRingHom_superTrace"]
uses = ["definition-categorical-trace"]
+++
Let $\mathcal A$ be a braided monoidal closed Grothendieck abelian
category with tensor product additive in each variable, functorial flat
resolutions and a derived category. Use the Koszul braiding on
$D(\mathcal A)$. Suppose $P$ has a right dual, is a finite direct sum
of shifts of the unit, and every $H^i(P)$ is dualizable. For $v:P\to P$,

$$
\operatorname{tr}(v\mid P)
=\iota\left(\sum_i(-1)^i\operatorname{tr}(H^i(v)\mid H^i(P))\right),
$$

where $\iota:\End(\mathbf 1_{\mathcal A})\to
\End(\mathbf 1_{D(\mathcal A)})$ places an endomorphism of the unit
in degree zero. The sum is finite.

In particular, let $\ell$ be prime and let $\Omega$ be separably closed
of characteristic $p>0$, with $p\ne\ell$. If
$P\in\Dbc(\operatorname{Spec}\Omega,\Qbarl)$ has a right dual, then
the same formula holds for an endomorphism $v$ of $P$, with $H^i(P)$
its cohomology sheaves and $\iota$ the map from endomorphisms of the
unit sheaf to endomorphisms of the unit of $\Dbc$. The finite
decomposition into shifted units and dualizability of these cohomology
sheaves are conclusions in this case.
