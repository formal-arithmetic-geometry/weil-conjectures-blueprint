+++
id = "lemma-nagata-blowup-universal-graded-map"
kind = "lemma"
title = "The quotient construction is a graded algebra map"
order = 348
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup"]
uses = ["def-nagata-blowup-universal-graded-map", "def-nagata-global-blowup-cover-comparison", "lemma-nagata-invertible-ideal-tensor-power", "prop-nagata-global-blowup-cover-independent"]
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
