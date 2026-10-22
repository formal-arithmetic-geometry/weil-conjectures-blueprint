+++
id = "lem-pc-projective-space-twist-quotient"
kind = "lemma"
title = "A finite quotient by twists"
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_epi_sigma_twist"]
order = 632
uses = ["def-pc-projective-space-twist", "lem-pc-section-clearing-denominators", "pqf-def-coherent", "pqf-lem-coherent-ft-locnoeth"]
+++
Let $A$ be Noetherian, $P=\mathbf P^n_A$, and $\mathcal F$ a
coherent module on $P$.
There are integers $m_1,\ldots,m_r\ge0$ and a surjection

$$
\bigoplus_{j=1}^r\mathcal O_P(-m_j)\longrightarrow\mathcal F,
$$

where the summands are the
twisting modules.
Its kernel is coherent.
