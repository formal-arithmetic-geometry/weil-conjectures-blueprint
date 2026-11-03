+++
id = "cor-mg-rankone-weight-from-element"
kind = "theorem"
title = "Rank-one weight from a positive-degree element"
lean = ["AlgebraicGeometry.Monodromy.DegreeDatum.norm_apply_eq_rpow_iff", "AlgebraicGeometry.Monodromy.DegreeDatum.forall_norm_eq_rpow_iff_exists", "AlgebraicGeometry.Monodromy.DegreeDatum.forall_norm_eq_rpow_iff_forall"]
order = 4025
tags = ["latex:corollary"]
uses = ["def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "def-wf-weil-group", "lem-wf-rank-one-component-modulus", "sk-lem-coefficient-heart"]
+++
Let $X_0$ be a normal geometrically connected curve over $k_0$, put
$|k_0|=q$, and let
$\mathcal L_0$ be a rank-one lisse
Weil sheaf on $X_0$ with Weil
character $\chi:\hyperref[def-wf-weil-group]{W(X_0)}\to E^\times$, with $E/\mathbf Q_\ell$
finite, such that $\chi(\pi_1(X))$ is finite, and fix
$\iota:E\hookrightarrow\mathbf C$. For $w\in\mathbf R$ the
sheaf $\mathcal L_0$ is punctually $\iota$-pure of weight $w$ if
and only if there is (equivalently, for every) element
$\sigma\in W(X_0)$ of positive degree $d$ with

$$
|\iota(\chi(\sigma))|=q^{wd/2}.
$$
