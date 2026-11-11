+++
id = "lemma-change-coefficients"
kind = "lemma"
title = "Change of coefficients"
order = 699
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "definition-derived-adic-completeness", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "theorem-proper-base-change-classical-pro", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-schematic-closure-uniqueness", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Suppose that the schemes in (8.1) are of finite type over
$k$. Let $\Lambda\to\Lambda'$ be a coefficient map of
Proposition [proposition-six-operations-change-coefficients] and let
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$. Then the square

$$
\begin{CD}
(g^*Rf_*K)_{\Lambda'} @>>> (Rf'_*g'^*K)_{\Lambda'}\\
@VVV @VVV\\
g^*Rf_*(K_{\Lambda'}) @>>> Rf'_*g'^*(K_{\Lambda'})
\end{CD}
$$

commutes. Here the upper arrow is the extension of scalars of the base change
map (4.5) for $K$, the lower arrow is the base change map
for $K_{\Lambda'}$, and the vertical arrows are the composites of the
change-of-coefficients isomorphisms of
Proposition [proposition-six-operations-change-coefficients] for $g^*$ and
$Rf_*$, respectively for $Rf'_*$ and $g'^*$.
