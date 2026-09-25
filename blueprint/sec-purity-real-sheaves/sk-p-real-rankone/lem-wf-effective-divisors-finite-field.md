+++
id = "lem-wf-effective-divisors-finite-field"
kind = "lemma"
title = "Effective divisors of fixed degree over a finite field are finite"
order = 2784
uses = ["def-pc-degree-line-bundle", "def-pc-relative-effective-cartier", "def-pc-smooth-projective-curve", "thm-pc-hilb-curves"]
+++
Let $C_0$ be a smooth projective
curve over a finite field $\mathbf F_Q$ which is geometrically irreducible,
and let $d\geq0$. Then the set of
effective Cartier divisors of
degree $d$ on $C_0$, the degree being that of
[def-pc-degree-line-bundle], is finite.

## Proof

By [thm-pc-hilb-curves] the effective Cartier divisors of degree $d$ on
$C_0$ are the $\mathbf F_Q$-rational points of the Hilbert scheme
$\underline{\operatorname{Hilb}}^d_{C_0/\mathbf F_Q}$, and that Hilbert
scheme is a variety of finite type over $\mathbf F_Q$; the divisors and their
degrees are those of [def-pc-relative-effective-cartier] and
[def-pc-degree-line-bundle]. A scheme of finite type over a finite field
has only finitely many rational points: cover it by finitely many affine
opens, each of which embeds as a closed subscheme of an affine space over
$\mathbf F_Q$, and an affine space over the finite field $\mathbf F_Q$ has
finitely many $\mathbf F_Q$-points. Hence the set of divisors is finite.
