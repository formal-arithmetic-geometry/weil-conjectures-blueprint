+++
id = "thm-zl-riemann-hypothesis"
kind = "theorem"
title = "Riemann hypothesis for smooth proper schemes"
order = 3198
uses = ["cor-zl-purity-smooth-proper", "cor-zl-zeta-from-weights", "def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-reciprocal-roots", "def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "thm-pod-derived-poincare-duality", "thm-pur-rational-and-qbar-purity", "thm-zl-lefschetz-weil-identity", "thm-zl-wme-deligne-estimate"]
+++
Fix the finite-field datum
$(p,a,q,k_0,k)$, where $q=p^a$, and a prime $\ell\neq p$; write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$,
fix an isomorphism $\iota:\Qlb\xrightarrow{\sim}\mathbf C$, and interpret
the $\Qlb$-objects in the
algebraically closed
coefficient category. Let $X_0/k_0$ be
smooth, proper, geometrically
connected of pure dimension $d\in\mathbf Z_{\geq0}$, put
$X=X_0\times_{k_0}k$, let $F$ be the
global geometric Frobenius
in the geometric-Frobenius convention, and
let $(V_{i,\ell},F_{i,\ell},P_{i,\ell})_{0\leq i\leq2d}$ be the
smooth-proper
cohomological family extended to $\Qlb$. Use the
ordinary/reciprocal-root
convention. Then, for every $0\leq i\leq2d$, every
reciprocal root
$\alpha\in\Qlb$ of $P_{i,\ell}(T)=\det(1-TF_{i,\ell}\mid V_{i,\ell})$
satisfies

$$
\boxed{|\iota(\alpha)|=q^{i/2}}.
$$

Equivalently, in the ordinary-root convention, every zero $\beta$ of
$P_{i,\ell}$ satisfies $|\iota(\beta)|=q^{-i/2}$. Once the
zeta series is identified, by
[thm-zl-lefschetz-weil-identity], with

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_{i,\ell}(T)^{(-1)^{i+1}}\in\Qlb(T),
$$

this is the statement that the zeros and poles of $Z(X_0,T)$ arising
from the degree-$i$ factor have absolute value $q^{-i/2}$ under $\iota$.
The weight input is the
Frobenius-module weight
conclusion of [cor-zl-zeta-from-weights]. Its direct-image weight
input is proved from the affine-curve estimate and the subsequent
geometric reduction: [thm-zl-real-mixed-by-curves] supplies the
general-base filtration used in [lem-zl-relative-curve-mixedness].

## Proof

By [cor-zl-purity-smooth-proper] the Frobenius
modules $(H^i(X,\Qlb),F_i)$ are $\iota$-pure of weight $i$ for every
$0\leq i\leq2d$; the corresponding mixedness assertion for
$H_c^i$ is the second part of the same corollary. These are exactly the hypotheses of
[cor-zl-zeta-from-weights], whose root bound is the displayed
assertion $|\iota(\alpha)|=q^{i/2}$ of the theorem. The pure-weight
input is the weight estimate
([thm-zl-wme-deligne-estimate]) together with Poincare duality
([thm-pod-derived-poincare-duality]), as verified in
[cor-zl-purity-smooth-proper]; the smooth-proper purity of
the smooth-purity chapter, [thm-pur-rational-and-qbar-purity], is the recorded
alternative source of the same conclusions, and no obligation is left
open here.
