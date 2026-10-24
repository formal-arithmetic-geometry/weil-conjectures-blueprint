+++
id = "cor-zl-purity-smooth-proper"
kind = "theorem"
title = "Purity of smooth proper cohomology"
lean = ["AlgebraicGeometry.WeilSheaf.purity_smoothProper", "AlgebraicGeometry.WeilSheaf.isPureOfWeightOver_cohomology_of_isLisse", "AlgebraicGeometry.WeilSheaf.isLisse_adicConstant", "AlgebraicGeometry.WeilSheaf.isPunctuallyPureOfWeight_adicConstant", "AlgebraicGeometry.WeilSheaf.hasWeightsAtMostOver_compactlySupportedCohomology_adicConstant"]
order = 4093
tags = ["latex:corollary"]
uses = ["det-def-sfb-pulled-back-coefficients", "det-def-sfb-bounded-constructible", "def-weil-exceptional-adjoint-admissibility", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-local-frobenius-trace", "def-weil-punctual-weights", "prop-weil-operations", "prop-zl-smooth-proper-relative-purity"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$,
let $\iota:\Qlb\hookrightarrow\mathbf C$ be any field embedding, and use the
coefficient sheaves $\Lambda_X=p_X^*\Lambda$ of the condensed rings
$\Lambda=\Ql,\Qlb$ on the pro-étale site
([det-def-sfb-pulled-back-coefficients]), with complexes in
$D^b_c(X,\Lambda)\subset D(X_{\mathrm{proét}},\Lambda)$
([det-def-sfb-bounded-constructible]). Let $X_0/k_0$ be
smooth and proper of pure dimension $d\in\mathbf Z_{\geq0}$, put
$X=X_0\times_{k_0}k$, let $F$ be the
global geometric Frobenius
in the geometric-Frobenius convention, and
let $(\Qlb)_X=p_X^*\Qlb$ be the constant
$\Qlb$-sheaf on
$X_{\mathrm{proét}}$; no admissibility hypothesis is imposed on the structure morphism
$a_X:X_0\to\Spec k_0$ (its exceptional inverse image is the constructible
one, defined for every separated finite-type morphism; the ambient notion of
[def-weil-exceptional-adjoint-admissibility] is not used). Then, for every $i\in\mathbf Z$, the Frobenius module

$$
(H^i(X,\Qlb),F)
$$

is $\iota$-pure of weight $i$ in the sense of
[def-weil-frobenius-module-weights]; the group
$H_c^i(X,\Qlb)=H^i(X,\Qlb)$ (proper coincidence,
[prop-weil-operations]) is $\iota$-mixed of weights at most $i$.
