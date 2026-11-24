+++
id = "remark-constructible-sheaves-coefficient-rings"
kind = "remark"
title = "Constructible sheaves for the individual coefficient rings"
name_showing = false
order = 223
+++
1. For Noetherian $X$, every locally closed subset is constructible,
   so in Definition [definition-constructible-sheaves](2) any finite stratification
   by locally closed subschemes may be used.
2. For finite $A$ and qcqs $X$, [$D^b_{\mathrm{ctf}}(X,A)$](@definition-constructible-sheaves) is the pullback of the
   usual étale category $D^b_{\mathrm{ctf}}(X_{\acute{e}t},A)$ by
   Corollary [corollary-finite-tor-amplitude-under-comparison].
3. If $\Lambda=E$ or $\overline{\mathbf Q}_\ell$, the ring $\Lambda(*)$ is a field,
   so each $P_i$ is a finite-dimensional vector space, and
   a [lisse](@definition-lisse-sheaves) module is locally free of
   finite rank. In other words, a [constructible](@definition-constructible-sheaves) $E$- or $\overline{\mathbf Q}_\ell$-sheaf is
   one that is [lisse](@definition-lisse-sheaves) on the strata of a finite stratification
   [bhatt-scholze15, Definition 6.8.6].
4. If $\Lambda=\mathcal O_E$, locally on a stratum a [constructible](@definition-constructible-sheaves)
   [$\mathcal O_{E,X}$](@lemma-comparison-completed-coefficients)-module is $P\otimes_{\mathcal O_E}\href{@lemma-comparison-completed-coefficients}{\mathcal O_{E,X}}$
   for a finitely generated $\mathcal O_E$-module $P$. For example,
   $\href{@lemma-comparison-completed-coefficients}{\mathcal O_{E,X}}/\pi_E$ is [constructible](@definition-constructible-sheaves).
5. For the admissible coefficients, the [constructible sheaves](@definition-constructible-sheaves) form an
   abelian category. For finite $A$ this is the classical theory of
   sheaves with finite stalks, and the other cases are
   Lemma [lemma-constructible-sheaves],
   Corollary [corollary-coefficient-heart-b] and
   Lemma [lemma-structure-integral-constructible-complexes], which we
   prove in Subsection [subsec-Integral-coefficients].
6. For finite $A$, a [lisse](@definition-lisse-sheaves) $A_X$-module is the same as a locally
   constant sheaf with finite stalks. For $\Lambda=\mathcal O_E$ a [lisse](@definition-lisse-sheaves)
   module may have torsion, such as $\href{@lemma-comparison-completed-coefficients}{\mathcal O_{E,X}}/\pi_E$; the [lisse](@definition-lisse-sheaves)
   [$\mathcal O_{E,X}$](@lemma-comparison-completed-coefficients)-modules without torsion are the locally free ones of
   finite rank, since a finitely generated torsion free $\mathcal O_E$-module
   is free.
