+++
id = "lem-kun-descent-limit"
kind = "lemma"
title = "A sheaf on an affine inverse limit is a colimit"
order = 1997
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions", "lem-kun-fp-algebra-descent"]
+++
Let $X=\varprojlim_iX_i$ be a directed inverse limit of affine schemes with
affine transition maps, and write $p_i:X\to X_i$. For every torsion abelian
sheaf $F$ on $X_{\Et}$, the sheaves $p_{i,*}F$, with their
canonical transition maps, form a compatible system and the canonical
morphism

$$
\varinjlim_ip_i^{-1}p_{i,*}F\longrightarrow F
$$

is an isomorphism.
