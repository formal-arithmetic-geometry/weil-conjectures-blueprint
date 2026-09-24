+++
id = "thm-constructible-serre"
kind = "theorem"
title = "Constructible sheaves form a weak Serre subcategory"
order = 1487
lean = ["AlgebraicGeometry.Scheme.IsConstructibleSheaf.cokernel", "AlgebraicGeometry.Scheme.IsConstructibleSheaf.kernel"]
uses = ["def-constructible-constructible", "lemma-constructible-common-refinement", "lemma-constructible-flc-serre", "lemma-constructible-of-refines", "prop-constructible-pullback"]
+++
Let $\mathcal A=\mathrm{Mod}_\Lambda$ with $\Lambda$ a finite ring. The
kernel and the cokernel of a morphism between constructible sheaves on
$\et X$, finite direct sums of constructible sheaves, and the middle term of
a short exact sequence whose outer terms are constructible, are
constructible. Consequently the constructible sheaves form a weak Serre
subcategory of $\shv{\et X}$. (The kernel and cokernel statements are
formalised, for any ring $\Lambda$, as are the instances
`IsClosedUnderKernels` and `IsClosedUnderCokernels` of
`Etale.constructibleSheaf`; the extension statement is not.)

## Proof

Let $\varphi\colon\mathcal F\to\mathcal F'$ be a morphism of constructible
sheaves. By [lemma-constructible-common-refinement] and
[lemma-constructible-of-refines] there is one stratification
$(\iota_k\colon Z_k\to X)_k$ such that all $\iota_k^*\mathcal F$ and
$\iota_k^*\mathcal F'$ are finite locally constant. Since $\iota_k^*$ is
exact, $\iota_k^*\ker\varphi=\ker(\iota_k^*\varphi)$ and
$\iota_k^*\operatorname{coker}\varphi=\operatorname{coker}(\iota_k^*\varphi)$
are finite locally constant by [lemma-constructible-flc-serre], so
$\ker\varphi$ and $\operatorname{coker}\varphi$ are constructible with
respect to the same stratification. The same argument, using exactness of
$\iota_k^*$ and the extension part of [lemma-constructible-flc-serre],
handles extensions, and [lemma-constructible-flc-biproduct] handles
finite direct sums. A full subcategory of an abelian category closed under
kernels, cokernels and extensions is a weak Serre subcategory.
