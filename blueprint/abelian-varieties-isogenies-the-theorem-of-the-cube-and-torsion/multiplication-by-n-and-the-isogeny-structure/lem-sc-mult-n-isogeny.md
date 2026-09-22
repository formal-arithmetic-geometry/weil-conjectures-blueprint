+++
id = "lem-sc-mult-n-isogeny"
kind = "lemma"
title = "Multiplication by n is surjective with finite kernel"
order = 4035
lean = ["AlgebraicGeometry.AbelianVariety.surjective_multByN", "AlgebraicGeometry.AbelianVariety.isFinite_torsion"]
uses = ["def-sc-mult-n", "def-sc-abelian-variety", "lem-sc-abelian-variety-projective", "lem-sc-ample-tensor", "lem-sc-mult-n-pullback", "lem-sc-ample-positive-degree", "lem-sc-av-commutative"]
+++
Let $A$ be an abelian variety [def-sc-abelian-variety] over a field $k$,
and let $n\geq1$. Then the map $[n]$ of [def-sc-mult-n] is a surjective
homomorphism of group schemes, and its kernel $A[n]$ is a finite group
scheme over $k$.

## Proof

*Reference: Stacks Project, Groupoid Schemes, Proposition 39.9.11 (3) and
(5), [Tag 03RP](https://stacks.math.columbia.edu/tag/03RP), whose proof is
Lemma 39.9.8, [Tag 0BFG](https://stacks.math.columbia.edu/tag/0BFG).* We
give the argument of loc. cit. The map $[n]$ of [def-sc-mult-n] is a
homomorphism of group schemes: the group law of $A$ is commutative by
[lem-sc-av-commutative], and for a commutative group scheme the $n$-fold
sum map is a homomorphism by the multiplication-by-$n$ lemma of the
group-scheme chapter.

*(i) Finiteness of the kernel.* By [lem-sc-abelian-variety-projective] and
[lem-sc-ample-tensor] there is an ample invertible module $\mathcal N$ on
$A$ with $[-1]^*\mathcal N\cong\mathcal N$, and by
[lem-sc-mult-n-pullback] $[n]^*\mathcal N\cong\mathcal N^{\otimes n^2}$. If
a fibre $[n]^{-1}(y)$ had positive dimension, it would contain a proper
curve $C$ (a positive-dimensional scheme of finite type over a field
contains an integral closed subscheme of dimension one), and on $C$ the
morphism $[n]$ is constant, so
$\mathcal O_C\cong[n]^*\mathcal N|_C\cong\mathcal N^{\otimes n^2}|_C$; but
the restriction of an ample module to a closed subscheme is ample, and an
ample module on a proper curve has positive degree
[lem-sc-ample-positive-degree], in particular it is not trivial — a
contradiction. Hence every fibre of $[n]$ is finite. The morphism $[n]$ is
proper ($A$ is proper and the target is separated), so $[n]$ is proper and
quasi-finite, hence finite (the finite-iff-proper-with-finite-fibres
theorem of the quasi-finite chapter; *reference: Stacks Project, Cohomology
of Schemes, [Tag 02OG](https://stacks.math.columbia.edu/tag/02OG): proper
and quasi-finite implies finite*). In particular the kernel
$A[n]=[n]^{-1}(e)$ is finite.

*(ii) Surjectivity.* The image $H:=[n](A)\subseteq A$ is a closed subgroup
scheme of $A$ by the image lemma of the group-scheme chapter (the source
$A$ is proper over $k$ and the target $A$ is separated of finite type over
$k$), applied to the homomorphism $[n]$. Since $[n]$ is finite,
its fibres have dimension zero, and the dimension formula for the
surjective morphism $A\to H$ gives $\dim H=\dim A-\dim A[n]=\dim A$. Thus
$H\subseteq A$ is a closed subscheme of the irreducible scheme $A$ with
$\dim H=\dim A$; the reduced subscheme $H_{\mathrm{red}}\subseteq A$ is
then a closed subscheme of the reduced irreducible scheme $A$ of the same
dimension, hence $H_{\mathrm{red}}=A$, and therefore $H=A$. So
$[n]:A\to A$ is surjective.

Unresolved dependencies: def:sc-group-scheme, thm:pqf-finite-iff-proper-finite-fibres, lem:sc-mult-n-homomorphism, lem:sc-image-subgroup
