+++
kind  = "proof"
of    = "thm-constructible-serre"
uses = ["def-constructible-finite-locally-constant", "def-constructible-refines", "def-constructible-stratification", "lemma-constructible-common-refinement", "lemma-constructible-flc-biproduct", "lemma-constructible-flc-serre", "lemma-constructible-iso-invariance", "lemma-constructible-of-refines"]
+++
Let $\varphi\colon\mathcal F\to\mathcal F'$ be a morphism of constructible
sheaves. By [lemma-constructible-common-refinement] and
[lemma-constructible-of-refines] there is one stratification
$(\iota_k\colon Z_k\to X)_k$ such that all $\iota_k^*\mathcal F$ and
$\iota_k^*\mathcal F'$ are finite locally constant. Since $\iota_k^*$ is
exact, $\iota_k^*\ker\varphi=\ker(\iota_k^*\varphi)$ and
$\iota_k^*\operatorname{coker}\varphi=\operatorname{coker}(\iota_k^*\varphi)$
are finite locally constant by [lemma-constructible-flc-serre] (for the
kernel, $\Lambda$ Noetherian), so
$\ker\varphi$ and $\operatorname{coker}\varphi$ are constructible with
respect to the same stratification. The same argument, using exactness of
$\iota_k^*$ and the extension part of [lemma-constructible-flc-serre],
handles extensions, and [lemma-constructible-flc-biproduct] handles
finite direct sums. A full subcategory of an abelian category closed under
kernels, cokernels and extensions is a weak Serre subcategory.
