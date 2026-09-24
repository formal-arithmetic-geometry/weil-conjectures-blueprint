+++
id = "lemma-nagata-blowup-universal-graded-map"
kind = "lemma"
title = "The quotient construction is a graded algebra map"
order = 348
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-universal-graded-map", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
The degreewise map $\alpha_f$ respects the unit and multiplication and is a
graded algebra morphism.

## Proof

In degree $n$, tensor $q$ $n$ times. Let
$\mu_{\mathcal I}\colon(f^*\mathcal I)^{\otimes n}\to f^*(\mathcal I^n)$ be multiplication. The composite of $q^{\otimes n}$
with
multiplication isomorphism
$\mathcal L^{\otimes n}\cong\mathcal L^n$ from
[lemma-nagata-invertible-ideal-tensor-power] and the injection
$\mathcal L^n\hookrightarrow\mathcal O_Y$ is ordinary $n$-fold
multiplication. It therefore kills $\ker(\mu_{\mathcal I})$; injectivity
of $\mathcal L^n\hookrightarrow\mathcal O_Y$ shows that $q^{\otimes n}$
itself kills this kernel. Hence it factors uniquely through
$f^*(\mathcal I^n)$. These factorizations commute with multiplication by
associativity and with the degree-zero unit, giving the graded algebra map.
Associativity of tensor products and the multiplication maps for ideal
powers show that these degreewise maps preserve the unit and multiplication.
