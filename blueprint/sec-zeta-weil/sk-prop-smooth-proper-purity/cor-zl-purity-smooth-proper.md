+++
id = "cor-zl-purity-smooth-proper"
kind = "theorem"
title = "Purity of smooth proper cohomology"
order = 3080
tags = ["latex:corollary"]
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-wf-wt", "def-wf-wtge", "def-wf-wtle", "lem-tw-multiplicativity", "lem-wf-tate-twist-frobenius", "prop-weil-operations", "thm-pod-derived-poincare-duality", "thm-zl-wme-deligne-estimate"]
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
let $(\Qlb)_X$ be the constant
$\Qlb$-sheaf on
$X$. Then, for every $i\in\mathbf Z$, the Frobenius module

$$
(H^i(X,\Qlb),F)
$$

is $\iota$-pure of weight $i$ in the sense of
[def-weil-frobenius-module-weights]; the group
$H_c^i(X,\Qlb)=H^i(X,\Qlb)$ (proper coincidence,
[prop-weil-operations]) is $\iota$-mixed of weights at most $i$.

## Proof

The constant $\Qlb$-sheaf is the constant [def-wf-wt] pure weight
$0$ constructible
[def-weil-frobenius-module-weights]-module; its pushforward data
along the structure morphism of
[def-weil-finite-field-fiber] $a_X:X_0\to\Spec k_0$ (a separated finite-type morphism, so the
hypotheses of [thm-zl-wme-deligne-estimate] hold) give, for every
$i$,

$$
H_c^i(X,\Qlb)=H^i(X,\Qlb)\ \ \text{mixed of weights at most}\ i
$$

(the proper coincidence is item (4) of
[prop-weil-operations], and the compact-support form of
[thm-zl-wme-deligne-estimate] is the upper bound $0+i$). This
is the upper bound $\mathrm{WtLe}(H^i(X,\Qlb),i)$ in the sense of
[def-wf-wtle].

For the lower bound, apply [thm-pod-derived-poincare-duality] to
$X$ (smooth proper of pure dimension $d$) with
$K=(\Qlb)_X$, which is perfect over $(\Qlb)_X$; it gives the
Frobenius-equivariant isomorphism

$$
H^i(X,\Qlb)^\vee\;\cong\;H^{2d-i}\bigl(X,(\Qlb)_X^\vee(d)\bigr)
=H^{2d-i}\bigl(X,\Qlb(d)\bigr),
$$

where $\Qlb(d)$ is the Tate twist of [lem-wf-tate-twist-frobenius],
punctually pure of weight $-2d$. Applying the upper bound above to the
lisse constant sheaf $\Qlb(d)$ (an independent instance of the same
argument, or verbatim the same step) gives the last group mixed of
weights at most $-2d+(2d-i)=-i$, hence $H^i(X,\Qlb)^\vee$ is so, and
passing to duals – inverse eigenvalues,
[lem-tw-multiplicativity] – shows that $H^i(X,\Qlb)$ is mixed of
weights at least $i$ ([def-wf-wtge]). Together with the upper
bound ([def-wf-wtle]) this is $\iota$-purity of weight $i$
([def-wf-wt]), as asserted.
