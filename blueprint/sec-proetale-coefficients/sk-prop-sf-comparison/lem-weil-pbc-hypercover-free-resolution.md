+++
id = "lem-weil-pbc-hypercover-free-resolution"
kind = "lemma"
title = "The augmented free complex of a hypercover"
order = 985
lean = ["AlgebraicGeometry.SplitEtaleHypercover.freeAbelian_augmentation_quasiIso", "AlgebraicGeometry.SplitEtaleHypercover.injective_abelian_section_cohomology", "AlgebraicGeometry.SplitEtaleHypercover.freeModule_augmentation_quasiIso", "AlgebraicGeometry.SplitEtaleHypercover.injective_module_section_cohomology"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-finite-split-hypercover"]
+++
Let $U\to X$ be a split etale hypercover
[def-weil-pbc-finite-split-hypercover]. Write $\mathbb Z[V]$ for the
sheafification of the free abelian presheaf on the sheaf represented by an
etale $X$-scheme $V$. Then the alternating-face augmented complex

$$
 \cdots\longrightarrow\mathbb Z[U_2]\longrightarrow
 \mathbb Z[U_1]\longrightarrow\mathbb Z[U_0]
 \longrightarrow\mathbb Z[X]\longrightarrow0
$$

is exact. For an injective abelian sheaf $I$, its complex of sections
consequently satisfies $H^0(C^\bullet(U,I))=I(X)$ and
$H^p(C^\bullet(U,I))=0$ for $p>0$. The same assertions hold with free modules
over a constant ring.
