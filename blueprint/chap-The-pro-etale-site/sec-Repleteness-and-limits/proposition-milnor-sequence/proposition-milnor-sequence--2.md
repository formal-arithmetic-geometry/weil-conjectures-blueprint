+++
id = "proposition-milnor-sequence--2"
kind = "proposition"
title = "The Milnor sequence (2)"
name_showing = false
order = 91003
aliases = ["bp-r024-2"]
lean = ["AlgebraicGeometry.Scheme.ProEt.milnor_sequence", "DerivedCategory.shortExact_milnor_of_isHomotopyLimit"]
uses = ["definition-small-pro-etale-site--1"]
+++
Let $\mathcal R$ be a sheaf of rings on $X_{\mathrm{pro}\acute{e}t}$ and let $(K_n)$ be a
countable tower of complexes of $\mathcal R$-modules, with no boundedness
assumption. For each integer $q$ there are maps $a_K,b_K$, natural in maps
of towers, giving a short exact sequence

$$
0\longrightarrow
\coker\Bigl(\prod_nH^{q-1}(K_n)\xrightarrow{\,1-T\,}
\prod_nH^{q-1}(K_n)\Bigr)
\xrightarrow{\,a_K\,}H^q(\Cone(1-T)[-1])
\xrightarrow{\,b_K\,}\varprojlim_nH^q(K_n)
\longrightarrow0.
$$

Here the middle cone is formed on the termwise product of the $K_n$,
as in (2.1). Using the isomorphism $e_1$ of
clause [proposition-milnor-sequence--1] for the tower $(H^{q-1}(K_n))$ gives the short
exact sequence

$$
0\longrightarrow R^1\varprojlim_n H^{q-1}(K_n)
\xrightarrow{\,a_K\circ e_1\,} H^q(R\varprojlim_nK_n)
\xrightarrow{\,b_K\,} \varprojlim_n H^q(K_n)
\longrightarrow 0.
\tag{2.2}
$$

More generally, let $\mathcal A$ be an abelian category with exact
countable products in which every complex has a K-injective resolution.
Let $(F_n)$ be a tower in $D(\mathcal A)$ with transition maps
$t_n:F_{n+1}\to F_n$, and let $L$, with its maps $L\to F_n$, be a
homotopy limit of the tower, as in (2.1). Let $i$ be
an integer and put $j=i+1$. Let $P=\prod_nH^i(F_n)$, with the endomorphism
$T$ satisfying $\operatorname{pr}_nT=H^i(t_n)\operatorname{pr}_{n+1}$.
There is a short exact sequence in $\mathcal A$

$$
0\longrightarrow\coker(1-T:P\to P)
\longrightarrow H^j(L)\longrightarrow\varprojlim_nH^j(F_n)\longrightarrow0,
$$

whose right map is induced by the maps $L\to F_n$.
