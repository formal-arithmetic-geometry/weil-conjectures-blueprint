+++
id = "lem-fin-constructible-devissage"
kind = "lemma"
title = "Devissage of a constructible sheaf"
lean = ["AlgebraicGeometry.Etale.exists_filtration_isFiniteLocallyConstant"]
order = 2654
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-extension-by-zero", "lemma-weil-pbc-geometric-stalk-conservative", "sbc-def-coefficient-conventions"]
+++
Let $X$ be of finite type over $k$ and let $F$ be a
constructible
$\Lambda$-sheaf on $X_{{\mathrm{et}}}$. There is a finite filtration
by subsheaves

$$
0=F_0\subset F_1\subset\cdots\subset F_m=F
$$

and locally closed constructible subschemes
$j_r:X_r\hookrightarrow X$, with
lisse
$\Lambda$-sheaves $L_r$ on $(X_r)_{{\mathrm{et}}}$, such that

$$
F_r/F_{r-1}\cong(j_r)_!L_r\qquad(1\leq r\leq m).
$$

Here $(j_r)_!$ is the extension by zero of
[def-weil-pbc-extension-by-zero] along the locally closed
immersion. The filtration need not split.
