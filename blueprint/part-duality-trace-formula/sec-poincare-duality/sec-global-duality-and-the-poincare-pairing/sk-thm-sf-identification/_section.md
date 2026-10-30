+++
id = "sk-thm-sf-identification"
kind = "theorem"
title = "Poincaré duality"
order = 519
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerStar_coefficientDual_of_orientation"]
uses = ["sk-def-sp-trace", "sk-def-pairing", "sk-cor-sp-all-coefficients", "sk-thm-sf-global-duality", "sk-lem-finite", "sk-lem-sf-twist-interchange", "sk-thm-sf-tensor-hom", "sk-thm-purity-transport", "sk-prop-scalar-six"]
tags = ["sketch"]
+++
Let $X/k$ be smooth, separated of pure dimension $d$, with
$k$ algebraically closed. For every admissible $\Lambda$ and
$K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, Theorem [sk-thm-purity-transport] gives isomorphisms

$$
\omega_X\simeq\Lambda_X(d)[2d],\qquad
\mathbb D_XK\simeq
\cHom_X(K,\Lambda_X)(d)[2d].
$$

Put $K^\vee=\cHom_X(K,\Lambda_X)$. If $K$ is locally perfect over
$\Lambda_X$, then so is $K^\vee$, and it is the ordinary dual. Let $\operatorname{Tr}_X$ be the map induced on $R\Gamma_c$ by
the trace map of $a_X$ (Definition [sk-def-sp-trace]). The
pairing

$$
\begin{split}
\beta_K:\quad
R\Gamma_c(X,K)\otimes^{\mathbf L}
R\Gamma(X,K^\vee(d))[2d]
&\longrightarrow R\Gamma_c(X,\Lambda_X(d))[2d]\\
&\xrightarrow{\operatorname{Tr}_X}\Lambda
\end{split}
\tag{11.6}
$$

is perfect, and its adjoint is the canonical isomorphism

$$
R\Gamma(X,K^\vee(d))[2d]
\xrightarrow{\sim}
R\!\operatorname{Hom}_\Lambda(R\Gamma_c(X,K),\Lambda).
\tag{11.7}
$$

If $X$ is proper, $R\Gamma_c$ may be replaced by
$R\Gamma$. The isomorphisms above and the pairing $\beta_K$ are
compatible with the change-of-coefficients maps of
Proposition [sk-prop-scalar-six].

*Complement.* If $X$ is proper, $K$ is locally perfect over $\Lambda_X$ and
$\Lambda=A_{E,n}=\mathcal O_E/\pi_E^n$, the degreewise form of (1) gives perfect
pairings

$$
\langle-,-\rangle_i:H_c^i(X,K)\times H^{2d-i}\bigl(X,K^\vee(d)\bigr)
\longrightarrow\Lambda\qquad(i\in\mathbf Z),
$$

because this ring is self-injective, so that $\operatorname{Hom}_\Lambda(-,\Lambda)$
is exact.
