+++
id = "prop-weight-purity"
kind = "theorem"
title = "Smooth-proper purity of the constant Weil sheaf"
lean = ["AlgebraicGeometry.WeilSheaf.isMixedOfWeightsAtMost_toComplex_adicConstant", "AlgebraicGeometry.WeilSheaf.weightPurity_adicConstant"]
order = 3217
tags = ["latex:proposition"]
uses = ["sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-bounded-constructible", "sk-def-sf-weil-complexes", "sk-prop-sfb-finite-extension-compatibility", "def-weil-complex-weights", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-ordinary-reciprocal-roots", "def-weil-pbc-proetale-site", "def-weil-smooth-proper-cohomological-family", "def-weil-weil-sheaf-complex", "thm-weil-deligne-purity"]
+++
Fix the global finite-field datum
$(p,a,q,k_0,k)$, where $p$ is prime and $a\in\mathbf Z_{\geq1}$ with
$q=p^a$. Choose a prime $\ell\neq p$, an algebraic closure
$\Qlb$ of $\Ql=\mathbf Q_\ell$, and an isomorphism
$\iota:\Qlb\xrightarrow{\sim}\mathbf C$. All coefficient sheaves are the pulled-back condensed rings
$\Lambda_X=p_X^*\Lambda$ on the pro-étale site ($\Lambda=\Ql,\Qlb$;
[sk-def-sfb-pulled-back-coefficients]), and complexes lie in
$D^b_c(X,\Lambda)\subset D(X_{\mathrm{proét}},\Lambda)$
([sk-def-sfb-bounded-constructible]), with Weil structures as in
[sk-def-sf-weil-complexes]. Let
$X_0/k_0$ be smooth, proper,
geometrically connected of pure dimension
$d\in\mathbf Z_{\geq0}$, and put $X=X_0\times_{k_0}k$. Let
$a_X:X\to\Spec k$ be the structure morphism, and let
$g_X=\operatorname{id}_{X_0}\times\operatorname{Spec}(\operatorname{Frob}_q)$
be the geometric-Frobenius automorphism.
Let $F_\ell$ be the induced
global geometric Frobenius
on the ordinary and
compactly supported cohomology with $\Ql$-coefficients,
and let $F_{\Qlb}$ be its scalar extension to the corresponding
$\Qlb$-cohomology. Define the graded cohomology notation by

$$
H^\bullet(X,\Lambda):=\bigoplus_{i\in\mathbf Z}H^i(X,\Lambda),
\qquad
H_c^\bullet(X,\Lambda):=\bigoplus_{i\in\mathbf Z}H_c^i(X,\Lambda)
\quad(\Lambda=\Ql,\Qlb).
$$

Use the scalar-extension identifications
([sk-prop-sfb-finite-extension-compatibility])

$$
H^\bullet(X,\Ql)\otimes_{\Ql}\Qlb\simeq H^\bullet(X,\Qlb),\qquad
H_c^\bullet(X,\Ql)\otimes_{\Ql}\Qlb\simeq H_c^\bullet(X,\Qlb).
$$

Assume $a_X:X\to\Spec k$ is
exceptional-adjoint
admissible at $\Qlb$, and choose a dualizing
Weil complex
$(\omega_X,\theta_{\omega_X})$ with

$$
\operatorname{For}(\omega_X)=Ra_X^!\Qlb,
$$

where $Ra_X^!$ is the
exceptional inverse image
for this admissible structure morphism, and require
$\theta_{\omega_X}$ to be the canonical functorial Weil lift induced by
geometric-Frobenius base change and the adjunction units and counits, rather
than an arbitrary lift.
These operators come from the constant
Weil sheaf $(\Qlb)_X$ on the
small pro-etale site, with the
geometric-Frobenius convention. Fix an
indeterminate $T$. For
$0\leq i\leq2d$, set

$$
H^i(X,\Qlb)=H^i\!\left(R\Gamma(X,(\Qlb)_X)\right),\qquad
H_c^i(X,\Qlb)=H^i\!\left(R\Gamma_c(X,(\Qlb)_X)\right),
\qquad
V_{i,\ell}=H^i(X,\Ql),
$$

and $F_{i,\ell}=F_\ell|_{V_{i,\ell}}$,
$P_{i,\ell}(T)=\det(1-TF_{i,\ell}\mid V_{i,\ell})$. These data are the
smooth-proper
cohomological family; reciprocal roots use the
ordinary/reciprocal-root
convention. Use the
complex-weight and
Frobenius-module weight
predicates. Then the constant
Weil sheaf $(\Qlb)_X$ is
$\iota$-pure of weight $0$.
