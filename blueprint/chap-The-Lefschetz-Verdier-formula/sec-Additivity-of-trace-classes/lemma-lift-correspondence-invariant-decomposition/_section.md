+++
id = "lemma-lift-correspondence-invariant-decomposition"
kind = "lemma"
title = "Lifting a correspondence to an invariant decomposition"
order = 937
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "proposition-splitting-ind-etale-covers", "theorem-existence-contractible-covers", "theorem-pro-etale-refinements-weakly-etale", "proposition-pro-etale-affines-form-basis", "lemma-w-contractible-affines-projective", "proposition-comparison-morphism-inverse-image", "lemma-acyclicity-pulled-back-injectives", "theorem-comparison-direct-images", "lemma-comparison-direct-images-compatibilities", "proposition-locally-constant-sheaves-finite-presentation", "theorem-comparison-constructible-sheaves", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-derived-adic-completeness", "lemma-reduction-derived-nakayama", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-integral-models", "proposition-inverting-ell", "lemma-cohomology-modules-underlying-abelian", "definition-derived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "proposition-cohomology-p-1-over-henselian", "proposition-proper-base-change-projective-line", "lemma-finite-cover-projective-space", "proposition-proper-base-change-etale-site", "theorem-proper-base-change-classical-pro", "proposition-forgetting-supports-composition", "proposition-composition-open-restriction-compactifications-f", "definition-exceptional-base-change-finite", "proposition-adjunction-projective-line", "lemma-smooth-morphisms-locally-constant-sheaves", "lemma-extension-across-finite-subset", "lemma-generic-smooth-open", "definition-change-of-coefficients-maps", "proposition-six-operations-change-coefficients", "proposition-dctf-x-qbar-2-colimit", "lemma-degree-zero-calculation", "lemma-reduction-field", "lemma-reduction-curve-over-normal-base", "proposition-base-change-larger-algebraically-closed", "lemma-change-coefficients", "lemma-kunneth-field-coefficients", "definition-relative-dualizing-complex", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "remark-non-noetherian-compactifications", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "theorem-theorem-cube", "lemma-symmetric-ample-sheaf", "proposition-multiplication-n", "definition-relative-picard-functor", "corollary-degree-jacobian"]
+++
Let $c:C\to X\times X$ be a correspondence, $i:Z\to X$ a closed
immersion with open complement $j:U\to X$, and suppose

$$
c_1^{-1}(Z)\subset c_2^{-1}(Z),
\qquad\text{equivalently }c_2^{-1}(U)\subset c_1^{-1}(U).
$$

Let $u$ be a cohomological correspondence on $(X,K)$, and write
$K_U=j_!j^*K$ and $K_Z=Ri_*i^*K$ for the two pieces of the localization
triangle $K_U\to K\to K_Z$. Then $u$ has a lift, unique up to
contractible choice, to a cohomological correspondence $\tilde u$ in the
filtered derived category on the two-step filtered complex given by this
triangle. Its graded pieces are cohomological correspondences $u_U$ on
$(X,K_U)$ and $u_Z$ on $(X,K_Z)$, and $\widehat u_Z$ restricted to $Z$ is

$$
Rc_{1Z!}c_{2Z}^*i^*K\simeq i^*\Theta K
\xrightarrow{i^*\widehat u}i^*K.
$$
