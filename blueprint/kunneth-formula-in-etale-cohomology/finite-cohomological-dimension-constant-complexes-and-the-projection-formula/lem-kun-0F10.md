+++
id = "lem-kun-0F10"
kind = "lemma"
title = "Finite cohomological dimension of finite-type morphisms"
order = 6094
lean = ["AlgebraicGeometry.Etale.cohomologicalDimension_lt_top_of_finiteType"]
uses = ["def-kun-cd", "def-kun-separably-closed", "lem-kun-cd-sep-closed-point"]
+++
Let $K$ be a field and let $f:X\to Y$ be a morphism between schemes of
finite type over $K$.

1. $\operatorname{cd}(f)<\infty$.
2. If $K$ is separably closed [def-kun-separably-closed], then
   $\operatorname{cd}(X)<\infty$ for every scheme $X$ of finite type over
   $K$.

Clauses (1) and (2) are the classical finiteness of the cohomological
dimension of a scheme of finite type over a field, which this manuscript
already imports elsewhere: the finiteness chain of the constructibility
chapter uses it, and the Jacobian chapter proves the curve case, so that
the curve and proper instances are internal to the blueprint. The affine
bound $\operatorname{cd}(X)\le\operatorname{cd}(K)+\dim X$ for affine $X$ of
finite type over $K$ (Stacks Tag
[0F0V](https://stacks.math.columbia.edu/tag/0F0V)) is not needed here.

(*Source:* Stacks Project, Lemma 59.96.2, [Tag
0F10](https://stacks.math.columbia.edu/tag/0F10): clause (1) is assertion
(1) of that lemma, and clause (2) is its assertion (2) — which assumes
$\operatorname{cd}(K)<\infty$ — combined with
[lem-kun-cd-sep-closed-point].) In the Stacks Project the proof uses the
induction principle of Cohomology of Schemes, Lemma 30.4.1, [Tag
08DR](https://stacks.math.columbia.edu/tag/08DR), with the affine cases
[Tag 0F0X](https://stacks.math.columbia.edu/tag/0F0X) and [Tag
0F0V](https://stacks.math.columbia.edu/tag/0F0V), together with the
Mayer–Vietoris sequences [Tag
0EYK](https://stacks.math.columbia.edu/tag/0EYK) and [Tag
0A50](https://stacks.math.columbia.edu/tag/0A50).

## Proof

This is the recorded classical input named in the statement, Stacks Project,
[Tag 0F10](https://stacks.math.columbia.edu/tag/0F10): a morphism of schemes
of finite type over a field has finite cohomological dimension, and over a
separably closed field every such scheme does. The curve and proper
instances are internal to the blueprint, as recorded in the statement; no
separate proof of the general case is given.

Unresolved dependencies: def:weil-pbc-scheme-conventions, sbc-thm-finiteness-finite-type, lem:sc-cohomological-dimension
