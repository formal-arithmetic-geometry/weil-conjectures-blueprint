+++
id = "sk-thm-betti"
kind = "theorem"
title = "Betti symmetry and the endpoint factors"
order = 3261
lean = ["AlgebraicGeometry.WeilFunctionalEquation.natDegree_rev", "AlgebraicGeometry.Scheme.weil_conjectures"]
uses = ["sk-def-cohfamily", "sk-def-roots", "sk-prop-rootpurity", "sk-thm-intfactors", "sk-thm-poincare-duality", "sk-thm-rationality"]
tags = ["sketch"]
+++
With $b_i=\deg P_i$ one has, for every $\ell\ne p$,

$$
b_i=\dim_{\Ql}H^{i}(X,\Ql),\qquad b_i=b_{2d-i},\qquad b_0=b_{2d}=1,
$$

and

$$
P_0(T)=1-T,\qquad P_{2d}(T)=1-q^{d}T .
$$

In particular $Z$ has a pole of order $1$ at $T=1$ and, if $d\ge1$, a pole of
order $1$ at $T=q^{-d}$.
