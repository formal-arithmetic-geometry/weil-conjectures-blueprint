+++
id = "lem-kun-leray-unbdd"
kind = "lemma"
title = "Unbounded Leray for finite cohomological dimension"
order = 6058
lean = ["AlgebraicGeometry.Etale.RGamma_comp_derivedPushforward_of_finite_cd"]
uses = ["def-weil-pbc-hypercohomology-filtrations", "def-kun-cd", "def-kun-rgamma-unbounded", "lem-kun-leray-bdd"]
+++
Let $f:X\to Y$ be a qcqs morphism of schemes with
$\operatorname{cd}(f)<\infty$ and let $n\ge1$. Then
$$
R\Gamma(X_{\Et},E)\cong R\Gamma\bigl(Y_{\Et},Rf_*E\bigr)
$$
canonically for every $E\in D(X_{\Et},\mathbf Z/n\mathbf Z)$.

## Proof

For $E\in D(X_{\Et},\mathbf Z/n\mathbf Z)$ the Grothendieck spectral sequence
of the composite $\Gamma(Y_{\Et},-)\circ Rf_*$ has
$$
E_2^{p,q}=H^p\bigl(Y_{\Et},R^qf_*E\bigr)\Longrightarrow H^{p+q}(X_{\Et},E),
$$
the abutment being $R\Gamma(X_{\Et},E)$ by [def-kun-rgamma-unbounded].

Since $\operatorname{cd}(f)<\infty$ by hypothesis, $R^qf_*E=0$ for all
$q>d$ with $d=\operatorname{cd}(f)$ ([def-kun-cd]), so the spectral sequence
is confined to the finitely many columns $0\le q\le d$; a half-plane
spectral sequence with finitely many columns converges strongly without any
boundedness hypothesis on $E$, and its edge map in degree $n$ is the
canonical map $H^n(Y_{\Et},Rf_*E)\to H^n(X_{\Et},E)$. For $E$ bounded below
this edge map is an isomorphism by [lem-kun-leray-bdd]; the finiteness of
the columns forces the same for arbitrary $E$, since each abutment is
computed from finitely many columns.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-direct-image, def:weil-pbc-derived-categories
