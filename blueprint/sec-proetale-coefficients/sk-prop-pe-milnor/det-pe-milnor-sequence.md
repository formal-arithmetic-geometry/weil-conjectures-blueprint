+++
id = "det-pe-milnor-sequence"
kind = "lemma"
title = "Cohomology of the sequential derived limit"
lean = ["DerivedCategory.shortExact_milnor_of_isHomotopyLimit", "DerivedCategory.isLE_of_isHomotopyLimit"]
order = 981
uses = ["det-pe-products-exact", "det-pe-products-derived"]
+++
Let $\mathcal C$ be an abelian category with K-injective resolutions in which countable
products exist and are exact (for instance the sheaves of $\Lambda$-modules on
$X_{\mathrm{proét}}$, by [det-pe-products-exact]). Let
$\cdots\to F_2\xrightarrow{t_1}F_1\xrightarrow{t_0}F_0$ be a tower in $D(\mathcal C)$, let
$T\colon\prod_nF_n\to\prod_nF_n$ be the map with components $\prod_mF_m\to F_{n+1}
\xrightarrow{t_n}F_n$, and let $R\varprojlim_nF_n$ be a homotopy limit of the tower: an object
with maps to the $F_n$ compatible with the $t_n$, whose induced map to $\prod_nF_n$ sits in a
distinguished triangle
$R\varprojlim_nF_n\to\prod_nF_n\xrightarrow{1-T}\prod_nF_n\to R\varprojlim_nF_n[1]$. (For a
tower of complexes one may take $\operatorname{Cone}(1-T)[-1]$, formed on complexes.) For a
tower $(M_n)$ in $\mathcal C$ write $R^1\varprojlim_nM_n=\coker(1-T\colon\prod_nM_n\to
\prod_nM_n)$.

1. For every $q$ there is a short exact sequence

   $$
   0\to\coker\Bigl(\prod_nH^{q-1}(F_n)\xrightarrow{1-T}\prod_nH^{q-1}(F_n)\Bigr)
   \to H^q\bigl(R\varprojlim_nF_n\bigr)\to\varprojlim_nH^q(F_n)\to0,
   $$

   whose second map is induced by the maps $R\varprojlim_nF_n\to F_n$.
2. For a tower $(M_n)$ in $\mathcal C$, viewed as complexes in degree $0$,
   $H^p(R\varprojlim_nM_n)$ is $\varprojlim_nM_n$ for $p=0$, $R^1\varprojlim_nM_n$ for
   $p=1$, and $0$ for $p\notin\{0,1\}$.
3. Consequently the sequence in 1 is the Milnor sequence
   $0\to R^1\varprojlim_nH^{q-1}(F_n)\to H^q(R\varprojlim_nF_n)\to\varprojlim_nH^q(F_n)\to0$.
