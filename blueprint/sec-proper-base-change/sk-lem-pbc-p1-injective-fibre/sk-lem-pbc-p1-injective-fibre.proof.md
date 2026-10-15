+++
kind = "proof"
of = "sk-lem-pbc-p1-injective-fibre"
uses = ["sk-thm-pbc-henselian-h0", "sk-lem-pbc-finite"]
+++
*Inputs.* We use two results on henselian pairs, both valid with no
Noetherian or characteristic hypotheses.

1. *Gabber's affine henselian comparison.* If $(B,J)$ is a henselian pair and
   $G$ is a torsion abelian sheaf on $\operatorname{Spec}(B)_{\Et}$,
   restriction induces
   $H^q(\operatorname{Spec}B,G)\xrightarrow{\sim}H^q(\operatorname{Spec}(B/J),G|)$
   for $q\geq0$. This is Stacks Project, Tag 09ZI; its proof is an affine
   effacement argument.
2. *Lifting finite étale covers over a proper henselian pair.* If $Y$ is
   proper over a henselian pair $(B,J)$ and $Y_0=Y\times_BB/J$, restriction
   gives an equivalence $\mathsf{FEt}(Y)\xrightarrow{\sim}\mathsf{FEt}(Y_0)$
   (Stacks Project, Tag 0GS2, proved by algebraization, approximation, and
   descent of finite presentation). In particular, for a finite abelian group
   $M$, it gives the finite-torsor comparison
   $H^1(Y,\underline M)\xrightarrow{\sim}H^1(Y_0,\underline M)$: these groups
   classify $M$-torsors, and finite étale covers, their group actions, and the
   equations expressing simple transitivity are transported by the
   equivalence.

We also use the degree-zero comparison [sk-thm-pbc-henselian-h0], and two
finiteness facts on quasi-compact quasi-separated schemes: a sheaf of
$\mathbf F_r$-modules is a filtered colimit of constructible ones (Stacks
Project, Tag 03SA), and cohomology commutes with filtered colimits (Tag 03Q5).
Moreover a constructible sheaf $G$ of $\mathbf F_r$-modules admits a
monomorphism

$$
G\hookrightarrow\bigoplus_{a=1}^N(h_a)_*\underline{M_a},\qquad
h_a:Y_a\to X\ \text{finite and finitely presented},
$$

with $M_a$ finite $\mathbf F_r$-modules (Tag 09Z7). By [sk-lem-pbc-finite],
for $h$ finite, $R^qh_*G=0$ for $q>0$ and the underived exchange
$i^{-1}h_*G\xrightarrow{\sim}(h_0)_*i_Y^{-1}G$ is an isomorphism, where
$h_0:Y_0=Y\times_XX_0\to X_0$ and $i_Y:Y_0\to Y$ are the base changes.

*Degrees $q\geq2$.* First consider an affine open $W=\operatorname{Spec}B$ of
$X$, and set $J=\mathfrak mB$. The pair $(B,J)$ need not be henselian, so we
pass to its henselization $(B^h,JB^h)$. It has quotient $B/J$, and $B^h$ is
the filtered colimit of the étale $B$-algebras $B'$ equipped with
$B'/JB'\simeq B/J$. Gabber's affine comparison and étale cohomology
continuity give

$$
H^q(W_0,I_0|_{W_0})\simeq H^q(\operatorname{Spec}B^h,I|)
\simeq\varinjlim_{B'}H^q(\operatorname{Spec}B',I|).
$$

Restriction of an injective to an étale object is injective: the restriction
functor has the exact left adjoint given by extension by zero in the
localized site. Thus every group on the right vanishes for $q>0$.

The two standard affine charts $U,V\subset X$ have affine intersection.
Consequently $U_0$, $V_0$, and $(U\cap V)_0$ are acyclic for the restriction
of $I$ in positive degrees, by the display. Mayer–Vietoris on $X_0$ then gives
$H^q(X_0,I_0)=0$ for $q\geq2$. This is the two-chart case of Stacks Project,
Tag 0A51.

*Degree $1$.* Let $\xi\in H^1(X_0,I_0)$. Write $I$ as a filtered colimit of
constructible $\mathbf F_r$-sheaves. Pullback commutes with this colimit, as
does $H^1$ on $X_0$. Hence $\xi$ is the image of a class
$\zeta\in H^1(X_0,G_0)$ for some constructible $G$ with a map $G\to I$.
Choose an embedding as above and put $P=\bigoplus_a(h_a)_*\underline{M_a}$.
Injectivity of $I$ extends $G\to I$ to $P\to I$; let $\zeta'$ be the image of
$\zeta$ in $H^1(X_0,P_0)$.

By the finite-morphism facts and Leray,

$$
H^1(X_0,P_0)\simeq\bigoplus_aH^1((Y_a)_0,\underline{M_a}),\qquad
H^1(X,P)\simeq\bigoplus_aH^1(Y_a,\underline{M_a}).
$$

Each $Y_a$ is proper over $A$, since it is finite over $X$. The finite-torsor
comparison therefore lifts $\zeta'$ to a class $\widetilde\zeta\in H^1(X,P)$.
Its image in $H^1(X,I)$ is zero because $I$ is injective. The natural
restriction square

$$
\begin{array}{ccc}
H^1(X,P) & \longrightarrow & H^1(X,I)\\
\downarrow & & \downarrow\\
H^1(X_0,P_0) & \longrightarrow & H^1(X_0,I_0)
\end{array}
$$

shows that the image $\xi$ of $\zeta'$ is zero. This proves the remaining
degree. The argument is the one in Stacks Project, Tag 0A5H.
