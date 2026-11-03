+++
id = "lem-kun-base-change-open-closed"
kind = "lemma"
title = "Base change for open-closed immersions"
order = 3133
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-underived-exchange", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $j:U\to X$ be both an open and a closed immersion of schemes
and let $g:Y\to X$ be a morphism, forming the
cartesian square

$$
\begin{array}{ccc}
Y\times_XU&\xrightarrow{\;h\;}&Y\\
\Big\downarrow{\scriptstyle p}&&\Big\downarrow{\scriptstyle g}\\
U&\xrightarrow{\;j\;}&X .
\end{array}
$$

Then for every abelian sheaf $F$ on $U_{\Et}$ the base change map
$g^{-1}j_*F\to h_*p^{-1}F$ of
[def-weil-pbc-underived-exchange] is an isomorphism.
