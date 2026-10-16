+++
id = "thm-weil-grothendieck-lefschetz-trace"
kind = "theorem"
title = "Grothendieck–Lefschetz trace formula"
lean = ["AlgebraicGeometry.WeilComplex.finsum_traceFunction_eq_and_pointCount_eq"]
order = 3223
uses = ["cor-trf-point-counting", "def-trf-frobenius-operators", "def-trf-karoubi-trace", "def-weil-algebraically-closed-coefficients", "def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-global-geometric-frobenius", "def-weil-local-frobenius-trace", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-point-counts-zeta", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "prop-trf-karoubi-independence", "prop-weil-proper-compact-coincidence", "thm-trf-frobenius-fixed-points", "thm-trf-frobenius-local-term", "thm-trf-grothendieck-lefschetz-finite-ring", "thm-trf-grothendieck-lefschetz-qbar", "thm-trf-lefschetz-verdier", "thm-trf-trace-formula-e", "thm-zl-lefschetz-weil-identity"]
+++
Fix the finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, and choose a prime $\ell\neq p$;
write $\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of
$\Ql$, and let $Y_0$ be a
separated finite-type
$k_0$-scheme and put $Y=Y_0\times_{k_0}k$. Let
$K\in D^b_{c,\mathrm W}(Y,\Qlb)$ be a
Weil complex; choose a finite
extension $E/\Ql$ contained in $\Qlb$ and a model
$K_E\in D^b_{c,\mathrm W}(Y,E)$ with scalar extension
$K_E\otimes_E\Qlb=K$. These coefficients are formed on the
small pro-etale site, and the
common-stage
coefficient construction supplies the scalar extension. Use the
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
and write $K_{E,\bar x}= L\bar x^*\operatorname{For}(K_E)$, using the
derived pullback. The trace
identity is
understood after mapping the left-hand $E$-valued traces to $\Qlb$ along
the chosen inclusion $E\hookrightarrow\Qlb$, and is explicitly

$$
\sum_{x\in Y_0(\mathbf F_{q^n})}\sum_{j\in\mathbf Z}(-1)^j
\Tr\bigl(F_x^{(n)}\mid
\mathcal H^j(\operatorname{For}K_E)_{\bar x}\bigr)
=
\sum_{i\in\mathbf Z}(-1)^i\Tr(F^n\mid H_c^i(Y,K)).
$$

For $K_E=E_Y$, so that $K=(\Qlb)_Y$, and
proper $Y_0$, the
point-count convention specializes to

$$
\#Y_0(\mathbf F_{q^n})
=\sum_{i\in\mathbf Z}(-1)^i\Tr(F^n\mid H^i(Y,\Qlb)).
$$

Here $F_x^{(n)}$ and $K_{\bar x}$ are the
local Frobenius and stalk
constructions, and $H_c^i$ is
compact-support cohomology.
