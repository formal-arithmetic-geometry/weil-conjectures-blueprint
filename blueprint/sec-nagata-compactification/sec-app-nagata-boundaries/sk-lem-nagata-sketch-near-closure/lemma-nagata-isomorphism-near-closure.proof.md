+++
kind  = "proof"
of    = "lemma-nagata-isomorphism-near-closure"
uses = ["cor-nagata-blowup-product-common-refinement", "def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-product-comparison", "def-nagata-blowup-product-domination-maps", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-invertible-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-maximal-isomorphism-open", "def-nagata-proj-closed-center-finite-degree", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "lemma-nagata-affine-blowup-complement", "lemma-nagata-blowup-invertible-factor", "thm-nagata-global-blowup-proper", "lemma-nagata-composition-center-ideal", "lemma-nagata-elimination-indeterminacy", "lemma-nagata-extend-admissible-blowup", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-ideal-unit-off-support", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-localization-ideal-pow", "lemma-nagata-maximal-isomorphism-open", "lemma-nagata-product-ideal-common-blowup", "lemma-nagata-proper-to-separated-target", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-separate-constructible-closed", "lemma-nagata-spectral-constructible-separation-exists", "prop-nagata-affine-blowup-chart", "prop-nagata-rees-graded", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property", "thm-nagata-strict-transform-is-blowup"]
+++
We show that $\pi=\mathsf{IsoBl}_{V,T}(q)\to X$ of
[def-nagata-isomorphism-near-closure] has this property, using the notation
of that construction. By [lemma-nagata-maximal-isomorphism-open] the
assumed isomorphism neighbourhood of $T$ is contained in
$\operatorname{IsoOpen}(q)$, so $T$ and $E$ are disjoint and the construction
applies; moreover $V_2=V\setminus E_c\subseteq\operatorname{IsoOpen}(q)$, so $q$
is an isomorphism over $V_2$. Since $\pi_1$ is an isomorphism over $V$, the
strict transform $\lambda_1$ is an isomorphism over $\pi_1^{-1}(V_2)$ by
[lemma-nagata-strict-transform-over-complement]. It is proper: its composite
with $\pi_1$ is $q$ composed with the proper blow-up $Z_1\to Z$, and $\pi_1$ is
separated.

By [lemma-nagata-elimination-indeterminacy], applied to $\lambda_1$ over the
qcqs scheme $X_1$ and the quasi-compact open $\pi_1^{-1}(V_2)$, the strict
transform of $\lambda_1$ along the elimination blow-up is an open immersion.
The centre $D$ agrees on $A$ with the elimination centre
([lemma-nagata-extend-admissible-blowup]), so over the inverse image of $A$
in $\operatorname{Bl}_D(X_1)$ the strict transform of $\lambda_1$ is again an
open immersion. By [lemma-nagata-admissible-blowup-comp] the blow-up
$X'=\operatorname{Bl}_K(X)$ is identified with $\operatorname{Bl}_D(X_1)$ over
$X$, compatibly with the strict transforms of $q$ and of $\lambda_1$. Let
$A'\subseteq X'$ be the inverse image of $A$. Over $A'$ the strict transform
$q'$ of $q$ along $\pi$ is an open immersion, and it is proper, being a
closed subscheme of a base change of $q$
([prop-nagata-strict-transform-closed-fiber-product]). Let $N'\subseteq A'$
be the image of $q'$ over $A'$; it is open, and $q'$ restricts to an
isomorphism over $N'$.

It remains to see that $N'$ contains the closure of $\pi^{-1}(T)$. This
closure lies over $\overline{\pi_1^{-1}(T)}\subseteq
\overline{\pi_1^{-1}(T_c)}\subseteq A$, hence in $A'$. The range of $q'$ is
closed because $q'$ is proper, and it contains $\pi^{-1}(T)$ because $\pi$
is an isomorphism over $V\supseteq T$ and $q$ is an isomorphism over a
neighbourhood of $T$. Hence the closure of $\pi^{-1}(T)$ lies in the range
of $q'$ over $A'$, which is $N'$.
