+++
id = "lemma-nagata-rees-localization-mul"
kind = "lemma"
title = "Iterated localization coherence"
order = 88
lean = ["AlgebraicGeometry.reesGrading.hom_localization_mul", "AlgebraicGeometry.AffineBlowup.hom_localization_mul"]
uses = ["prop-nagata-rees-localization"]
+++
Let $s,t\in A$. Localizing the Rees algebra first at $s$ and then at the
image of $t$ gives the same graded ring homomorphism as localizing at $st$,
after the canonical isomorphism $(A_s)_t\cong A_{st}$: the composite
$\mathcal R_A(I)\to\mathcal R_{A_s}(IA_s)\to\mathcal R_{(A_s)_t}(I(A_s)_t)
\to\mathcal R_{A_{st}}(IA_{st})$ of coefficientwise maps equals
$\rho_{st}$. Consequently the same holds for the induced morphisms of
affine blow-ups.
