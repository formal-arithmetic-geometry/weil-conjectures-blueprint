+++
kind  = "proof"
of    = "thm-pur-localized-top-chern"
+++
The line-bundle class in the proposed construction is the divisor class of [lem-pur-divisor-class]; products have their twists identified by [def-coefficient-twists-detailed].
Step 1: the flag-bundle pullback is injective. Write the group in
the form

$$
H^{2r}_{Z(s)}(T,\Lambda(r))
:=\operatorname{Hom}_{D(T,\Lambda)}
\bigl(i_*\Lambda_{Z(s)},\Lambda_T(r)[2r]\bigr).
$$

Pull $F$ back to its complete flag bundle $p:T'\to T$. Iterating
[thm-pur-projective-bundle-formula] gives a direct-sum
decomposition of $Rp_*\Lambda_{T'}$ whose degree-zero summand is
$\Lambda_T$; projection to this summand with the projection formula
is a left inverse to

$$
p^*:H^{2r}_{Z(s)}(T,\Lambda(r))
\longrightarrow
H^{2r}_{Z(s)\times_TT'}(T',\Lambda(r)),
$$

so this pullback is injective: the ordinary splitting principle for the
displayed abelian group.

Step 2: the class on the flag bundle. On $T'$ the flag quotients are
line bundles; successively take the localized Kummer classes of the
induced line-bundle sections on their successive zero loci and cup them,
obtaining an element
$\operatorname{cl}_{T'}\in H^{2r}_{Z(s)\times_TT'}(T',\Lambda(r))$.
The result is unchanged under a refinement of the flag: after forgetting
support each factor is $-c_1$ of its line quotient (the section of the
quotient $L_i$ vanishes exactly on a divisor $D_i$ with
$\mathcal O(D_i)\cong L_i$, and [lem-pur-divisor-class](b) applies), and
expanding the product and using the additivity of
[lem-pur-kummer-additivity]
($c_1(L\otimes M)=c_1(L)+c_1(M)$) shows that it is the symmetric
elementary polynomial of degree $r$ in the negated Chern roots
$-x_1,\dots,-x_r$.

Step 3: the class descends, by gluing in the universal case and pulling
back. Supported classes do not glue over an open cover in general: the
presheaf $U\mapsto H^{2r}_{Z\cap U}(U,\Lambda(r))$ is a sheaf only when
the local cohomology sheaves of $\Lambda$ along $Z$ vanish in degrees
below $2r$. So the gluing is done where this vanishing is known, namely
for the zero section of a vector bundle, and the general class is obtained
from it by pullback.

*The universal case.* Let $\pi:E\to T$ be the vector bundle of
[def-pur-vector-bundle-zero-section] whose sections are the sections of
$F$, with zero section $z$; the tautological section $\tau$ of $\pi^*F$
has zero scheme $z(T)$. For an open $U\subseteq T$ write
$E_U=\pi^{-1}(U)$. By the localization triangle of
[lem-pur-support-localization-triangle] (and its compatibility with
restriction to opens),
$H^q_{z(U)}(E_U,\Lambda(r))=H^q(U,Rz^!\Lambda_E(r))$. Over an open $T_0$
on which $F$ is trivial, $E_{T_0}\cong\mathbf A^r_{T_0}$ with $z$ the
zero section, and [cor-pur-affine-space-zero-section-purity] gives
$Rz^!\Lambda_E\cong\Lambda_{T_0}(-r)[-2r]$ there. Hence the cohomology
sheaves $\mathcal H^q(Rz^!\Lambda_E(r))$ vanish for $q<2r$ (the vanishing
is local on $T$), and

$$
H^{2r}_{z(U)}\bigl(E_U,\Lambda(r)\bigr)
=\Gamma\bigl(U,\mathcal H^{2r}(Rz^!\Lambda_E(r))\bigr)
$$

for every open $U\subseteq T$. Thus $U\mapsto H^{2r}_{z(U)}(E_U,\Lambda(r))$
is a sheaf on $T$, and classes given on the members of an open cover that
agree on the overlaps glue to a unique class. Now choose a trivialization
of $F|_{T_0}$, with linear coordinates $t_1,\dots,t_r$ on
$E_{T_0}\cong\mathbf A^r_{T_0}$. The pair
$(E_{T_0},z(T_0))$ is in the setting of [def-pur-frame-class] over the
base $T_0$, and $t_1,\dots,t_r$ is a frame of the ideal of $z(T_0)$, so put

$$
u_F|_{T_0}=\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_r)
\in H^{2r}_{z(T_0)}\bigl(E_{T_0},\Lambda(r)\bigr).
$$

A second trivialization changes the coordinates by an invertible matrix,
so by [lem-pur-frame-independence] this class depends only on the ideal
of the zero section, hence only on $T_0$; in particular the classes on two
trivializing opens agree on their intersection. By the sheaf property they
glue to a unique class $u_F\in H^{2r}_{z(T)}(E,\Lambda(r))$.

*The general case.* The section $s$ is a morphism $\sigma_s:T\to E$ with
$\pi\sigma_s=\mathrm{id}_T$ and $\sigma_s^*\tau=s$, so
$\sigma_s^{-1}(z(T))=Z(s)$ as schemes. Define

$$
c_r(F,s)=\sigma_s^*u_F\in H^{2r}_{Z(s)}\bigl(T,\Lambda(r)\bigr),
$$

the pullback of a class supported on $z(T)$ being supported on its inverse
image. This is a single global construction, involving no gluing on $T$.
On a trivializing open $T_0$ with $s|_{T_0}=(s_1,\dots,s_r)$ we have
$\sigma_s^*t_i=s_i$ and $\sigma_s^{-1}V(t_i)=V(s_i)$, so the
functoriality of the Kummer class, of the support boundary of
[def-pur-support-cohomology] and of the supported product gives

$$
c_r(F,s)|_{T_0}=\partial\kappa(s_1)\cup\cdots\cup\partial\kappa(s_r);
$$

when $s$ is regular this is the class of [def-pur-frame-class] of the
frame $s_1,\dots,s_r$ of the ideal of $Z(s)$.

*Comparison with $\operatorname{cl}_{T'}$.* Form the flag bundle
$p:T'\to T$ and $E'=E\times_TT'$, the vector bundle of $p^*F$, with zero
section $z'$, tautological section $\tau'$ and $\sigma_{s'}=\sigma_s\times_TT'$.
Let $\operatorname{cl}_{E'}\in H^{2r}_{z'(T')}(E',\Lambda(r))$ be the class
of Step 2 for $(p^*F,\tau')$ on $E'$. The construction of Step 2 is
functorial (Kummer classes, boundaries and supported products pull back),
so $\sigma_{s'}^*\operatorname{cl}_{E'}=\operatorname{cl}_{T'}$. It
therefore suffices to show $p_E^*u_F=\operatorname{cl}_{E'}$, where
$p_E:E'\to E$ is the projection. Both are classes on $E'$ supported on the
zero section of a vector bundle over $T'$, so by the universal case
applied over $T'$ they may be compared on the members of an open cover of
$T'$. The universal filtration of $p^*F$ is by subbundles with line-bundle
quotients, hence is split Zariski locally on $T'$: every point of $T'$ has
an open neighbourhood $U$ with a basis $e_1,\dots,e_r$ of $p^*F|_U$ such
that the $i$-th member of the filtration is spanned by $e_1,\dots,e_i$.
In the dual coordinates $t_1,\dots,t_r$ on $E'_U\cong\mathbf A^r_U$ the
line quotients carry, successively on the coordinate subspaces
$V(t_r)\supseteq V(t_r,t_{r-1})\supseteq\cdots$, the sections
$t_r,t_{r-1},\dots,t_1$, so the successive construction of Step 2 is
$\partial\kappa(t_1)\cup\cdots\cup\partial\kappa(t_r)$, the frame class of
an adapted frame. On $U\cap p^{-1}(T_0)$ the class $p_E^*u_F$ is the frame
class of the pullback of the frame chosen on $T_0$, which by
[lem-pur-frame-independence] equals the frame class of the adapted frame;
by the sheaf property over $U$ the two classes agree on $E'_U$, and hence on
$E'$. Pulling back along $\sigma_{s'}$ gives
$p^*c_r(F,s)=\operatorname{cl}_{T'}$. In particular the class of Step 2
lies in the image of the injective pullback $p^*$ of Step 1, and
$c_r(F,s)$ is the unique element with that pullback.

Step 4: the four properties. They follow after the injective
flag-bundle pullback, where they reduce respectively to the rank-one
Kummer construction, the functoriality of a local equation, the
associativity and direct-sum behaviour of the cup product (with the
transversality as in [lem-pur-kunneth-supported]), and the usual
splitting-principle definition of $c_r(F)$. For (L4): by Step 2 the
forgotten class of $\operatorname{cl}_{T'}$ is
$\prod_i(-c_1(L_i))=(-1)^rc_r(p^*F)$, where $L_1,\dots,L_r$ are the line
quotients of the flag, and $p^*$ is injective on ordinary cohomology by
Step 1 applied with support $T$; hence $c_r(F,s)$ forgets support to
$(-1)^rc_r(F)$, which is $c_r(F^\vee)$ because the Chern roots of
$F^\vee$ are $-x_1,\dots,-x_r$. The local description in the statement is
the formula for $c_r(F,s)|_{T_0}$ in Step 3. This is descent of one
element along a split injection of abelian groups, not descent of
derived categories or derived objects.
