+++
kind = "proof"
of = "proposition-properties-trace--3"
order = 896007
uses = ["proposition-properties-trace--2"]
+++
Write $\phi_{Q,Q'}:F(Q)\otimes F(Q')\xrightarrow{\sim}F(Q\otimes Q')$ for the
monoidal structure of $F$ and $\beta$ for the braidings, so that
$F(\beta_{Q,Q'})\circ\phi_{Q,Q'}=\phi_{Q',Q}\circ\beta_{F(Q),F(Q')}$. Since $F$
is an additive functor, $a\mapsto F(a)$ is additive and multiplicative on
$\operatorname{End}(\mathbf 1_{\mathcal C})$ and preserves $1$, and conjugation
by $\phi_0$ preserves these properties. So $\rho_F$ is a ring map.

*The trace does not depend on the right dual.* Let $(P^\vee,\mathrm{ev},
\mathrm{coev})$ and $(Q,\mathrm{ev}_Q,\mathrm{coev}_Q)$ be right duals of $P$,
with $\mathrm{ev}:P^\vee\otimes P\to\mathbf 1$ and
$\mathrm{coev}:\mathbf 1\to P\otimes P^\vee$ as in
Definition [definition-categorical-trace--2]. The composite
$u:P^\vee\to P^\vee\otimes P\otimes Q\to Q$ of $1\otimes\mathrm{coev}_Q$ and
$\mathrm{ev}\otimes1$ (with the unit and associativity constraints) is an
isomorphism, and the triangle identities give
$\mathrm{ev}_Q\circ(u\otimes1_P)=\mathrm{ev}$ and
$(1_P\otimes u)\circ\mathrm{coev}=\mathrm{coev}_Q$. Using these and the
naturality of $\beta$,

$$
\mathrm{ev}_Q\circ\beta_{P,Q}\circ(v\otimes1_Q)\circ\mathrm{coev}_Q
=\mathrm{ev}_Q\circ\beta_{P,Q}\circ(1_P\otimes u)\circ(v\otimes1)\circ\mathrm{coev}
=\mathrm{ev}_Q\circ(u\otimes1_P)\circ\beta_{P,P^\vee}\circ(v\otimes1)\circ\mathrm{coev},
$$

which is the trace computed with $P^\vee$.

*Transport of the dual.* Put
$\mathrm{ev}'=\phi_0^{-1}\circ F(\mathrm{ev})\circ\phi_{P^\vee,P}$ and
$\mathrm{coev}'=\phi_{P,P^\vee}^{-1}\circ F(\mathrm{coev})\circ\phi_0$.
Applying $F$ to the two triangle identities of $(P,P^\vee)$ and using the
naturality of $\phi$ and its compatibility with the associativity and unit
constraints gives the triangle identities for $(\mathrm{ev}',\mathrm{coev}')$,
so $F(P^\vee)$ with these maps is a right dual of $F(P)$. With this dual, the
braided compatibility of $\phi$ and its naturality,
$\phi_{P,P^\vee}\circ(F(v)\otimes1)=F(v\otimes1)\circ\phi_{P,P^\vee}$, give

$$
\mathrm{ev}'\circ\beta_{F(P),F(P^\vee)}\circ(F(v)\otimes1)\circ\mathrm{coev}'
=\phi_0^{-1}\circ F\bigl(\mathrm{ev}\circ\beta_{P,P^\vee}\circ(v\otimes1)
\circ\mathrm{coev}\bigr)\circ\phi_0
=\rho_F(\operatorname{tr}(v\mid P)).
$$

By the previous paragraph, the left side is $\operatorname{tr}(F(v)\mid F(P))$
for any right dual of $F(P)$. By conjugacy invariance
(clause [proposition-properties-trace--2]) applied to $e$,
$\operatorname{tr}(v'\mid P')=\operatorname{tr}(F(v)\mid F(P))$, which proves
the formula.

*Scalar extension.* Let $A\to B$ be a ring map, and represent perfect
complexes by bounded complexes of finite projective modules, so that derived
tensor products are total tensor products. Then $F=-\otimes_AB$ is an additive
functor from perfect $A$-complexes to perfect $B$-complexes. The isomorphisms
$(M\otimes_AB)\otimes_B(N\otimes_AB)\to(M\otimes_AN)\otimes_AB$,
$(m\otimes b)\otimes(n\otimes b')\mapsto(m\otimes n)\otimes bb'$, and
$B\simeq A\otimes_AB$ make it strong monoidal. It is braided because both
symmetries carry the same Koszul sign $(-1)^{|m||n|}$. The endomorphism rings
of the units are $A$ and $B$, with $a$ acting by multiplication, and
$F(a)$ is multiplication by the image of $a$ in $B$, so $\rho_F$ is the given
map $A\to B$. Every perfect complex has the right dual $P^\vee$ of
Definition [definition-categorical-trace--1]. Taking $P'=F(P)$, $e=\mathrm{id}$ and
$v'=v\otimes_A^{\mathbf L}B$ gives the last assertion.

*Source:* the proof of Proposition [proposition-properties-trace].
