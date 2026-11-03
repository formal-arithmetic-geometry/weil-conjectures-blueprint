+++
kind  = "proof"
of    = "lem-pc-divisor-line-bundle-agrees-sc"
+++
*(1).* Every local ring $\mathcal{O}_{C,P}$ at a closed point is regular of
dimension one ([lem-sc-smooth-regular]), hence a discrete valuation ring
([lem-sc-regular-dim1-dvr]), and the ideal sheaf $\mathcal{I}_P$ of a
closed point is invertible ([lem-sc-point-cartier]). A product of
invertible ideal sheaves is invertible, and for invertible ideals
$\mathcal{I},\mathcal{J}$ multiplication
$\mathcal{I}\otimes\mathcal{J}\to\mathcal{I}\mathcal{J}$ is an isomorphism
(locally it sends $f\otimes g$ to $fg$ for local generators $f,g$, and $fg$
is again a non-zero-divisor). Hence
$[\mathcal{I}_E]=\prod_i[\mathcal{I}_{P_i}]^{n_i}$ in
$\operatorname{Pic}(C)$. Since the dual of an invertible module represents
the inverse class,

$$
[\mathcal{I}_E^\vee]=[\mathcal{I}_E]^{-1}=\prod_i[\mathcal{I}_{P_i}]^{-n_i}
=\prod_i[\mathcal{I}_{P_i}^\vee]^{n_i}=\prod_i[\mathcal{O}_C(P_i)]^{n_i},
$$

which is the class $[\mathcal{O}_C(E)]$ of [def-sc-divisor].

*(2).* By [lem-sc-cartier-divisor-points] the support of $D$ is a finite
set of closed points $P$, at which $\mathcal{I}_{D,P}=(t_P^{n_P})$ for a
uniformizer $t_P$ of the discrete valuation ring $\mathcal{O}_{C,P}$, with
$n_P=\operatorname{ord}_P(\mathcal{I}_D)\ge1$, and
$\mathcal{I}_{D,x}=\mathcal{O}_{C,x}$ at all other points. The ideal
$\mathcal{I}_E=\prod_P\mathcal{I}_P^{n_P}$ of $E=\sum_Pn_P[P]$ has the same
stalks, so $\mathcal{I}_D=\mathcal{I}_E$ (an ideal sheaf is determined by
its stalks), and (1) applies.
