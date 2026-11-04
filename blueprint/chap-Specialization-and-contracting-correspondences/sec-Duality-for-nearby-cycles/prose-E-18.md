+++
id = "prose-E-18"
kind = "hidden"
title = "Duality for nearby cycles (1)"
order = 1664
+++
Since the second factor of $K\boxtimes \mathbb DK$ is a Verdier dual,
specializing a trace class also requires nearby cycles to commute with
Verdier duality, by an explicit map $\delta_{X,M}$ defined below
[illusie94, Theorem 4.2].

The trait $S$ and the coefficient ring $A$ are those of
Proposition [proposition-external-kunneth-formula-nearby-cycles], and
$\mathbb D_{X_{\bar\eta}}$ and $\mathbb D_{X_s}$ are the Verdier duals
relative to the geometric generic point $\bar\eta$ and the closed
point $s$ of $S$. We work on the classical étale site and transport
the result to the pro-étale site at the end.

We use the base change maps $\chi_f$, $\nu_f$, $\beta_f$, the lax monoidal
map $\mu_X$ and the map $\theta_X:\Psi_X\omega_{X_\eta}\to\omega_{X_s}$ of
the preceding subsection.  Recall that $\beta_f$ is the adjoint, for $Rf_{s!}\dashv f_s^!$, of
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
