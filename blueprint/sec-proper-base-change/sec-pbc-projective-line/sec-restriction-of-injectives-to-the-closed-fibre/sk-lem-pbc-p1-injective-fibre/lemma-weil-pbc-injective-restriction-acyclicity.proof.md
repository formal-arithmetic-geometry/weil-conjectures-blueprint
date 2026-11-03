+++
kind  = "proof"
of    = "lemma-weil-pbc-injective-restriction-acyclicity"
+++
Induction on $n$. Let first $U\subseteq Y$ be an affine open, with closed fibre
$U_0=U\times_YY_0$, a closed subscheme of the affine scheme $U$. For every étale
$U'\to Y$ the restriction $I|_{U'}$ is an injective sheaf of $\Lambda$-modules
(restriction has the exact left adjoint extension by zero), so its underlying
abelian sheaf has no higher cohomology: $H^q(U',I|_{U'})=0$ for $q>0$. By the
second part of [prop-weil-pbc-gabber-affine-comparison], applied to the closed
immersion $U_0\hookrightarrow U$ and the torsion sheaf $I|_U$,
$H^q(U_0,I|_{U_0})$ is a filtered colimit of groups $H^q(U',I|_{U'})$ over étale
neighbourhoods $U'\to U$ of $U_0$, hence $H^q(U_0,I|_{U_0})=0$ for $q>0$. This is
the case $n=0$; it is the colimit form of the comparison that applies, since $U$
itself is not a henselian pair.

For the induction step write $Y=U\cup V$ with $U$ affine and $V$ covered by $n$
affine opens. The intersection $U\cap V$ is covered by $n$ affine opens (the
intersections of $U$ with those of $V$, affine because $Y$ is separated). The
restrictions of $I$ to the opens $V$ and $U\cap V$ are again injective torsion
sheaves of $\Lambda$-modules, and $V$, $U\cap V$ are separated and locally of
finite type over $A$, so the induction hypothesis gives vanishing on $V_0$ and
$(U\cap V)_0$ in degrees $>n-1$. The Mayer–Vietoris long exact sequence of the
closed fibre

$$
 \cdots\to H^{q-1}((U\cap V)_0,-)\to H^q(Y_0,-)\to H^q(U_0,-)\oplus H^q(V_0,-)
 \to\cdots
$$

then gives $H^q(Y_0,I|_{Y_0})=0$ for $q>n$.
