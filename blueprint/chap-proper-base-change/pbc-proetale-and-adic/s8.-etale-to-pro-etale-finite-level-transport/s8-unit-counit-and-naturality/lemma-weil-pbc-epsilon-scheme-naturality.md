+++
id = "lemma-weil-pbc-epsilon-scheme-naturality"
kind = "lemma"
title = "Naturality of the comparison in the scheme"
order = 1808
uses = ["def-weil-pbc-epsilon-comparison", "def-weil-pbc-epsilon-unit-counit", "def-weil-pbc-etale-proetale-inclusion"]
+++
For a scheme morphism $u:X\to Y$, base change on the two sites gives a
canonical natural isomorphism

$$
u_{\mathrm{proet}}^*\iota_Y\xrightarrow{\sim}
\iota_Xu_{\mathrm{et}}^*.
$$

It is compatible with identities and composition in $u$, and the induced
square of geometric morphisms carries $\eta^Y,\varepsilon^Y$ to
$\eta^X,\varepsilon^X$.

## Proof

On an etale object $V\to Y$, both composites have underlying $X$-scheme
$X\times_YV\to X$; on a morphism they both use its base change. The identity
map of this fiber product gives the component of the natural isomorphism.
The associativity and unit isomorphisms for fiber products give its
composition and identity coherence. Under this identification, the unit is
still represented by an identity arrow and the counit is still restriction
along $W\to\iota_XU$. The formulas in Definition
[def-weil-pbc-epsilon-unit-counit] therefore give the two compatibility
squares.
