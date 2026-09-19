+++
id = "lem-zla-finite-coordinate-lattice"
kind = "lemma"
title = "Finite-coordinate lattice"
order = 1009
uses = ["def-zla-integral-shift-lattice", "lem-zla-finite-coordinates"]
+++
With the notation of [def-zla-integral-shift-lattice], there is a finite
set $J\subset\mathbf N$ such that coordinate evaluation

$$
\operatorname{ev}_J:W\longrightarrow\mathbf Q^J
$$

is injective. Its restriction maps $M(a)$ injectively into $\mathbf Z^J$.
Hence $M(a)$ is a finite free abelian group.

## Proof

Choose a basis of $W$ consisting of shifts of $a$ and let $J$ be a set of
coordinates on which the corresponding determinant does not vanish
([lem-zla-finite-coordinates]); then $\operatorname{ev}_J$ is injective on
$W$ for dimension reasons. Every element of $M(a)$ is an integral linear
combination of integral sequences, hence integral, so
$\operatorname{ev}_J(M(a))\subseteq\mathbf Z^J$, and a subgroup of a finite
free abelian group is finite free.
