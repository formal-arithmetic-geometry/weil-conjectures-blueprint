+++
id = "sk-prop-pe-milnor"
kind = "proposition"
title = "The Milnor sequence"
order = 64
lean = ["DerivedCategory.shortExact_milnor_of_isHomotopyLimit", "DerivedCategory.isLE_of_isHomotopyLimit", "AlgebraicGeometry.ProEtale.isHomotopyLimit_mapCone_Q_of_epi", "CategoryTheory.GrothendieckTopology.epi_one_sub_of_forall_mittagLeffler"]
uses = ["sk-prop-pe-products", "sk-cor-pe-sections"]
tags = ["sketch"]
+++
For a countable tower of $\mathcal R$-modules, $R^p\varprojlim=0$
for $p>1$, and

$$
R^1\varprojlim_n M_n
=\coker\left(\prod_n M_n\xrightarrow{\,1-T\,}\prod_n M_n\right).
$$

For a tower $(K_n)$ of complexes there is a short exact sequence of
sheaves

$$
0\longrightarrow R^1\varprojlim_n H^{q-1}(K_n)
\longrightarrow H^q(R\varprojlim_nK_n)
\longrightarrow \varprojlim_n H^q(K_n)
\longrightarrow 0.
\tag{2.2}
$$

If the transitions of a tower of modules are epimorphisms, its derived
limit is its ordinary limit in degree zero.
