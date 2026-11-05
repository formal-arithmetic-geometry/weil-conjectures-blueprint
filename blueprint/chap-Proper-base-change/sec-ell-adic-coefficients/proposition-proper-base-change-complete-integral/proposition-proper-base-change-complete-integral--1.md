+++
id = "proposition-proper-base-change-complete-integral--1"
kind = "proposition"
title = "Completeness and finite reduction of direct image"
order = 417001
aliases = ["bp-r127-1"]
lean = ["AlgebraicGeometry.ProEtale.internal_integral_direct_image_limits"]
+++
Let $p:X\to Y$ be proper, let $g:Y'\to Y$ be any morphism, and let
$p':X'\to Y'$ and $g':X'\to X$ be the projections from $X'=X\times_YY'$.
Fix a finite extension $E/\mathbf Q_\ell$. Suppose that
$K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ is derived $\pi_E$-complete and that
each reduction

$$
K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X
$$

belongs to $D^+_{\mathrm{class}}(X_{\mathrm{pro}\acute{e}t},\mathcal O_E/\pi_E^n)$. Then
$Rp_*K$ is derived $\pi_E$-complete.

More generally, let $p:X\to Y$ be any morphism of schemes, and put $\kappa_E=\mathcal O_E/\pi_E$. For every
$M\in D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, the canonical comparison
between inverse image and derived reduction is an isomorphism

$$
(p^*M)\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\kappa_E)_X
\xrightarrow{\ \sim\ }
p^*\bigl(M\otimes^{\mathbf L}_{\mathcal O_{E,Y}}(\kappa_E)_Y\bigr).
$$

For every $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$, its adjoint
comparison, obtained using the inverse of this isomorphism and the counit
$p^*Rp_*K\to K$, is an isomorphism

$$
(Rp_*K)\otimes^{\mathbf L}_{\mathcal O_{E,Y}}(\kappa_E)_Y
\xrightarrow{\ \sim\ }
Rp_*\bigl(K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\kappa_E)_X\bigr).
$$

If $K$ is derived $\pi_E$-complete, then $Rp_*K$ is derived
$\pi_E$-complete. Here neither properness nor classicality of the reductions is needed.
