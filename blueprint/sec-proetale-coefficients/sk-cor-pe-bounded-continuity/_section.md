+++
id = "sk-cor-pe-bounded-continuity"
kind = "corollary"
title = "Bounded-below continuity"
order = 722
uses = ["sk-prop-pe-hypercover", "sk-cor-pe-sections", "sk-cor-pe-wc-sections"]
tags = ["sketch"]
+++
Suppose $U$ is quasi-compact and quasi-separated and $(K_i^\bullet)$ is a filtered diagram
of complexes of $\mathcal R$-modules vanishing below one fixed degree $a$. Then for every
$q$,

$$
\varinjlim_iH^q(U,K_i^\bullet)\simeq H^q\bigl(U,\varinjlim_iK_i^\bullet\bigr).
$$

If $f\colon X\to Y$ is quasi-compact and quasi-separated, the analogous map
$\varinjlim_iR^qf_*K_i^\bullet\to R^qf_*(\varinjlim_iK_i^\bullet)$ is an isomorphism of
sheaves on $Y_{\mathrm{proét}}$.

Complexes in degree zero give continuity of $H^q(U,-)$ for filtered colimits of module
sheaves, and hence for direct sums, which are filtered colimits of finite subsums. For
general complexes the common lower bound is needed.

**Complement.** The same statements hold, with the same proof, for any quasi-compact and
quasi-separated scheme $Y$ (taking $U=Y$) and any sheaf of rings $A$ on $Y_{\mathrm{proét}}$
in place of $\mathcal R$: for a filtered diagram $(K_i^\bullet)$ of complexes of $A$-modules,
termwise colimits, all vanishing in degrees below a fixed $a$, the map
$\varinjlim_iH^q(Y,K_i^\bullet)\to H^q(Y,\varinjlim_iK_i^\bullet)$ is an isomorphism for every
$q$, and for $g\colon Y\to Z$ quasi-compact and quasi-separated the map
$\varinjlim_iR^qg_*K_i^\bullet\to R^qg_*(\varinjlim_iK_i^\bullet)$ is an isomorphism of sheaves on
$Z_{\mathrm{proét}}$. In particular, for a quasi-compact quasi-separated scheme $Z$, each
$H^q(Z_{\mathrm{proét}},-)$ from sheaves of $A$-modules to abelian groups commutes with filtered
colimits and direct sums, and if $p\colon X\to Y$ is quasi-compact and quasi-separated, each
$R^qp_*$ on sheaves of $A$-modules on $X_{\mathrm{proét}}$ commutes with filtered colimits and
direct sums.
