+++
id = "lemma-nagata-partial-union-overlap-dense"
kind = "lemma"
title = "Density needed for induction on the affine cover"
order = 323
lean = ["Dense.preimage_val_inter"]
uses = ["def-nagata-partial-affine-unions", "lemma-nagata-dense-affine-cover"]
+++
Let $D$ be a dense subset of a topological space $X$, and let
$U,V\subseteq X$ be subsets with $D\subseteq U$, $D\subseteq V$ and
$U\cup V$ open. Then $U\cap V$ is dense in $U\cup V$. In particular, for
$r>1$ the overlap $X_{r-1}\cap U_r$ is dense in $X_r$, both $X_{r-1}$ and
$U_r$ containing the dense total intersection $D_X$ of the cover.

## Proof

The overlap $U\cap V$ contains $D$, and $D\subseteq U\cup V$. A dense subset
of $X$ contained in an open subset $O$ is dense in $O$: every nonempty open
subset of $O$ is open in $X$, hence meets $D$. Applied to $O=U\cup V$, this
shows that $D$ is dense in $U\cup V$, and therefore so is the larger subset
$U\cap V$. For the last assertion take $D=D_X$, $U=X_{r-1}$, $V=U_r$, so
that $U\cup V=X_r$ is open in $X$.
