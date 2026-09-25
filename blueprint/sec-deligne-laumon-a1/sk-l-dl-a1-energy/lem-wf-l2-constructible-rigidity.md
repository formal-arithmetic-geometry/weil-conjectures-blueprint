+++
id = "lem-wf-l2-constructible-rigidity"
kind = "lemma"
title = "The $L^2$-weight of a sheaf without punctual sections"
order = 3022
uses = ["def-weil-ordinary-compact-cohomology", "def-weil-pbc-constructible-complexes", "def-weil-punctual-weights", "def-wf-l2-norm", "def-wf-middle-extension", "lem-fd-l2-mixed-lisse", "lem-wf-boundary-semicontinuity"]
+++
Let $X_0$ be a smooth geometrically connected affine curve and let
$\mathcal G\neq0$ be a
constructible
Weil sheaf with a finite filtration having punctually pure graded
pieces. Suppose
$\hyperref[def:weil-ordinary-compact-cohomology]{H_c^0} (X,\mathcal G)=0$.
Let $W$ be the maximum weight occurring in the nonzero restrictions
of those pieces to a common dense lisse open.
Then every closed-point eigenvalue of $\mathcal G$ has weight at
most $W$, and $\|\mathcal G\|=W$ in
[def-wf-l2-norm].

## Proof

Choose a dense open $j:U_0\hookrightarrow X_0$ on which the
finitely many sheaves in the filtration are lisse.
The kernel of the adjunction
$\mathcal G\to j_*j^*\mathcal G$, with ordinary direct image as in
[def-wf-middle-extension], is supported on the finite complement.
After geometric base change, a nonzero such sheaf has a nonzero
compactly supported global section, namely any nonzero vector at one
of its finitely many support points. Its inclusion in $\mathcal G$
would contradict the assumed vanishing in
[def-weil-ordinary-compact-cohomology]. Thus the adjunction is
injective. In particular $j^*\mathcal G\neq0$.

The restricted pure filtration and [lem-fd-l2-mixed-lisse]
give $\|j^*\mathcal G\|=W$.
The local eigenvalues on $U_0$ have weights at most $W$, by
[def-weil-punctual-weights]. Boundary semicontinuity
[lem-wf-boundary-semicontinuity] gives the same bound for
$j_*j^*\mathcal G$, hence for its subsheaf $\mathcal G$.
If $D$ bounds the number of geometric boundary points and $r$
bounds the stalk ranks, their squared trace contribution is at most
$Dr^2q^{mW}$. The square sums for $\mathcal G$ and its open
restriction therefore differ by a nonnegative term bounded by that
quantity. For every $b>W$, division by $q^{m(b+1)}$ makes this
term tend to zero, as does the open contribution.
The reverse inequality follows because the whole square sum
dominates its open part. By [def-wf-l2-norm],
$\|\mathcal G\|=W$.
