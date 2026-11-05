+++
id = "proposition-milnor-sequence--2"
kind = "proposition"
title = "The Milnor sequence (2)"
name_showing = false
order = 91002
aliases = ["bp-r024-2"]
lean = ["AlgebraicGeometry.Scheme.ProEt.milnor_sequence", "DerivedCategory.shortExact_milnor_of_isHomotopyLimit"]
uses = ["definition-small-pro-etale-site", "prose-02-23", "proposition-milnor-sequence--1"]
+++
Let $\mathcal R$ be a sheaf of rings on $X_{\mathrm{pro}\acute{e}t}$ and
let $(K_n)$ be a countable tower of complexes of $\mathcal R$-modules,
with no boundedness assumption. For each integer $q$ there are maps
$a_K,b_K$, natural in maps of towers, giving a short exact sequence

$$
0\longrightarrow
\coker\left(\prod_nH^{q-1}(K_n)\xrightarrow{\,1-T\,}
\prod_nH^{q-1}(K_n)\right)
\xrightarrow{\,a_K\,}H^q(\Cone(1-T)[-1])
\xrightarrow{\,b_K\,}\varprojlim_nH^q(K_n)
\longrightarrow0.
$$

Here the middle cone is formed on the termwise product of the $K_n$,
as in (2.1). Using the isomorphism $e_1$ of
[proposition-milnor-sequence--1] for the tower $(H^{q-1}(K_n))$ gives
the short exact sequence

$$
0\longrightarrow R^1\varprojlim_n H^{q-1}(K_n)
\xrightarrow{\,a_K\circ e_1\,} H^q(R\varprojlim_nK_n)
\xrightarrow{\,b_K\,} \varprojlim_n H^q(K_n)
\longrightarrow 0.
\tag{2.2}
$$

More generally, let $\mathcal A$ be an abelian category with a derived
category, K-injective resolutions, and exact countable products. Let
$(F_n)$ be a tower in $D(\mathcal A)$ and let $L\to F_n$ be a homotopy
limit cone. For integers $i,j$ with $i+1=j$, choose a product
$P=\prod_nH^i(F_n)$, an endomorphism $T$ satisfying
$\operatorname{pr}_nT=H^i(t_n)\operatorname{pr}_{n+1}$, and a limit
$D=\varprojlim_nH^j(F_n)$. There is a short exact sequence in
$\mathcal A$

$$
0\longrightarrow\coker(1-T:P\to P)
\longrightarrow H^j(L)\longrightarrow D\longrightarrow0,
$$

whose right map is induced by the homotopy limit cone.
