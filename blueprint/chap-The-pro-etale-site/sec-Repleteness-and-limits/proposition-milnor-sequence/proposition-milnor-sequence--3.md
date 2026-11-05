+++
id = "proposition-milnor-sequence--3"
kind = "proposition"
title = "The Milnor sequence (3)"
name_showing = false
order = 91005
aliases = ["bp-r024-3"]
lean = ["AlgebraicGeometry.ProEtale.milnor_epimorphic"]
+++
Let $\mathcal R$ be a sheaf of rings on $X_{\mathrm{pro}\acute{e}t}$ and
let $(M_n)$ be a countable tower of $\mathcal R$-modules whose
transitions $t_n:M_{n+1}\to M_n$ are epimorphisms. Then

$$
1-T:\prod_nM_n\longrightarrow\prod_nM_n
$$

is an epimorphism, and $H^1(\Cone(1-T)[-1])=0$. The canonical map

$$
(\varprojlim_nM_n)[0]\longrightarrow
R\varprojlim_nM_n=\Cone(1-T)[-1],
$$

given by the limit projections and the zero null-homotopy of their
composite with $1-T$, is an isomorphism in
$D(X_{\mathrm{pro}\acute{e}t},\mathcal R)$. Thus the derived limit is
the ordinary limit in degree zero.
