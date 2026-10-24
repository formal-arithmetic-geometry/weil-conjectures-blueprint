+++
id = "thm-weil-deligne-purity"
kind = "theorem"
title = "Deligne smooth-proper purity"
lean = ["AlgebraicGeometry.WeilSheaf.deligne_purity", "AlgebraicGeometry.WeilSheaf.isPunctuallyPureOfWeight_adicConstant", "AlgebraicGeometry.WeilSheaf.hasWeightsAtMostOver_compactlySupportedCohomology_adicConstant", "AlgebraicGeometry.WeilSheaf.isPureOfWeightOver_cohomology_of_isLisse", "AlgebraicGeometry.WeilSheaf.isLisse_adicConstant"]
order = 4094
uses = ["cor-zl-purity-smooth-proper", "def-trf-frobenius-operators", "def-weil-complex-weights", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "det-def-sfb-pulled-back-coefficients", "sk-def-sf-weil-complexes", "lem-zl-constant-sheaf-weight-zero", "prop-weil-proper-compact-coincidence", "thm-sf-dual-perfect", "thm-zl-wme-deligne-estimate"]
+++
Fix a prime $p$, an integer $a\in\mathbf Z_{\geq1}$, put $q=p^a$,
$k_0=\Fq$, and let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Choose a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, choose an
algebraic closure $\Qlb$ of $\Ql$, and
let $\iota:\Qlb\hookrightarrow\mathbf C$ be any field embedding. Let
$X_0/k_0$ be smooth and proper of pure dimension
$d\in\mathbf Z_{\geq0}$, and put
$X=X_0\times_{k_0}k$. Let
$a_X:X\to\operatorname{Spec}k$ be the structure morphism, and let
$\gamma=\operatorname{Frob}_q$ and $g_X=\operatorname{id}_{X_0}\times \operatorname{Spec}(\gamma)$ be the
geometric Frobenius; let $F$ be the induced
global geometric-Frobenius
operator. Let
$(\Qlb)_X=p_X^*\Qlb$ be the coefficient sheaf on the
small pro-etale site ([det-def-sfb-pulled-back-coefficients]), with its
canonical Weil structure ([sk-def-sf-weil-complexes]). For each $0\leq i\leq2d$, let

$$
H_c^i(X,\Qlb)=H^i\!\left(Ra_{X!}(\Qlb)_X\right),\qquad
H^i(X,\Qlb)=H^i\!\left(Ra_{X*}(\Qlb)_X\right),
$$

using the ordinary and
compactly supported cohomology functors, with the
induced $F$-actions. Weight predicates for
$(\Qlb)_X$ use the
Weil-complex weight definition (with the dualizing Weil complex
$Ra_X^!\Qlb$ fixed there); weights for the cohomology groups use
Frobenius-module weights. Then,
for every $0\leq i\leq2d$, the following five assertions hold:

1. the constant Weil sheaf
$(\Qlb)_X$ is $\iota$-pure of weight $0$;
1. $H_c^i(X,\Qlb)$ is $\iota$-mixed of weights at most $i$;
1. the canonical comparison
$$
H_c^i(X,\Qlb)\xrightarrow{\sim}H^i(X,\Qlb)
$$
is Frobenius-equivariant;
1. the geometric-Frobenius
module $H^i(X,\Qlb)$ is $\iota$-pure of weight $i$;
1. every eigenvalue $\alpha$ of
geometric Frobenius on
$H^i(X,\Qlb)$ satisfies $|\iota(\alpha)|=q^{i/2}$.
