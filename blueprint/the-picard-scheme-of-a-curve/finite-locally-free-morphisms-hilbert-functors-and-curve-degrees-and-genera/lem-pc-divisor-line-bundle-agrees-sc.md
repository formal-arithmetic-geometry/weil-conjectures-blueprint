+++
id = "lem-pc-divisor-line-bundle-agrees-sc"
kind = "lemma"
title = "O_X(D) agrees with the divisor module of the earlier chapter"
order = 4266
lean = ["AlgebraicGeometry.divisorLineBundle_eq_divisorSheaf"]
uses = ["def-pc-divisor-line-bundle", "def-pc-degree-line-bundle", "lem-pc-divisor-line-bundle-properties", "lem-pc-euler-additive", "lem-pc-degree-base-change"]
+++
Let $k$ be a field, $C$ a smooth curve [def-pc-curve] over $k$ and
$D=\sum_{i=1}^m n_i[P_i]$ a divisor of $C$ which is an effective Cartier
divisor (e.g. all $n_i\ge0$). Then $\mathcal{O}_C(D)$ of the divisor class
lemma of the divisors chapter (the sub-$\mathcal{O}_C$-module of $k(C)$)
and the module $\mathcal{O}_C(D)$ of [def-pc-divisor-line-bundle] are
canonically isomorphic; and for $D=[P]$ a $k$-rational point
$\deg(\mathcal{O}_C([P]))=1$ [def-pc-degree-line-bundle].

## Proof

It suffices to prove this for $D=[P]$ with $P$ a closed point: both
constructions are additive in $D$ (the divisor module of the earlier
chapter is $\mathcal{O}_C(D_1)\otimes\mathcal{O}_C(D_2)$ on the open dense
subscheme where the two divisors are supported away from each other —
equivalently
$\mathcal{O}_C(D_1+D_2)=\mathcal{O}_C(D_1)\otimes\mathcal{O}_C(D_2)$ — an
easy check from the definitions via $k(C)$, and the Cartier module by
[lem-pc-divisor-line-bundle-properties]); the constructions are compatible
after restriction to the cover of $C$ by the open sets
$U=C\setminus\{P_i\}$ and affine neighbourhoods of the $P_i$; the
isomorphism is local: on $U\ni P$ with $\mathcal{I}_P=(t)$ (a
non-zero-divisor, the ideal of the point on the smooth curve), the divisor
module $\{f\in k(C):\operatorname{div}f|_U+[P]\ge0\}$ is
$t^{-1}\mathcal{O}_C(U)$, the module $\mathcal{I}_P^\vee$ likewise maps
$\mathcal{I}_P=(t)$ to $\mathcal{O}_U$ isomorphically to
$t^{-1}\mathcal{O}_U$, and on $V=C\setminus\{P\}$ both are
$\mathcal{O}_C(V)$. This gives the canonical isomorphism.

For the degree: the exact sequence
$0\to\mathcal{O}_C\to\mathcal{O}_C([P])\to\kappa(P)\to0$ (the second map is
the inclusion of the inside of the dual of an invertible ideal, the
quotient is
$\mathcal{O}_C([P])|_P=\mathcal{H}om(\mathcal{I}_P,\mathcal{O}_C)\otimes\mathcal{O}_P=\kappa(P)$,
a $k$-vector space of dimension $1$ since $P$ is $k$-rational) together
with the additivity of $\chi$ [lem-pc-euler-additive] gives
$\chi(C,\mathcal{O}_C([P]))=\chi(C,\mathcal{O}_C)+1$, whence
$\deg(\mathcal{O}_C([P]))=\chi(\mathcal{O}_C([P]))-\chi(\mathcal{O}_C)=1$,
the value given by the degree of the earlier chapter of the class $[P]$;
for general $D$ the value follows by additivity of the degree on tensor
products [lem-pc-degree-base-change]. This proves the claim.

*Import note.* The source writes the local statement as "on $U\,$i$\,P$",
a place where a backslash was lost in the conversion; it is restored above
as $U\ni P$.

Unresolved dependencies: def:sc-divisor, lem:sc-divisor-class-curve, def:sc-pic0, lem:sc-point-cartier
