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
are finite locally constant by [lemma-constructible-flc-serre], so
$\ker\varphi$ and $\operatorname{coker}\varphi$ are constructible with
respect to the same stratification. The same argument, using exactness of
$\iota_k^*$ and the extension part of [lemma-constructible-flc-serre],
handles extensions, and [lemma-constructible-flc-biproduct] handles
finite direct sums. A full subcategory of an abelian category closed under
kernels, cokernels and extensions is a weak Serre subcategory.


Work on an affine open of $T$, and refine the finitely many partitions of
the given constructible sheaves to one common partition, as in the
definition of a constructible complex. Inverse image to a part is exact, by
the stalkwise exactness of geometric stalks. It suffices to prove the
assertions for finite locally constant sheaves on each part, locally for the
topology of the small etale site.

For a map between two such sheaves, trivialize both near a geometric point.
The images of the finitely many elements of the first constant module are
sections of the second. After an etale refinement each is a specified
constant section. The map is then induced by a map of finite modules, whose
kernel and cokernel give the constant kernel and cokernel sheaves. These
descriptions prove the first two assertions.

Consider an extension $0\to F'\to F\to F''\to0$ with $F'$ and $F''$ finite
locally constant. Fix a geometric point $\bar t$ and trivialize both outer
sheaves on an etale neighbourhood. By the exactness of geometric stalks, the
middle stalk $B=F_{\bar t}$ is an extension of two finite modules and is
finite. Represent each of its finitely many elements by a section of $F$ on
a common pointed etale neighbourhood. All addition, zero and
scalar-multiplication relations of $B$ hold after a further common
refinement: there are only finitely many relations since $B$ and $\Lambda$
are finite, and equality in a stalk means equality on such a neighbourhood.
Also impose the finitely many equalities identifying the chosen sections of
the submodule with the constant sections of $F'$, and their images with the
constant sections of $F''$. We obtain a map from the constant exact sequence
of stalk modules to the given exact sequence, which is the identity on the
outer terms. The kernel--cokernel argument for a map of short exact
sequences makes the middle map an isomorphism; equivalently, apply the same
argument on every stalk and conservativity of geometric stalks. Thus $F$ is
finite locally constant near every point. Applying this on the common
partition proves extension closure and completes the proof.
