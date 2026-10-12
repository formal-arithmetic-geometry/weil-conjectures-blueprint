+++
id = "def-sfb-finite-extension-by-zero"
kind = "definition"
title = "Extension by zero $j_!$"
order = 1637
uses = ["def-weil-pbc-proetale-site"]
lean = ["AlgebraicGeometry.ProEtale.openImmersionLowerShriek"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and $j\colon U\to X$ an open
immersion. Since $j$ is weakly étale, composition with $j$ is a functor
$\ell\colon U_{\mathrm{proét}}\to X_{\mathrm{proét}}$, $(T\to U)\mapsto(T\to U\to X)$
[def-weil-pbc-proetale-site], the *localization functor*. The *extension by zero* is

$$
j_!\colon\Sh(U_{\mathrm{proét}},\mathcal A)\to\Sh(X_{\mathrm{proét}},\mathcal A),
\qquad j_!F:=\operatorname{sheafify}\bigl(\operatorname{Lan}_{\ell^{\mathrm{op}}}F\bigr).
$$
