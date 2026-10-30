+++
id = "prose-E-09"
kind = "hidden"
title = "Verdier duality for nearby cycles"
order = 959
+++
The second factor of $K\boxtimes \mathbb DK$ is a Verdier dual. Hence,
to specialize the trace class of $K\boxtimes\mathbb DK$, we need that
nearby cycles commute with Verdier duality, by an explicit map
$\delta_{X,M}$ defined below (Ill, Theorem 4.2).

The trait $S$ and the coefficient ring $A$ are those of
Proposition [sk-prop-tf-nearby-external-kunneth], and
$\mathbb D_{X_{\bar\eta}}$ and $\mathbb D_{X_s}$ are the Verdier duals
relative to the geometric generic point $\bar\eta$ and the closed
point $s$ of $S$. We work on the classical étale site and transport
the result to the pro-étale site at the end.

We use the base change maps $\chi_f$, $\nu_f$, $\beta_f$, the lax monoidal
map $\mu_X$ and the map $\theta_X:\Psi_X\omega_{X_\eta}\to\omega_{X_s}$ of
the preceding subsection. Recall that $\beta_f$ is the adjoint, for $Rf_{s!}\dashv f_s^!$, of
(E.6) and that $\nu_f=\chi_f^{-1}$ for proper $f$.
For $M\in D^b_{\mathrm{ctf}}(X_\eta,A)$, define the morphism
$\delta_{X,M}:\Psi_X\mathbb D_{X_\eta}M\to\mathbb D_{X_s}(\Psi_XM)$
as the tensor–Hom adjoint of the pairing

$$
\Psi_XM\otimes \Psi_X\mathbb D_{X_\eta}M
\xrightarrow{\mu_X}\Psi_X(M\otimes \mathbb D_{X_\eta}M)
\xrightarrow{\Psi_X\operatorname{ev}}\Psi_X\omega_{X_\eta}
\xrightarrow{\theta_X}\omega_{X_s}.
\tag{E.13}
$$
