+++
id = "lem-fin-extension-by-zero"
kind = "lemma"
title = "Extension by zero preserves constructibility"
order = 5159
lean = ["AlgebraicGeometry.Etale.IsConstructible.extensionByZero"]
uses = ["sbc-def-coefficient-conventions"]
+++
Let $X$ be of finite type over $k$, let $j:U\hookrightarrow X$ be an open
immersion, and let $F$ be a constructible $\Lambda$-sheaf on $U_{\Et}$. Then
$j_!F$ is constructible on $X_{\Et}$.

## Proof

By the definition of constructibility $U$ has a finite partition
$U=\bigsqcup_\alpha U_\alpha$ into locally closed constructible subschemes
with $F|_{U_\alpha}$ lisse. The pieces $U_\alpha$ are locally closed
constructible subschemes of $X$ (locally closed in the open subscheme $U$),
and $X$ is the disjoint union of $X\setminus U$ and the $U_\alpha$. By the
stalk description of extension by zero, the restriction of $j_!F$ to
$U_\alpha$ is the lisse $F|_{U_\alpha}$ and its restriction to
$X\setminus U$ is the zero sheaf, which is lisse; this is the required
finite partition with lisse restrictions.

Unresolved dependencies: def:weil-pbc-constructible-complexes, def:weil-pbc-extension-by-zero, def:weil-pbc-scheme-conventions
