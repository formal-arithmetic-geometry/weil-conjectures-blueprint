+++
id = "sk-lem-nagata-density-normalization"
kind = "lemma"
title = "Passing to the schematic closure"
order = 4
uses = ["sk-def-nagata-sketch-data", "sk-lem-nagata-sketch-closure", "sk-prop-sf-open-closed-triangle"]
tags = ["sketch"]
+++
Let $X\xrightarrow{j}\overline X\xrightarrow{p}S$ be any compactification
([sk-def-nagata-sketch-data]) with $\overline X$ Noetherian, and let
$i:Z\hookrightarrow\overline X$ be the schematic closure of $X$, with
$j_Z:X\hookrightarrow Z$ the induced open immersion
([sk-lem-nagata-sketch-closure]). For a condensed coefficient ring
$\Lambda$, use its pulled-back coefficient sheaves on these schemes. For
every $K\in D(X_{\mathrm{pro\acute{e}t}},\Lambda_X)$ there are canonical
identifications, in $D(\overline X_{\mathrm{pro\acute{e}t}},\Lambda_{\overline X})$
and $D(S_{\mathrm{pro\acute{e}t}},\Lambda_S)$ respectively,

$$
j_!K\simeq i_*j_{Z,!}K,\qquad
Rp_*j_!K\simeq R(p\circ i)_*j_{Z,!}K.
$$

Thus, for schemes of finite type over $k$, replacing a compactification by
the schematic closure of $X$ does not change the expression $Rp_*j_!$
defining $Rf_!$; that expression needs only an open immersion followed by a
proper morphism.
