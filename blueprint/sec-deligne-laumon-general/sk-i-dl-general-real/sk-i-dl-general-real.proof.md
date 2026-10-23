+++
kind  = "proof"
of    = "sk-i-dl-general-real"
+++
First suppose that $X_0$ is smooth, geometrically connected and
affine, and that the sheaf $G$ is lisse. Make the constant extension of
[sk-lem-wgen-geometric-constituents] and write $S_1,\ldots,S_r$
for the quotients of its Weil filtration. The sheaf $G$ remains real
after this extension, since the powers of a conjugation-stable
multiset of eigenvalues again form a conjugation-stable multiset.

Fix a closed point $x_*$ of $X_0$, and let $x$ be any other closed
point. By [sk-cor-wgen-bertini-irreducible], there is a curve
through chosen geometric points above $x_*$ and $x$ on which every
$S_j$ remains irreducible. The restriction of $G$ to this curve is
real, and so each restricted $S_j$ is pure by
[sk-p-real-purity]. Let $\alpha$ be an eigenvalue of $S_j$
at $x_*$. If the point of the curve above $x_*$ has residue degree
$e$, the corresponding eigenvalue there is $\alpha^e$ and the residue
cardinality is $q_{x_*}^e$. Thus the weight of the restriction of
$S_j$ must be

$$
 w_j=2\log_{q_{x_*}}|\iota(\alpha)|,
$$

which does not depend on the curve, and all eigenvalues of $S_j$ at
$x_*$ have this modulus. The same calculation with powers at $x$ shows
that $S_j$ is pure of weight $w_j$ at $x$. Thus each $S_j$ is pure of
weight $w_j$ on $X_0$, and the chosen Weil filtration shows that $G$
is mixed.

Mixedness descends along the finite constant extension
$g:X'_0\to X_0$ made at the start. We push the mixed filtration
forward using [sk-l-dl-general-quasifinite]. The unit
$G\to g_*g^*G$ has the Weil-equivariant retraction
$(\deg g)^{-1}\operatorname{Tr}$. Indeed, étale locally the unit is
the diagonal and the trace is the sum over the copies, and these local
maps glue because the sum is invariant under permutations of the
copies. By [sk-r-real-linear], a Weil subobject of a
mixed sheaf is mixed, and applying this to the unit we obtain the
assertion on $X_0$.

Now let $G$ be an arbitrary constructible real sheaf. Since nilpotents
do not change the category of sheaves ([sk-i-topology]), we may work on
the geometric reduction. In each irreducible component, choose a dense
smooth affine open on which $G$ is lisse and which avoids the other
components; the complement has smaller dimension. Iterating, we obtain
a finite chain of closed subschemes whose differences are disjoint
unions of smooth connected affine pieces on which $G$ is lisse. After
one finite constant extension, the pieces and their geometric
components are all defined. The preceding argument applies to the
positive-dimensional pieces, and at a zero-dimensional piece a
Frobenius-stable Jordan flag has pure quotients of rank one.

For an open piece $j$ with closed complement $i$, the exact sequence
([sk-prop-sf-open-closed-triangle])

$$
 0\longrightarrow j_!j^*G\longrightarrow G
   \longrightarrow i_*i^*G\longrightarrow0
$$

splices the two filtrations, because $j_!$ and $i_*$ are exact and
preserve pure weights. Applying this successively along the chain of
closed subschemes, we obtain a finite filtration by Weil subsheaves
with pure quotients, and the trace retraction descends mixedness to
the original field.
