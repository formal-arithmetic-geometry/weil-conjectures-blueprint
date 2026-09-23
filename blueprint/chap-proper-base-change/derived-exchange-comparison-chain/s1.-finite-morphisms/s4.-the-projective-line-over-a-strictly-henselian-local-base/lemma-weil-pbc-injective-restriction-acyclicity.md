+++
id = "lemma-weil-pbc-injective-restriction-acyclicity"
kind = "lemma"
title = "Injective restriction acyclicity bound"
order = 1518
uses = ["prop-weil-pbc-gabber-affine-comparison"]
+++
Let a separated scheme with affine diagonal be covered by $n+1$ affine opens.
If $I$ is injective on the scheme over a henselian pair, then the restriction
to the closed fibre has vanishing cohomology in degrees $>n$.

## Proof

For $n=0$ this is the affine comparison applied to the injective $I$. For
$n>0$, split the cover as $U_0$ and $V=\bigcup_{i>0}U_i$. The Mayer–Vietoris
long exact sequence for $U_0\cup V$ has terms on $U_0$, $V$, and
$U_0\cap V$; the last two have covers of size at most $n$ and the affine
comparison kills their groups above the inductive bound. The long exact
sequence therefore kills the group above degree $n$. This is the dimension
induction located at Tag `0A51`.
