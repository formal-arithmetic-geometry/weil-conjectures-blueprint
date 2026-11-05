+++
id = "definition-correspondence"
kind = "definition"
title = "Correspondences"
order = 904
lean = ["AlgebraicGeometry.Etale.CohomologicalCorrespondence", "AlgebraicGeometry.Etale.CohomologicalCorrespondence.fixedScheme", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus"]
uses = ["lemma-stability", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-composition-open-restriction-compactifications-f", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $X$ be a separated $k$-scheme of finite type. A *correspondence*
on $X$ is a morphism of $k$-schemes $c=(c_1,c_2):C\to X\times_sX$ from a
separated $k$-scheme of finite type (similarly over a base $S$). For $K\in D^b_{\mathrm{ctf}}(X,A)$, a
*cohomological correspondence* on $(X,K)$ is a morphism

$$
u:c_2^*K\longrightarrow c_1^!K.
$$

The *fixed locus* of $c$ is the closed subscheme

$$
\Fix(c)=C\times_{X\times X,\Delta_X}X,
\qquad i_c:\Fix(c)\longrightarrow C,\quad d_c:\Fix(c)\longrightarrow X,
$$

where $i_c$ and $d_c$ are the two projections.
