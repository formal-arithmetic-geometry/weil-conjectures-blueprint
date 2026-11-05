+++
id = "lemma-simple-objects--2"
kind = "lemma"
title = "The exact sequence criterion for simplicity"
name_showing = false
order = 1255002
aliases = ["bp-r388-2"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isZero_or_isZero_of_exact"]
uses = ["definition-punctual-sheaf", "definition-lisse-sheaves", "definition-weil-structure"]
+++
The separate assertion that middle extensions have no nonzero punctual
subobject or quotient in the perverse heart is bypassed by the Lean
proof of simplicity, which uses the following criterion for ordinary
Weil sheaves.

Let $j:U_0\hookrightarrow\Aone_{\Fq}$ be a dense open immersion,
let $\ell\ne\operatorname{char}\Fq$, and let $N$ be a nonzero
irreducible lisse Weil $\Qbarl$-sheaf on $U_0$. Suppose that

$$
0\longrightarrow A\xrightarrow{a}M\xrightarrow{s}B
\xrightarrow{t}C\longrightarrow0
$$

is an exact sequence of Weil $\Qbarl$-sheaves on $\Aone_{\Fq}$,
that $M\simeq j_*N$, that $C$ is punctual, and that $B$ has no
nonzero punctual subsheaf. Then either $A=C=0$ or $B=0$.
