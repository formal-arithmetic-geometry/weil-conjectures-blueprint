+++
id = "lemma-nagata-admissible-blowup-preserves-density"
kind = "lemma"
title = "Density is preserved by an admissible blow-up"
order = 103
lean = ["AlgebraicGeometry.IsAdmissible.isSchemeTheoreticallyDominant_preimage_ι", "AlgebraicGeometry.Scheme.IdealSheafData.isSchemeTheoreticallyDominant_blowupMap_preimage_compl_support"]
uses = ["def-nagata-admissible-blowup", "def-nagata-dense-compactification", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "def-nagata-scheme-theoretically-dense-open", "lemma-nagata-dense-flat-pullback", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-global-blowup-complement"]
+++
Let $\mathcal I$ be a quasi-coherent ideal on a scheme $X$. Then the inverse
image of $X\setminus V(\mathcal I)$ is scheme-theoretically dense in
$\operatorname{Bl}_{\mathcal I}(X)$. Moreover, let $U\subseteq X$ be an open
subscheme such that $U\hookrightarrow X$ is quasi-compact and
scheme-theoretically dense, and let $\operatorname{Bl}_{\mathcal I}(X)\to X$
be a $U$-admissible blow-up (so $\mathcal I$ is of finite type and
$V(\mathcal I)\cap U=\varnothing$). Then the inverse image of $U$ is
scheme-theoretically dense in $\operatorname{Bl}_{\mathcal I}(X)$.

## Proof

First, the complement of the support of an invertible ideal is
scheme-theoretically dense: on an affine open where the ideal is generated
by a single non-zero-divisor $a$, the restriction map to the complement of
the support is the localization away from $a$, which is injective.
Applying this on $\operatorname{Bl}_{\mathcal I}(X)$ to the extended ideal
$\mathcal I\mathcal O_{\operatorname{Bl}_{\mathcal I}(X)}$, which is
invertible by [thm-nagata-blowup-principalizes-center] and whose vanishing
locus is the inverse image of $V(\mathcal I)$, shows that the inverse image
$\pi^{-1}(W)$ of the complement $W=X\setminus V(\mathcal I)$ of the center
is scheme-theoretically dense in the blow-up
$\pi\colon\operatorname{Bl}_{\mathcal I}(X)\to X$. This is the first
assertion; no finiteness of $\mathcal I$ is used.

For the second assertion, $V(\mathcal I)\cap U=\varnothing$ gives
$U\subseteq W$. Density now descends along the partial isomorphism:
$\pi$ is an isomorphism over $W$ by
[thm-nagata-global-blowup-complement], hence also over the smaller
open $U\subseteq W$; since $U$ is quasi-compact and scheme-theoretically
dense in $X$, the inclusion $U\hookrightarrow W$ is scheme-theoretically
dominant, and transporting it across the isomorphism over $W$ and composing
with the scheme-theoretically dense open immersion
$\pi^{-1}(W)\hookrightarrow \operatorname{Bl}_{\mathcal I}(X)$ shows that
$\pi^{-1}(U)$ is scheme-theoretically dense.

Consequently the same holds for a finite composite of such blow-ups: at
each stage the inverse image of $U$ is again a quasi-compact
scheme-theoretically dense open, so induction on the length of the
composite applies the one-step assertion at each stage.
