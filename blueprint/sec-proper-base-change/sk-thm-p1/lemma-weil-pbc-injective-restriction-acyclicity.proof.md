+++
kind  = "proof"
of    = "lemma-weil-pbc-injective-restriction-acyclicity"
+++
Let $U\subseteq Y$ be an affine open, with closed fibre $U_0=U\times_YY_0$.
The restriction of $I$ to any etale $U'\to Y$ is an injective sheaf of
$\mathbf Z/n$-modules on $U'_{\Et}$, and such sheaves have no higher
cohomology, so $H^q(U',I|_{U'})=0$ for $q>0$. By the second
part of Gabber's affine comparison [prop-weil-pbc-gabber-affine-comparison],
applied to the affine $U$ over the henselian pair (for the torsion sheaf
$I|_U$, killed by $n$), $H^q(U_0,I|_{U_0})$ is the
colimit of the groups $H^q(U',I|_{U'})$ over the affine etale neighbourhoods
$U'\to U$ of $U_0$, hence $H^q(U_0,I|_{U_0})=0$ for $q>0$. This is the case
$n=0$; it is the colimit form of the comparison that applies, since $U$
itself is not a henselian pair and $H^q(U,I|_U)\to H^q(U_0,I|_{U_0})$ need not
be an isomorphism. For the induction step write $Y=U\cup V$ with $U$ affine and $V$
covered by $n$ affine opens; the intersection $U\cap V$ is affine because $Y$
is separated with affine diagonal, and the Mayer--Vietoris long exact sequence
of the closed fibre

$$
 \cdots\to H^q((U\cup V)_0,-)\to H^q(U_0,-)\oplus H^q(V_0,-)
 \to H^q((U\cap V)_0,-)\to\cdots
$$

together with the induction hypothesis for $V$ and for $U\cap V$ gives the
vanishing for $q>n$. The restriction of an injective sheaf of $\mathbf Z/n$-modules to an open
subscheme is again one, so the induction hypothesis
applies to $V$, to $U\cap V$ and to each chart separately.
