+++
id = "proposition-twisting-weight-zero-adding-dual"
kind = "proposition"
title = "Twisting to weight zero and adding the dual"
order = 1188
lean = ["AlgebraicGeometry.WeilSheaf.realEnvelope", "AlgebraicGeometry.WeilSheaf.isReal_realEnvelope", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.realEnvelope", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.exists_units_norm_eq"]
+++
Let $\mathcal F\ne0$ be lisse and pure of weight $w$ on a nonempty
finite-type scheme over $k_0$.  There is $b\in\overline{\mathbf Q}_\ell^\times$ with
$|\iota(b)|=q^{-w/2}$.  Put

$$
\mathcal F^0=\mathcal F\otimes\mathcal B_b,
\qquad \mathcal E=\mathcal F^0\oplus(\mathcal F^0)^\vee.
$$

Then $\mathcal E$ is real and pure of weight zero, contains
$\mathcal F^0$ as a direct summand, and at points over $k_n$ its trace
is twice the real part of the trace of $\mathcal F^0$.
