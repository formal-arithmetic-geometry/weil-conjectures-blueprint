+++
id = "det-sf-flat-model-generation"
kind = "lemma"
title = "Strata of a flat constructible sheaf and generation by $a_!L$"
uses = ["lem-sf-flat-model"]
+++
Let $A$ be a finite commutative ring and $X$ a Noetherian scheme (for
instance of finite type over the standing field), on the étale or the
pro-étale site.

1. If $F$ is a flat constructible sheaf of $A$-modules on $X$, there is a
finite partition $X=\bigsqcup_{k=1}^mS_k$ into locally closed subschemes,
ordered so that $X_{\ge k}=\bigcup_{k'\ge k}S_{k'}$ is closed and $S_k$ is open in
$X_{\ge k}$, such that each $F|_{S_k}$ is locally constant with stalks finite
projective $A$-modules.
2. For such a partition, with $a_k:S_k\hookrightarrow X$ the inclusions and
$L_k=F|_{S_k}$, $F$ is an iterated extension of the sheaves $a_{k!}L_k$; each
$a_{k!}L_k$ is flat constructible and lies in $\Dctf(X,A)$.
3. $\Dctf(X,A)$ is the smallest full subcategory of $D(X,A)$ containing the
objects $a_!L$ ($a:S\hookrightarrow X$ locally closed, $L$ locally constant
with finite projective stalks) and closed under shifts, extensions (cones)
and direct summands.
