+++
id = "thm-trf-trace-formula-e"
kind = "theorem"
title = "Trace formula over a finite extension"
order = 2527
uses = ["def-trf-adic-system", "def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-weil-finite-field-fiber", "def-weil-pbc-rational-category", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "prop-trf-trace-formal-laws", "thm-trf-integral-adic-trace-formula"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and the
coefficient conventions,
let $X_0$ be
separated finite-type
over $k_0$, put $X=X_0\times_{k_0}k$, and let
$K_E\in D^b_c(X,E)$ be in the
rationalized
$E$-coefficient category, presented by a
normalized integral system $K_\bullet$
with $\mathcal O_E$-realization a lattice for $K_E$. Assume that
this system satisfies the hypotheses and pending trace inputs of
[thm-trf-integral-adic-trace-formula]; in particular its finite
levels carry explicit etale-origin witnesses. Then for every $m\geq1$,

$$
\sum_{i\in\mathbf Z}(-1)^i
\operatorname{Tr}\bigl(F_{c,K_E}^m\mid H_c^i(X,K_E)\bigr)
=
\sum_{y\in X_0(\mathbf F_{q^m})}
\sum_{j\in\mathbf Z}(-1)^j
\operatorname{Tr}\bigl(F_{y,m}\mid H^j(K_{E,\bar y})\bigr),
$$

in $E$: both sides are the scalar extensions of, respectively, the
image in $E$ of the integral identity of
[thm-trf-integral-adic-trace-formula] and its local part, under
$\mathcal O_E\to E$, and both sides agree with the
categorical traces by the
supertrace law over the field $E$ of
[prop-trf-trace-formal-laws].

## Proof

By [thm-trf-integral-adic-trace-formula], the identity

$$
\operatorname{tr}_{\mathcal O_E}
\bigl(F_{c}^m\mid R\Gamma_c(X,K_{\mathcal O_E})\bigr)
=
\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\mathcal O_E}
\bigl(F_{y,m}\mid K_{\mathcal O_E,\bar y}\bigr)
$$

holds in $\mathcal O_E$. Applying the localization
$\mathcal O_E\to E$ and using the scalar-extension law of the
categorical trace for $\rho:\mathcal O_E\to E$ of
[prop-trf-trace-formal-laws] on both sides gives the identity of
the $E$-valued categorical traces of the realized endomorphisms of
$R\Gamma_c(X,K_E)$ and of the stalks; and by the supertrace law over
the field $E$ of [prop-trf-trace-formal-laws], each categorical
trace is the alternating sum of the traces on cohomology, which is the
displayed identity.
