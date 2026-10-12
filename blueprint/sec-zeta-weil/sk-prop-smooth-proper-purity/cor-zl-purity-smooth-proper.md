+++
id = "cor-zl-purity-smooth-proper"
kind = "theorem"
title = "Purity of smooth proper cohomology"
order = 3173
tags = ["latex:corollary"]
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-exceptional-adjoint-admissibility", "def-weil-finite-field-fiber", "def-weil-frobenius-detailed", "def-weil-frobenius-module-weights", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-local-frobenius-trace", "def-weil-punctual-weights", "prop-weil-operations", "prop-zl-smooth-proper-relative-purity"]
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
$X$; no admissibility hypothesis is imposed on the structure morphism
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
