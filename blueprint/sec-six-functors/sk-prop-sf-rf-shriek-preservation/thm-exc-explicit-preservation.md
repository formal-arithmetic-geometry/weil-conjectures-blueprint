+++
id = "thm-exc-explicit-preservation"
kind = "theorem"
title = "Preservation in the open and finite etale cases"
order = 2367
uses = ["def-weil-constructible-intervals", "def-weil-derived-tensor", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-scheme-morphism-properties", "prop-exc-finite-etale-adjoint", "prop-exc-open-adjoint"]
+++
Let $A=A_{E,n}$, and let $f:V\to X$ be an
open immersion or a finite
etale morphism. Its ambient exceptional right adjoint satisfies

$$
Rf^{\times}D_c^{[a,b]}(X,A)\subseteq D_c^{[a,b]}(V,A).
$$

Here $D_c^{[a,b]}$ denotes the
constructible interval.
It also preserves the same
Tor-amplitude interval.
For every quotient $A\to B=A_{E,m}$, $m\leq n$, its
derived coefficient comparison is
an isomorphism:

$$
(Rf_A^{\times}K)\otimes_A^L B
\simeq Rf_B^{\times}(K\otimes_A^L B).
$$

For finite-Tor input the two sides are bounded constructible.
All bounds are independent of $n$.
