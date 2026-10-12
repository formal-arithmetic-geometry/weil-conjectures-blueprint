+++
id = "def-weil-pbc-constructible-direct-image-finiteness"
kind = "definition"
title = "Constructible direct-image finiteness condition"
order = 1341
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-constructible-complexes", "def-weil-pbc-proetale-modules", "def-weil-pbc-site-comparison-morphism"]
+++
For the adic coefficient datum, write $\Lambda=P_n=A/I^n$, and assume $T$
noetherian of finite dimension with the orders of the torsion ring $P_n$
invertible on $T$. A sheaf $F$ of $\Lambda_{T,\Proet}$-modules on
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
