+++
id = "lem-pc-picard-functor-agrees-sc"
kind = "lemma"
title = "Agreement with the affine Picard functor of the earlier chapter"
order = 4274
lean = ["AlgebraicGeometry.picardFunctor_restrict_affine"]
uses = ["def-pc-picard-functor", "def-pc-fppf-site", "def-pc-picard-presheaf", "def-pc-scheme"]
+++
Let $k$ be a field and $X$ a smooth projective curve
[def-pc-smooth-projective-curve] over $k$. The restriction of
$\operatorname{Pic}_{X/k}$ [def-pc-picard-functor] to affine $k$-schemes
$T=\operatorname{Spec}(R)$ is canonically the sheafification presented in
the divisors chapter, namely the fppf sheafification of
$R\mapsto\operatorname{Pic}(X\times_k\operatorname{Spec} R)$; more
precisely
$\operatorname{Pic}_{X/k}(\operatorname{Spec}(R))=\operatorname{Pic}_{X/k}^{\mathrm{sc}}(R)$
where the right side is the value of the Picard functor of that chapter.

## Proof

Both sides are the fppf sheafification of the same presheaf on the category
of affine $k$-schemes: the left is the restriction of the fppf
sheafification on $(\mathit{Sch}/k)_{fppf}$, and fppf sheafification
commutes with restricting to the essentially full subcategory of affine
schemes, because the $(\mathit{Sch}/k)_{fppf}$-coverings of an affine
scheme and the corresponding coverings by affines cofinalize (every scheme
is covered by open affines in the Zariski, hence fppf, topology; and for
our purposes the affine objects fully capture the value of a sheaf). More
precisely: let $F_T=\operatorname{Pic}(X_T)$ and let
$\pi:(\mathit{Sch}/k)_{fppf}\to(\mathit{Aff}/k)_{fppf}$ be the restriction;
the map of sites $\pi$ induces for the sheafification
$(\pi^{-1}F^\#)^\#=(\pi^{-1}F)^\#$ for the restriction of the sheafified
functor to affine schemes; the sheaves that are sheafifications of
presheaves on the affine site are exactly the fppf sheaves on
$(\mathit{Aff}/k)_{fppf}$, and the two prescriptions agree on affine
inputs. This is the standard construction of the big sites (see Topologies,
Section 34.7, [Tag 021S](https://stacks.math.columbia.edu/tag/021S)).

Unresolved dependencies: def:sc-picard-functor
