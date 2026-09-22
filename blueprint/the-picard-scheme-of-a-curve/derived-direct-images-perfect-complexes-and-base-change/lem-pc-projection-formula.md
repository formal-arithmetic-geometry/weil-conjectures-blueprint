+++
id = "lem-pc-projection-formula"
kind = "lemma"
title = "The projection formula"
order = 4350
lean = ["AlgebraicGeometry.projection_formula"]
uses = ["def-pc-derived-category", "def-pc-derived-direct-image", "def-pc-base-change"]
+++
Let $f:X\to Y$ be a quasi-compact, quasi-separated morphism of schemes. For
$E\in D_{\mathrm{QCoh}}(\mathcal{O}_X)$ and
$K\in D_{\mathrm{QCoh}}(\mathcal{O}_Y)$ the canonical map
$$
Rf_*(E)\otimes_{\mathcal{O}_Y}^{\mathbb L}K\;\longrightarrow\;
Rf_*(E\otimes_{\mathcal{O}_X}^{\mathbb L}Lf^*K)
$$
is an isomorphism; in particular, for an invertible $\mathcal{O}_Y$-module
$\mathcal{N}$,
$Rf_*(E)\otimes\mathcal{N}\cong Rf_*(E\otimes f^*\mathcal{N})$.

## Proof

The map of the statement (defined in Cohomology, Equation 20.54.2.1) is
natural in $E$ and $K$, so:

1. The assertion is local in $Y$: if $Y=\bigcup_{i\in I}V_i$ is an open
   covering, the objects and the map restrict to the open sets (the derived
   functors localize: $Rf_*$ and $\otimes^{\mathbb L}$ are computed on the
   open subschemes and the restriction maps are the restrictions of the
   canonical maps), and $D_{\mathrm{QCoh}}$-identifications can be checked
   on an open cover. So we may assume $Y$ affine,
   $Y=\operatorname{Spec}(A)$.
2. For affine $Y$, the functor
   $D_{\mathrm{QCoh}}(\mathcal{O}_Y)\to D(A)$ (global sections, with the
   standard equivalence $D_{\mathrm{QCoh}}(\mathcal{O}_Y)\cong D(A)$, cf.
   Derived Categories of Schemes, Lemma 36.3.5, Section 36.3, [Tag
   08CU](https://stacks.math.columbia.edu/tag/08CU)) identifies both sides.
   The case $K=A[k]$ is the statement $Rf_*(E[k])\cong Rf_*(E)[k]$ (the
   shift: clear). An object $K$ is a retract of a complex built up by
   direct sums and distinguished triangles from the shifts $A[k]$: the
   functors $Lf^*$, $\otimes^{\mathbb L}$, $Rf_*$ preserve direct sums and
   exact triangles, so the property "$P(K)$ holds" is stable under
   triangles and passes to direct sums, and the class of $K$ with $P(K)$
   contains $A[k]$ and is closed under those two operations and under
   retracts. That the subcategory so generated is all of $D(A)$ is the
   standard generation argument: truncations reduce to the bounded case,
   and a bounded complex is filtered by the shifts of its terms through the
   triangles $M^{[p,q]}\to M^{[p,q+1]}\to M^{q+1}[-q-1]\to$, with $M^q$
   free after a resolution — as in the proof of Lemma 36.22.1, [Tag
   08EU](https://stacks.math.columbia.edu/tag/08EU). Hence $P(K)$ holds for
   all $K$.
3. The last statement: for an invertible $\mathcal{N}$, take $\mathcal{N}$
   as an object of $D_{\mathrm{QCoh}}$; the natural map
   $Rf_*E\otimes\mathcal{N}\to Rf_*(E\otimes f^*\mathcal{N})$ is the
   $\otimes^{\mathbb L}$-statement specialized to $K=\mathcal{N}[0]$, using
   $\otimes^{\mathbb L}\mathcal{N}=\otimes\,\mathcal{N}$ and
   $L f^*\mathcal{N}=f^*\mathcal{N}$ since $\mathcal{N}$ is locally free.

Unresolved dependencies: def:sc-invertible-module
