+++
id = "sk-thm-sf-identification"
kind = "theorem"
title = "Derived Poincaré duality"
order = 3291
uses = ["sk-def-sp-trace", "sk-def-pairing", "sk-cor-sp-all-coefficients", "sk-thm-sf-global-duality", "sk-lem-finite", "sk-lem-sf-twist-interchange", "sk-thm-sf-tensor-hom"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerStar_coefficientDual_of_orientation"]
tags = ["sketch"]
+++
Let $X/k$ be smooth, separated of pure dimension $d$, with $k$ algebraically
closed. For every admissible $\Lambda$ and $K\in\Dctf(X,\Lambda)$, purity gives
isomorphisms in $\Dctf(X,\Lambda)$

$$
\omega_X\simeq\Lambda_X(d)[2d],\qquad
\mathbb D_XK\simeq\cHom_X(K,\Lambda_X)(d)[2d].
$$

Put $K^\vee=\cHom_X(K,\Lambda_X)$; when $K$ is locally perfect over $\Lambda_X$, so
is $K^\vee$, and it is the ordinary dual. Let $\operatorname{Tr}_X$ be the map
induced on $R\Gamma_c$ by the smooth trace of $a_X$ [sk-def-sp-trace]. The pairing
in $D(\Lambda)$

$$
\begin{aligned}
\beta_K:\quad
R\Gamma_c(X,K)\otimes^{\mathbf L}R\Gamma\bigl(X,K^\vee(d)\bigr)[2d]
&\longrightarrow R\Gamma_c\bigl(X,\Lambda_X(d)\bigr)[2d]\\
&\xrightarrow{\operatorname{Tr}_X}\Lambda
\end{aligned}
$$

is perfect in the sense of [sk-def-pairing], and its adjoint is the canonical
isomorphism

$$
R\Gamma\bigl(X,K^\vee(d)\bigr)[2d]
\xrightarrow{\sim}
R\operatorname{Hom}_\Lambda\bigl(R\Gamma_c(X,K),\Lambda\bigr).
\tag{1}
$$

If $X$ is proper, $R\Gamma_c$ may be replaced by $R\Gamma$.

*Complement.* If $X$ is proper, $K$ is locally perfect over $\Lambda_X$ and
$\Lambda=A_{E,n}=\mathcal O_E/\pi_E^n$, the degreewise form of (1) gives perfect
pairings

$$
\langle-,-\rangle_i:H_c^i(X,K)\times H^{2d-i}\bigl(X,K^\vee(d)\bigr)
\longrightarrow\Lambda\qquad(i\in\mathbf Z),
$$

because this ring is self-injective, so that $\operatorname{Hom}_\Lambda(-,\Lambda)$
is exact.
