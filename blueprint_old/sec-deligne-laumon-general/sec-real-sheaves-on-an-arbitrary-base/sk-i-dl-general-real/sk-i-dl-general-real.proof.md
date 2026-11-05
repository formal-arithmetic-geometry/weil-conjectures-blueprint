+++
kind = "proof"
of = "sk-i-dl-general-real"
+++
We join a fixed point $x_*$ to an arbitrary point $x$ by a
curve on which the geometrically irreducible constituents stay
irreducible. On that curve each constituent is pure by
Theorem [sk-p-real-purity], and its weight is read off at $x_*$, so
it does not depend on the curve. We first treat a lisse sheaf on a
smooth affine scheme in this way, and then pass to an arbitrary
constructible sheaf by stratifying.

*The lisse case.* Suppose that $X_0$ is smooth, geometrically
connected and affine, and that the sheaf $G$ is lisse. Make the
constant extension of
Lemma [sk-lem-wgen-geometric-constituents] and write $S_1,\ldots,S_r$
for the quotients of its Weil filtration. The sheaf $G$ remains real
after this extension, since the powers of a conjugation-stable
multiset of eigenvalues again form a conjugation-stable multiset.

Fix a closed point $x_*$ of $X_0$, and let $x$ be any other closed
point. By Corollary [sk-cor-wgen-bertini-irreducible], there is a curve
through chosen geometric points above $x_*$ and $x$ on which every
$S_j$ remains irreducible. The restriction of $G$ to this curve is
real, and so each restricted $S_j$ is pure by
Theorem [sk-p-real-purity]. Let $\alpha$ be an eigenvalue of $S_j$
at $x_*$. If the point of the curve above $x_*$ has residue degree
$e$, the corresponding eigenvalue there is $\alpha^e$ and the residue
cardinality is $q_{x_*}^e$. Hence the weight of the restriction of
$S_j$ must be

$$
w_j=2\log_{q_{x_*}}|\iota(\alpha)|,
$$

which does not depend on the curve, and all eigenvalues of $S_j$ at
$x_*$ have this modulus. The same calculation with powers at $x$ shows
that $S_j$ is pure of weight $w_j$ at $x$. As $x$ was arbitrary, each
$S_j$ is pure of weight $w_j$ on $X_0$, and the chosen Weil filtration
shows that $G$ is mixed.

*Descent along the constant extension.* Let $g:X'_0\to X_0$ be
the finite constant extension made at the start. Since $g^*G$ is mixed,
so is $g_*g^*G$ by Lemma [sk-l-dl-general-quasifinite]. The unit
$G\to g_*g^*G$ has the Weil-equivariant retraction
$(\deg g)^{-1}\operatorname{Tr}$. Indeed, étale locally the unit is
the diagonal and the trace is the sum over the copies, and these local
maps glue because the sum is invariant under permutations of the
copies. Hence $G$ is a Weil subsheaf of $g_*g^*G$, and it is mixed by
Proposition [sk-r-real-linear], since a Weil subobject of a mixed
sheaf is mixed.

*The general case.* Now let $G$ be an arbitrary constructible
real sheaf. Since nilpotents
do not change the étale site, we may assume that $X_0$ is reduced. In each irreducible component, choose a dense smooth affine
open on which $G$ is lisse and which avoids the other components. The
complement has smaller dimension. Iterating, we obtain a finite chain
of closed subschemes whose differences are disjoint unions of smooth
connected affine pieces on which $G$ is lisse. After one finite
constant extension, the pieces and their geometric components are all
defined. The preceding argument applies to the positive-dimensional
pieces, and at a zero-dimensional piece a Frobenius-stable Jordan
flag has pure quotients of rank one.

Let $j$ be the inclusion of an open piece and $i$ that of its closed
complement. Since $j_!$ and $i_*$ are exact and preserve pure weights
(Lemma [sk-l-dl-general-quasifinite]), the exact sequence

$$
0\longrightarrow j_!j^*G\longrightarrow G
\longrightarrow i_*i^*G\longrightarrow0
$$

lets us splice the filtrations of $j^*G$ and $i^*G$ into one of $G$
with pure quotients. Applying this successively along the chain of
closed subschemes, we obtain a finite filtration by Weil subsheaves
with pure quotients. Finally, the retraction $(\deg g)^{-1}\operatorname{Tr}$ descends mixedness
to the original field, as in the lisse case.
