+++
id = "det-def-sfb-pulled-back-coefficients-ring"
kind = "lemma"
title = "$\\Lambda_X$ is a ring object, functorially and preserving commutativity"
uses = ["det-def-sfb-pulled-back-coefficients-definition", "det-def-sfb-ring-object-transport", "def-sfb-upper-star-from-point"]
lean = ["AlgebraicGeometry.ProEtale.coefficientRing", "CategoryTheory.Functor.mapMon", "AlgebraicGeometry.ProEtale.isCommMonObj_condensedRingObj"]
order = 1131
+++
In the situation of [det-def-sfb-pulled-back-coefficients-definition]:

1. $(\Lambda_X,\mu_X,\eta_X)$ is a ring object of $\Sh(X_{\mathrm{proét}},\Ab)$;
2. for a morphism of ring objects $\varphi\colon\Lambda\to\Lambda'$, $\varphi_X$ is a morphism of ring
   objects, and $\Lambda\mapsto\Lambda_X$, $\varphi\mapsto\varphi_X$ is a functor from ring objects of
   $\Sh(*_{\mathrm{proét}},\Ab)$ to ring objects of $\Sh(X_{\mathrm{proét}},\Ab)$;
3. if $\Lambda$ is commutative, then so is $\Lambda_X$.
