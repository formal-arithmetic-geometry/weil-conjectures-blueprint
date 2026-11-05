+++
id = "corollary-contracting-local-terms-point"
kind = "corollary"
title = "Contracting local terms at a point"
order = 1710
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_of_isContractingAt", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_ofGraph_eq_trace_of_isContractingAt"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-proper-direct-image-unbounded-complexes", "definition-correspondence", "definition-frobenius-correspondences-their-operators"]
+++
Let $y\in X(k)$, and suppose that $c_1^{-1}(y)$ is a single reduced point
$z$, with $c_2(z)=y$. Suppose that $F_0=\{z\}$ is an isolated reduced
component of $\Fix(c)$, open and closed, and that on a neighbourhood of $F_0$
the ideal $I_y$ satisfies

$$
c_2^{-1}(I_y)\mathcal O_C\subset c_1^{-1}(I_y)\mathcal O_C,
\qquad
\bigl(c_2^{-1}(I_y)\mathcal O_C\bigr)^n
\subset\bigl(c_1^{-1}(I_y)\mathcal O_C\bigr)^{n+1}
\quad\text{for some }n\geq1.
$$

Then for every $K\in D^b_{\mathrm{ctf}}(X,A)$ and every morphism
$u:c_2^*K\to c_1^!K$, the local term at $F_0$ is the categorical
trace of the restriction $u_Z$ to $Z=\{y\}$ of $u$ restricted to
that neighbourhood, defined in (E.21). In particular, for
$c=(\operatorname{id}_X,h)$,

$$
\operatorname{LT}_y(u)
=\operatorname{tr}_A(u_{\bar y}\mid K_{\bar y}).
$$
