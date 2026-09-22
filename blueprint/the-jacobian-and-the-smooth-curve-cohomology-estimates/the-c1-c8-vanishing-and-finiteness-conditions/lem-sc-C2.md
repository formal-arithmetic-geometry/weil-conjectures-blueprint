+++
id = "lem-sc-C2"
kind = "lemma"
title = "C2: vanishing on affine curves"
order = 4543
lean = ["AlgebraicGeometry.Curve.C2_constant"]
uses = ["def-weil-pbc-eight-curve-assertions", "thm-sc-affine-cohomology", "lem-sc-affine-cohomological-dimension", "lem-sc-artin-schreier-dimension"]
+++
Let $k$ be algebraically closed, let $C$ be a smooth affine curve over $k$,
and let $n$ be a prime. Then the constant sheaf $\mathbf F_n$ satisfies
$\mathcal C_2(C,\mathbf F_n)$ of [def-weil-pbc-eight-curve-assertions]: $H^q(C_{\Et},\mathbf F_n)=0$ for every
$q>1$.

## Proof

If $n\neq\operatorname{char}k$, this is [thm-sc-affine-cohomology]. If
$n=\operatorname{char}k=p>0$, then $\mathbf F_p$ is $p$-primary and the
assertion follows from [lem-sc-artin-schreier-dimension] (and from
[lem-sc-affine-cohomological-dimension] directly).

Unresolved dependencies: def:sc-curves
