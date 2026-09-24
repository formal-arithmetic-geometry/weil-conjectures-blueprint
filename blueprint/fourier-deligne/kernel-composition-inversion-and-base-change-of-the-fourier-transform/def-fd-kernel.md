+++
id = "def-fd-kernel"
kind = "definition"
title = "The Fourier kernel and integrand"
order = 4149
uses = ["def-fd-artin-schreier-sheaf", "def-weil-pbc-qbar-category", "def-weil-pbc-scheme-conventions"]
+++
Let $S_0$ be a separated
scheme of finite type over $k_0$, let $V_0\to S_0$ be a vector
bundle of rank $r$ with dual $V_0^\vee$, and let
$b:V_0\times_{S_0}V_0^\vee\to S_0$ be the pairing. The
*Fourier kernel* is

$$
\mathcal K_\psi:=b^*\mathcal L_{\psi(b(x,\xi))}
$$

on $V_0\times_{S_0}V_0^\vee$. For $K\in D^b_c(V,E)$ (the
coefficient category of [def-weil-pbc-qbar-category]), the
*Fourier integrand* is

$$
\mathcal F_\psi(K):=p_{13,*}\bigl(p_{12}^*K\otimes^L_E\mathcal K_\psi\bigr)
$$

on $V\times_SV^\vee$, with $p_{12},p_{13}$ the projections.
