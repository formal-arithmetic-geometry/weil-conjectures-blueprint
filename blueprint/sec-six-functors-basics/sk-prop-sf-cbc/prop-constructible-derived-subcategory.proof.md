+++
kind  = "proof"
of    = "prop-constructible-derived-subcategory"
uses = ["def-constructible-constant", "def-constructible-finite", "def-constructible-finite-locally-constant", "def-constructible-locally-constant", "def-constructible-stratification", "def-kun-separably-closed", "lemma-constructible-iso-invariance", "lemma-constructible-pullback-locally-constant"]
+++
For a weak Serre subcategory $\mathcal C$ of an abelian category, the
complexes with cohomology in $\mathcal C$ form a triangulated subcategory
of the derived category: the zero object and shifts are clear, and for a
distinguished triangle $K\to L\to M\to K[1]$ with $K$ and $M$ having
cohomology in $\mathcal C$, the long exact cohomology sequence
$H^{n}(K)\to H^n(L)\to H^n(M)$ exhibits $H^n(L)$ as an extension of a
subobject of $H^n(M)$ (a kernel) by a quotient of $H^n(K)$ (a cokernel),
both in $\mathcal C$, hence $H^n(L)\in\mathcal C$. Apply this to the weak
Serre subcategory of [thm-constructible-serre]. (In the formalisation the
general statement is `DerivedCategory.homologyProperty_isTriangulated`, for any
property of objects closed under isomorphisms, kernels, cokernels and extensions; it is
applied to the constructible sheaves with these closure properties, the content of
[thm-constructible-serre], as hypotheses.)
