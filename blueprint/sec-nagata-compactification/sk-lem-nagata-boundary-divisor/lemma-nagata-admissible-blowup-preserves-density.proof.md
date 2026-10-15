+++
kind  = "proof"
of    = "lemma-nagata-admissible-blowup-preserves-density"
uses = ["def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-invertible-ideal", "lemma-nagata-dense-flat-pullback", "thm-nagata-blowup-principalizes-center", "thm-nagata-global-blowup-complement"]
+++
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
