+++
kind  = "proof"
of    = "det-lem-coefficient-heart-closure"
+++
*Local models over a field.* Since $\Lambda(*)$ is a field, a finitely presented
$\Lambda(*)$-module is $\Lambda(*)^r$, and $\Lambda_U\otimes_{\Lambda(*)}\Lambda(*)^r=\Lambda_U^r$;
conversely a finite free module is a finite constant local model. So "finite constant
local model" means "lisse".

(1) Choose a cover $\{U\to S\}$ on which $F'$ and $F''$ are free, $F''|_U\cong\Lambda_U^r$ with
basis $e_1,\dots,e_r\in F''(U)$. Since $F\to F''$ is an epimorphism of sheaves, after
refining the cover each $e_k$ lifts to $\tilde e_k\in F(U)$. The map $\Lambda_U^r\to F|_U$,
$e_k\mapsto\tilde e_k$, splits the sequence on $U$, so $F|_U\cong F'|_U\oplus\Lambda_U^r$ is
free of finite rank.

(2) The coefficient sheaves $E_S$, $\Qlb_S$ agree with those of Bhatt–Scholze
(Lemma 6.8.2 of *The pro-étale topology for schemes*, together with
[sk-prop-sfb-qlbar-colimit-x]), and their lisse sheaves agree with ours. By Bhatt–Scholze,
Corollary 6.8.5 (for topologically Noetherian $S$), lisse $\Lambda_S$-modules form an abelian
subcategory closed under kernels and cokernels; the rank of $\ker\phi$ and $\coker\phi$ is
locally constant on $S$, and no further stratification is needed. (The underlying reason:
on a connected $S$, lisse $E_S$-sheaves are equivalent to continuous representations of the
pro-étale fundamental group on finite-dimensional $E$-vector spaces, an abelian category,
and kernels and cokernels are computed in it; for $\Qlb$ one passes to the colimit over $E$.)

*Globalization.* Given constructible $F,G$ and $\phi\colon F\to G$, or an extension
$0\to F'\to F\to F''\to0$ with $F',F''$ constructible, choose a common refinement of the
stratifications ([det-lem-coefficient-heart-common-stratification] (1)); by (2) of that lemma
all modules involved are lisse on every stratum. Restriction to strata is exact
([det-lem-coefficient-heart-common-stratification] (3)), so $(\ker\phi)|_S=\ker(\phi|_S)$,
$(\coker\phi)|_S=\coker(\phi|_S)$, and $0\to F'|_S\to F|_S\to F''|_S\to0$ is exact; these are
lisse by (1), (2). Hence kernels, cokernels and extensions are constructible. A full
subcategory of an abelian category closed under kernels and cokernels (and containing $0$
and finite direct sums, which are extensions) is abelian, with exact inclusion.
