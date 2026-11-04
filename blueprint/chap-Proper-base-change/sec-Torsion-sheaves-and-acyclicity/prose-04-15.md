+++
id = "prose-04-15"
kind = "hidden"
title = "Torsion sheaves and acyclicity (4)"
order = 342
+++
From now until the end of Section [sec-Proper-morphisms], $\Lambda$ denotes a
commutative ring that is torsion as an abelian group, unless another ring
is specified. For such $\Lambda$ and proper $f$ we prove
$\mathrm{PBC}_\Lambda(f)$ in Propositions [proposition-proper-base-change-projective-line]
and [proposition-proper-base-change-etale-site]. Theorem [theorem-proper-base-change-classical-pro] then removes the
condition on $\Lambda$.

To pass from degree zero to higher degrees we apply the degree-zero
result to an injective resolution $F\to I^\bullet$ of a sheaf $F$ on
$X$. By
Proposition [proposition-proper-base-change-degree-zero]
the base change map is an isomorphism $g^*f_*I^m\simeq f'_*g'^*I^m$ in
each degree. The complex $g^*f_*I^\bullet$ computes $g^*Rf_*F$. The
complex $f'_*g'^*I^\bullet$, on the other hand, is $f'_*$ applied to a
resolution of $g'^*F$ that need not be injective, since $g'^*$ does not
preserve injectives. It still computes $Rf'_*g'^*F$ if every $g'^*I^m$
is $f'_*$-acyclic. We call this condition injective acyclicity, and
Theorem [theorem-pbc-injective-acyclicity] shows that it is
equivalent to proper base change. Unlike the base change statement,
injective acyclicity is a vanishing condition on single sheaves.
