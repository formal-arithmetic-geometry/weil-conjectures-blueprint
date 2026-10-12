+++
id = "lemma-nagata-partial-union-overlap-dense"
kind = "lemma"
title = "Density needed for induction on the affine cover"
order = 330
lean = ["Dense.preimage_val_inter"]
uses = ["def-nagata-partial-affine-unions", "lemma-nagata-dense-affine-cover"]
+++
Let $D$ be a dense subset of a topological space $X$, and let
$U,V\subseteq X$ be subsets with $D\subseteq U$, $D\subseteq V$ and
$U\cup V$ open. Then $U\cap V$ is dense in $U\cup V$. In particular, for
$r>1$ the overlap $X_{r-1}\cap U_r$ is dense in $X_r$, both $X_{r-1}$ and
$U_r$ containing the dense total intersection $D_X$ of the cover.
