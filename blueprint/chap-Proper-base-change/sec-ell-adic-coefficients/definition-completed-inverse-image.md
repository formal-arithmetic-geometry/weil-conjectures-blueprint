+++
id = "definition-completed-inverse-image"
kind = "definition"
title = "Completed inverse image"
order = 409
lean = ["AlgebraicGeometry.Scheme.completedPullbackObject", "AlgebraicGeometry.Scheme.completedPullbackFunctor"]
uses = ["definition-small-pro-etale-site"]
+++
Let $g:Y'\to Y$ be a morphism. For $M\in D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, the
*completed inverse image* is

$$
\hat g^*M
=R\varprojlim_n g^*(M\otimes^{\mathbf L}_{\mathcal O_{E,Y}}
(\mathcal O_E/\pi_E^n)_Y)
\in D(Y'_{\mathrm{pro}\acute{e}t},\mathcal O_E).
$$
