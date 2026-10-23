+++
id = "lemma-nagata-rees-localization-degree-zero"
kind = "lemma"
title = "Compatibility with degree zero"
lean = ["AlgebraicGeometry.gradeZeroRingHom_comp_reesGradingZero"]
order = 183
uses = ["lemma-nagata-rees-degree-zero", "prop-nagata-rees-localization"]
+++
Let $\varphi\colon A\to B$ be a ring homomorphism and let $J=\varphi(I)B$.
Under the identifications $\mathcal R_A(I)_0\cong A$ and
$\mathcal R_B(J)_0\cong B$ of [lemma-nagata-rees-degree-zero], the
degree-zero component of the coefficientwise map
$\rho_\varphi\colon\mathcal R_A(I)\to\mathcal R_B(J)$ is $\varphi$. In
particular, for the localization $A\to A_s$ it is the localization map.
