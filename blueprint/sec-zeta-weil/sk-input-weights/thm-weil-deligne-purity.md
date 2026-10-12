+++
id = "thm-weil-deligne-purity"
kind = "theorem"
title = "Deligne smooth-proper purity"
order = 3177
uses = ["cor-zl-purity-smooth-proper", "def-trf-frobenius-operators", "def-weil-complex-weights", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-frobenius-coefficient-twists", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "lem-zl-constant-sheaf-weight-zero", "prop-weil-proper-compact-coincidence", "thm-sf-dual-perfect", "thm-zl-wme-deligne-estimate"]
+++
Fix a prime $p$, an integer $a\in\mathbf Z_{\geq1}$, put $q=p^a$,
$k_0=\Fq$, and let $k=\Fbar$ be the
fixed algebraic closure of $k_0$.
Choose a prime $\ell\neq p$, write $\Ql=\mathbf Q_\ell$, choose an
algebraic closure $\Qlb$ of $\Ql$, and
an isomorphism $\iota:\Qlb\xrightarrow{\sim}\mathbf C$. Let
$X_0/k_0$ be smooth, proper,
geometrically connected of pure dimension
$d\in\mathbf Z_{\geq0}$, and put
$X=X_0\times_{k_0}k$. Let
$a_X:X\to\operatorname{Spec}k$ be the structure morphism, and let
$\gamma=\operatorname{Frob}_q$ and $g_X=\operatorname{id}_{X_0}\times \operatorname{Spec}(\gamma)$ be the
geometric Frobenius; let $F$ be the induced
global geometric-Frobenius
operator. Let
$(\Qlb)_X$ be the constant object in the
Weil-complex category on the
small pro-etale site. For each $0\leq i\leq2d$, let

$$
H_c^i(X,\Qlb)=H^i\!\left(Ra_{X!}(\Qlb)_X\right),\qquad
H^i(X,\Qlb)=H^i\!\left(Ra_{X*}(\Qlb)_X\right),
$$

using the ordinary and
compactly supported cohomology functors. Assume
$a_X:X\to\Spec k$ is exceptional-adjoint
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
than an arbitrary lift. Assume directly that all displayed
cohomology groups are finite-dimensional $\Qlb$-vector spaces equipped with the
induced $F$-actions. Weight predicates for
$(\Qlb)_X$ and for these complexes use the
Weil-complex weight definition; weights for the resulting vector spaces use
finite-dimensional
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
