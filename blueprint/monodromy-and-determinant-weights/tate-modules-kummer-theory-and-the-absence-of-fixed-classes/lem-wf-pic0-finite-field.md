+++
id = "lem-wf-pic0-finite-field"
kind = "lemma"
title = "Finiteness of the degree-zero Picard group over a finite field"
order = 4078
uses = ["def-pc-degree-line-bundle", "def-pc-smooth-projective-curve", "lem-pc-dense-separable-points", "lem-wf-effective-divisors-finite-field"]
+++
Let $C_0$ be a smooth projective
curve over a finite field $\mathbf F_Q$ which is geometrically irreducible,
of genus $g$. Then the group
$\operatorname{Pic}^0(C_0)=\ker(\deg:\operatorname{Pic}(C_0)\to\mathbf Z)$
of classes of degree $0$ is finite.

## Proof

By [lem-pc-dense-separable-points] the curve $C_0$, being smooth and
nonempty over the field $\mathbf F_Q$, has a closed point $x$; put
$e:=[\kappa(x):\mathbf F_Q]<\infty$ and let $D_x$ be the corresponding
effective Cartier divisor of degree $e$, with degrees as in
[def-pc-degree-line-bundle]. Choose $n\geq1$ with $ne\geq g$. For a
class $\mathcal M\in\operatorname{Pic}^0(C_0)$ the invertible module
$\mathcal M\otimes\mathcal O(nD_x)$ has degree $ne$, so by Riemann–Roch
over the field $\mathbf F_Q$ — Stacks Project, Algebraic Curves, Lemma
53.5.2 ([Tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6)), valid
over an arbitrary ground field — its space of global sections is nonzero,
and a nonzero global section exhibits it as $\mathcal O(D)$ for an effective
Cartier divisor $D$ of degree $ne$. The assignment
$D\mapsto\mathcal O(D-nD_x)$ is therefore a surjection from the set of
effective Cartier divisors of degree $ne$, which is finite by
[lem-wf-effective-divisors-finite-field], onto
$\operatorname{Pic}^0(C_0)$. Hence $\operatorname{Pic}^0(C_0)$ is finite.
