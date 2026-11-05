+++
id = "proposition-composition-open-restriction-compactifications-f--2"
kind = "proposition"
title = "Associativity of composition"
order = 530003
aliases = ["bp-r161-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl_assoc"]
uses = ["proposition-composition-open-restriction-compactifications-f--1"]
+++
For three composable morphisms $X\xrightarrow fY\xrightarrow gZ\xrightarrow hT$
of separated schemes of finite type over $k$ as in the shared context,
the specified composition comparisons of
[proposition-composition-open-restriction-compactifications-f--1] on
bounded constructible $\Qbarl$-complexes are associative.

More precisely, write $c_{f,g}:(gf)^!\xrightarrow\sim f^!g^!$.
For $K\in\Dbc(T_{\mathrm{pro}\acute{e}t},\Qbarl)$, after identifying
$h(gf)=(hg)f$, the composites
$$
(hgf)^!K\xrightarrow{c_{gf,h}}(gf)^!h^!K
  \xrightarrow{c_{f,g}}f^!g^!h^!K
$$
and
$$
(hgf)^!K\xrightarrow{c_{f,hg}}f^!(hg)^!K
  \xrightarrow{f^!c_{g,h}}f^!g^!h^!K
$$
agree.
