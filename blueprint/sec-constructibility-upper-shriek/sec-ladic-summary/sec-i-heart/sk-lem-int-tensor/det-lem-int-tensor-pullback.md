+++
id = "det-lem-int-tensor-pullback"
kind = "lemma"
title = "Integral inverse image preserves $\\Dbc$ and agrees with the completed inverse image"
order = 2473
uses = ["det-lem-int-tensor-shriek", "sk-prop-sfb-cartesian-coefficients", "sk-lem-integral-models", "def-pe-derived-complete"]
+++
Let $g\colon X\to Y$ be a morphism of standing schemes and
$g^*\colon\D(Y_{\mathrm{proét}},\mathcal O_E)\to\D(X_{\mathrm{proét}},\mathcal O_E)$ the inverse image.

1. $g^*$ maps $\Dbc(Y,\mathcal O_E)$ into $\Dbc(X,\mathcal O_E)$.
2. For $K\in\Dbc(Y,\mathcal O_E)$ the natural map
   $$
   c_K\colon g^*K\longrightarrow R\varprojlim_ng^{-1}\bigl(K\otimes^{\mathbf L}\mathcal O_E/\pi_E^n\bigr)
   $$
   is an isomorphism. After restriction of scalars to the constant sheaf
   $\underline{\mathcal O_E}$ the target is the completed inverse image of
   the Stacks Project (Stacks, Tags 099I, 09C4), so on
   $\Dbc(-,\mathcal O_E)$ the inverse image $g^*$ agrees with the completed inverse
   image.
