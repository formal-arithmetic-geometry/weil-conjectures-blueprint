+++
id = "def-weil-pbc-constructible-direct-image-finiteness"
kind = "definition"
title = "Constructible direct-image finiteness condition"
order = 2186
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-proetale-modules", "def-weil-pbc-site-comparison-morphism"]
+++
Let $\Lambda$ be a finite torsion ring, for example
$A_{E,n}=\mathcal O_E/\pi_E^n$ or $\mathbf Z/\ell^n\mathbf Z$, and assume $T$
noetherian of finite dimension with the order of $\Lambda$ invertible on $T$. A sheaf $F$ of $\Lambda_{T,\Proet}$-modules on
$T_{\Proet}$ is *constructible* if $F\cong\nu_T^*F_{\Et}$ for the comparison
morphism of sites [def-weil-pbc-site-comparison-morphism]
$\nu_T:T_{\Proet}\to T_{\Et}$ and a constructible $\Lambda$-module sheaf
$F_{\Et}$ on $T_{\Et}$. For a morphism $u:S\to T$, write
$\mathrm{FIN}(u,\Lambda;c)$ if:

1. *constructibility of direct images:* for every constructible sheaf $F$ of
   $\Lambda_{S,\Proet}$-modules on $S_{\Proet}$ and every $q\geq0$, the
   sheaf $R^qu_*F$ on $T_{\Proet}$ is constructible;
2. *amplitude:* there is an integer $c\in\mathbf Z_{\geq0}$ such that
   $R^qu_*F=0$ for every $q>c$ and every constructible sheaf $F$ of
   $\Lambda_{S,\Proet}$-modules on $S_{\Proet}$.
