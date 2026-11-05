+++
id = "lemma-finite-morphisms--3"
kind = "lemma"
title = "Finite morphisms (3)"
name_showing = false
order = 384003
aliases = ["bp-r116-3"]
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_of_isFinite"]
uses = ["lemma-finite-morphisms--2", "definition-derived-base-change-map"]
+++
Let $u:V\to W$ be finite and let $A$ satisfy the coefficient assumptions of
[lemma-finite-morphisms--2], with the forgetful functor carrying $A$-valued
sheaves on $Z_{\acute{e}t}$ to sheaves of sets for every scheme $Z$.
For every base change $g:W'\to W$, with $u'$ and $g'$ as above, the derived
base change map [definition-derived-base-change-map]

$$
g^*Ru_*K\longrightarrow Ru'_*g'^*K
$$

is an isomorphism for every $K\in D^+(V_{\acute{e}t},A)$.
In particular, this holds for every constant coefficient ring $\Lambda$
and every $K\in D^+(V_{\acute{e}t},\Lambda)$, without a torsion hypothesis.
