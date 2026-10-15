+++
id = "det-curveestimate-canonical-mu"
kind = "proposition"
title = "Canonical $\\mu_n$-cohomology of a smooth proper curve"
uses = ["def-sc-kummer-sequence", "lem-sc-kummer-exact", "lem-sc-kummer-les", "lem-sc-brauer-zero", "det-thm-br-higher-vanishing", "lem-sc-pic-proper-decomposition", "thm-sc-jacobian-representability", "thm-av-final", "lem-sc-base-change-curve", "def-sc-field-extension"]
+++
Let $k$ be algebraically closed, $C$ a smooth proper connected curve of
genus $g$ over $k$, $n\geq1$ prime to $\operatorname{char}k$, and
$J=J_C$ its Jacobian, so that $J(k)=\operatorname{Pic}^0(C)$
([thm-sc-jacobian-representability]). Let
$\delta^1:\Gamma(C,\mathbf G_m)\to H^1(C,\mu_n)$ and
$\delta^2:\operatorname{Pic}(C)=H^1(C,\mathbf G_m)\to H^2(C,\mu_n)$ be the
boundary maps of the Kummer sequence ([def-sc-kummer-sequence]). Then:

1. $H^0(C_{\mathrm{ét}},\mu_n)=\mu_n(k)$.
2. The map $H^1(C_{\mathrm{ét}},\mu_n)\to\operatorname{Pic}(C)$ of the long
   exact sequence is injective with image $\operatorname{Pic}(C)[n]=J[n](k)$;
   this group has order $n^{2g}$.
3. $\delta^2$ is surjective and there is a unique isomorphism
   $\deg_n:H^2(C_{\mathrm{ét}},\mu_n)\xrightarrow{\sim}\Z/n$ with
   $\deg_n(\delta^2[L])=\deg L\bmod n$ for every line bundle $L$.
4. $H^q(C_{\mathrm{ét}},\mu_n)=0$ for $q>2$.
5. For an extension $k\subseteq k'$ of algebraically closed fields, the
   pullback maps $\rho^q_{k'/k}$ of [def-sc-field-extension] for $\mu_n$ are
   isomorphisms, and they correspond under 1–3 to the inclusion
   $\mu_n(k)\to\mu_n(k')$, the base-change map $J[n](k)\to J[n](k')$, and
   the identity of $\Z/n$.
