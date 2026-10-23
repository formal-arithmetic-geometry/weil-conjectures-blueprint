+++
id = "thm-weil-grothendieck-lefschetz-trace"
kind = "theorem"
title = "Grothendieck–Lefschetz trace formula"
lean = ["AlgebraicGeometry.WeilComplex.finsum_traceFunction_eq_and_pointCount_eq"]
order = 4124
uses = ["cor-trf-point-counting", "def-trf-frobenius-operators", "def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-global-geometric-frobenius", "def-weil-local-frobenius-trace", "def-weil-ordinary-compact-cohomology", "def-weil-point-counts-zeta", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "prop-weil-proper-compact-coincidence", "det-def-sfb-bounded-constructible", "sk-def-sf-weil-complexes", "sk-thm-sfb-qlbar-two-colimit", "det-thm-tf-uniform-formula-weil", "thm-zl-lefschetz-weil-identity"]
+++
Fix the finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and choose a prime $\ell\neq p$;
write $\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of
$\Ql$, and let $Y_0$ be a
separated finite-type
$k_0$-scheme and put $Y=Y_0\times_{k_0}k$. Let $(K,\phi_K)$ be a
Weil complex with $K\in D^b_c(Y,\Qlb)\subset D(Y_{\mathrm{proét}},\Qlb)$
([det-def-sfb-bounded-constructible], [sk-def-sf-weil-complexes],
[def-weil-weil-sheaf-complex]). Use the
geometric Frobenius convention; the induced
cohomological action $F$ is the
global geometric-Frobenius
action. Use the
local Frobenius operators and the
compact-support cohomology
defined for this complex.
For every integer $n\geq1$ and each point
$x\in Y_0(\mathbf F_{q^n})$, choose a
geometric point
$\bar x\to Y$ over $x$, iterate its local Weil isomorphism $n$ times,
and write $K_{\bar x}= L\bar x^*K$, using the
derived pullback. The trace
identity, with values in $\Qlb$, is

$$
\sum_{x\in Y_0(\mathbf F_{q^n})}\sum_{j\in\mathbf Z}(-1)^j
\Tr\bigl(F_x^{(n)}\mid
\mathcal H^j(K)_{\bar x}\bigr)
=
\sum_{i\in\mathbf Z}(-1)^i\Tr(F^n\mid H_c^i(Y,K)).
$$

If $K$ and $\phi_K$ are obtained by extension of scalars from a Weil
complex $(K_E,\phi_{K_E})$ over a finite extension $E/\Ql$ inside $\Qlb$,
which is always possible by [sk-thm-sfb-qlbar-two-colimit] (3) for $K$ and
(2) for $\phi_K$, both sides are the images under $E\hookrightarrow\Qlb$ of
the corresponding $E$-valued traces for $K_E$.

For $K=(\Qlb)_Y=p_Y^*\Qlb$ with its canonical Weil structure and
proper $Y_0$, the
point-count convention specializes to

$$
\#Y_0(\mathbf F_{q^n})
=\sum_{i\in\mathbf Z}(-1)^i\Tr(F^n\mid H^i(Y,\Qlb)).
$$

Here $F_x^{(n)}$ and $K_{\bar x}$ are the
local Frobenius and stalk
constructions, and $H_c^i$ is
compact-support cohomology of the pro-étale site.
