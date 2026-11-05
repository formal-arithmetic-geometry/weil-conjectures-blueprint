+++
id = "proposition-base-change-fourier-inversion--2"
kind = "proposition"
title = "Fourier transform and constant twists"
name_showing = false
order = 1229003
aliases = ["bp-r379-2"]
lean = ["AlgebraicGeometry.nonempty_iso_fourierTransform_of_iso_constantTwist"]
uses = ["definition-weil-structure", "lemma-artin-schreier-character-sheaf"]
+++
The compatibility with tensoring by an arbitrary complex on the base is
bypassed by Lean; the mainline uses the following case of constant twists.

Let $k_0$ be a finite field, let $\ell\ne\operatorname{char}(k_0)$ be prime,
and let $\psi:k_0\to\Qbarl^\times$ be an additive character. For
$b\in\Qbarl^\times$, write $T_b$ for the exact functor on pro-étale Weil
sheaves which multiplies the Weil structure by $b$, and also for its
induced functor on the derived category. Let $K,K'$ be bounded
constructible Weil complexes on $\mathbf A^1_{k_0}$, and suppose that
$K'\simeq T_bK$ in the derived category of pro-étale Weil sheaves. Then
in that category there is an isomorphism
$$
\operatorname{FT}_\psi(K')\simeq T_b\operatorname{FT}_\psi(K).
$$
No nontriviality assumption on $\psi$ is needed.
