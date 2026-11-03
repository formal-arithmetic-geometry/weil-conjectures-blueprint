+++
kind = "proof"
of = "sk-lem-tf-rational-model"
uses = ["sk-thm-sfb-rationalization-comparison", "sk-lem-integral-models", "sk-prop-scalar-six"]
+++
By Proposition [sk-thm-sfb-rationalization-comparison], extension of
scalars induces an equivalence

$$
\Dbc(X,\mathcal O_E)[1/\ell]\simeq\Dbc(X,E),
$$

where the source has the objects of $\Dbc(X,\mathcal O_E)$ and Hom
groups tensored with $E$. By essential surjectivity, $K_E$ has an
integral model $K_0$. The model constructed there is built by finite
cones and shifts from the integral generators of
Lemma [sk-lem-integral-models](4), so in general it is not a lattice
in a lisse sheaf.

Since inverse image preserves integral constructibility,
$\Phi_X^*K_0$ is an integral model of $\Phi_X^*K_E$. By the description
of the Hom groups above, applied to the pair $(\Phi_X^*K_0,K_0)$, we may
write
$\psi_E=\pi_E^{-N}(\theta\otimes^{\mathbf L}_{\mathcal O_E}E)$. Since pullback is $\mathcal O_E$-linear,
each of the $m$ factors of the iterate contributes $\pi_E^{-N}$, and so
$(\psi_E)_m=\pi_E^{-Nm}(\theta_m\otimes^{\mathbf L} E)$.
By Proposition [sk-prop-scalar-six], the change-of-coefficients maps for
cohomology with compact support and for stalks respect the units of the
pullback adjunctions. Hence the pullback map $(\Phi_X^m)^*$ on $R\Gamma_c$ for $E$ is the extension
of scalars of the integral one. So is the identification
$((\Phi_X^m)^*K_E)_{\bar y}\simeq (K_E)_{\bar y}$ at a fixed point $\bar y$
of $\Phi_X^m$, because the comparison for inverse images is compatible
with composition and with extension of scalars. Applying $T_{c_m}$ and taking stalks at $\bar y$ in the formula for
$(\psi_E)_m$ gives (13.2).
