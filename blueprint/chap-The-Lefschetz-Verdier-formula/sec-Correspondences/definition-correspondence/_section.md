+++
id = "definition-correspondence"
kind = "definition"
title = "Correspondences"
order = 903
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.support", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence", "AlgebraicGeometry.Scheme.fixedScheme", "AlgebraicGeometry.Scheme.instIsClosedImmersionFixedSchemeιOfIsSeparated", "AlgebraicGeometry.Scheme.fixedSchemeι", "AlgebraicGeometry.Scheme.fixedSchemeProj"]
uses = ["definition-constructible-sheaves", "theorem-exceptional-inverse-image", "proposition-six-operations-dctf"]
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
