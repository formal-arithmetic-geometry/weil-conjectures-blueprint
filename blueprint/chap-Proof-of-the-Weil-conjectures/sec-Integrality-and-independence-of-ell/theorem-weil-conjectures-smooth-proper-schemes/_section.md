+++
id = "theorem-weil-conjectures-smooth-proper-schemes"
kind = "theorem"
title = "The Weil conjectures for smooth proper schemes"
order = 1388
lean = ["AlgebraicGeometry.Scheme.weil_conjectures", "AlgebraicGeometry.Scheme.weil_integral_factors", "AlgebraicGeometry.Scheme.riemann_hypothesis", "AlgebraicGeometry.Scheme.weil_betti", "AlgebraicGeometry.Scheme.weil_functional_equation"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-compactification-refinement"]
+++
Let $X_0/\mathbf F_q$ be smooth proper of pure dimension $d$, and let
$P_{i,\ell}$ be as above.

1. There are unique polynomials $P_i(T)\in\mathbf Z[T]$ with $P_i(0)=1$
   whose images in $\mathbf Q_\ell[T]$ are $P_{i,\ell}(T)$ for every prime
   $\ell\nmid q$, and
   $Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}$.
2. The reciprocal roots of $P_i$ are algebraic integers, and each of them
   has absolute value $q^{i/2}$ under every complex embedding.
3. The degrees $b_i=\deg P_i=\dim_{\mathbf Q_\ell}H^i_\ell$ do not depend on $\ell$,
   and $b_i=b_{2d-i}$. If $X_0$ is geometrically connected, then
   $P_0=1-T$, $P_{2d}=1-q^dT$, and $b_0=b_{2d}=1$.
4. Put $\chi=\sum_i(-1)^ib_i$. Then $d\chi$ is even and there
   is $\varepsilon\in\{1,-1\}$ such that
   $$
   Z\!\left(X_0,\frac1{q^dT}\right)
   =\varepsilon q^{d\chi/2}T^\chi Z(X_0,T)
   \quad\hbox{in }\mathbf Q(T).
   $$
