+++
id = "lem-weil-compact-support-finite-field-independence"
kind = "lemma"
title = "Independence of the finite coefficient field"
order = 1495
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-integral-rational-qbar-compact-support", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "lem-weil-scalar-extension-composition", "prop-weil-pbc-descent-functors"]
+++
Let $K_0$ be a field, let $X,Y$ be finite-type
[def-weil-scheme-morphism-properties] $K_0$-schemes, let $f:X\to Y$ be a
separated finite-type $K_0$-morphism, fix a prime $\ell$ whose image in $K_0$
is invertible, and fix an algebraic closure $\Qlb$ of $\Ql$. Let
$K_{\Qlb}\in D^b_c(X,\Qlb)$ be an object of the common-stage category of
[def-weil-algebraically-closed-coefficients] represented at the finite
coefficient stages $E\subset L\subset\Qlb$ by $K_E\in D^b_c(X,E)$ and $K_L\in
D^b_c(X,L)$ of [def-weil-rationalization-karoubi]. Then the two objects

$$
 Rf_!K_E\otimes_E\Qlb,\qquad Rf_!K_L\otimes_L\Qlb
$$

of $D^b_c(Y,\Qlb)$, formed from the compact-support functor
[def-weil-integral-rational-qbar-compact-support], are canonically
isomorphic.
