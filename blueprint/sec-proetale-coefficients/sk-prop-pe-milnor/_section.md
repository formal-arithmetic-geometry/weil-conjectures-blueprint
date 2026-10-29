+++
id = "sk-prop-pe-milnor"
kind = "proposition"
title = "The Milnor sequence"
order = 990
lean = ["DerivedCategory.shortExact_milnor_of_isHomotopyLimit", "DerivedCategory.isLE_of_isHomotopyLimit", "AlgebraicGeometry.ProEtale.isHomotopyLimit_mapCone_Q_of_epi", "CategoryTheory.GrothendieckTopology.epi_one_sub_of_forall_mittagLeffler"]
uses = ["sk-prop-pe-products", "sk-cor-pe-sections"]
tags = ["sketch"]
+++
For a countable tower write $t_n\colon M_{n+1}\to M_n$ and set
$T((m_n)_n)=(t_n(m_{n+1}))_n$. For a tower of complexes, represented by compatible
complexes, the derived inverse limit is the homotopy fibre

$$
R\varprojlim_nK_n=\operatorname{Cone}\Bigl(\prod_nK_n\xrightarrow{\,1-T\,}\prod_nK_n\Bigr)[-1].
$$

The cone is formed on the level of complexes, which makes the construction functorial in
the tower; it agrees with the derived inverse-limit functor on towers (Stacks, Tag 0940).

For a countable tower of $\mathcal R$-modules, $R^p\varprojlim=0$ for $p>1$, and

$$
R^1\varprojlim_nM_n=\coker\Bigl(\prod_nM_n\xrightarrow{\,1-T\,}\prod_nM_n\Bigr).
$$

For a tower $(K_n)$ of complexes there is a short exact sequence of sheaves

$$
0\longrightarrow R^1\varprojlim_nH^{q-1}(K_n)\longrightarrow H^q\bigl(R\varprojlim_nK_n\bigr)
\longrightarrow\varprojlim_nH^q(K_n)\longrightarrow0.
$$

If the transitions of a tower of modules are epimorphisms, its derived limit is its
ordinary limit in degree zero.

More generally, the $R^1\varprojlim$ term vanishes if, on every affine weakly contractible
$W$, the tower of section modules satisfies the Mittag–Leffler condition: evaluate the
cokernel formula and apply the Mittag–Leffler lemma for modules (Stacks, Tag 07KV). It
suffices to check the condition on this basis, because epimorphisms of sheaves induce
surjections on sections over weakly contractible objects.
