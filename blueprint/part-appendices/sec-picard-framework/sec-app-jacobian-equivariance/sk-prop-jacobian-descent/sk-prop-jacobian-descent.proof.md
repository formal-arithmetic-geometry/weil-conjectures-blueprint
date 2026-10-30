+++
kind = "proof"
of = "sk-prop-jacobian-descent"
uses = ["sk-thm-picard-main", "sk-def-picard-pic", "sk-thm-picard-twist", "sk-prop-av-mult-n-pullback", "sk-prop-picard-pic-split"]
+++
The idea is to descend the Jacobian of $C_{0,k_s}$, where $k_s\subseteq\bar k$ is a separable closure of $k$. Since $k_s/k$ is in general
infinite, hence not an fppf cover, we first pass to a finite
separable extension by limit arguments and then descend along it.

Let $F=\operatorname{Pic}^0_{C_0/k}$ be the degree-zero part of the
fppf Picard sheaf; the fibrewise degree is locally constant by coherent
base change and Riemann–Roch. Theorem [sk-thm-picard-main] gives an
abelian variety $J_s$ over $k_s$, which is projective, representing the
restriction of $F$ to $k_s$-schemes, because the Picard sheaf and the
degree commute with base change. Over $k_s\otimes_kk_s$ the two
pullbacks of $J_s$ represent the same functor, so Yoneda gives an
isomorphism between them; it satisfies the cocycle condition over
$k_s\otimes_kk_s\otimes_kk_s$ and respects the group structures, since
all identifications are induced by $F$.

Now $k_s$ is the filtered union of its finite separable
subextensions, and $k_s\otimes_kk_s$ and the triple tensor product are
the corresponding unions. By the limit theorems for schemes of finite
presentation [Stacks, Tag 01ZM](https://stacks.math.columbia.edu/tag/01ZM), the defining equations of $J_s$ in a
projective space, the descent isomorphism, its inverse and the group
operations are defined over some finite stage, and the finitely many
identities among them (inverse, cocycle, group axioms) hold after
enlarging the stage. Enlarging it further to a Galois extension, we
obtain a finite Galois extension $K/k$ in $k_s$, a projective $K$-scheme
$J_K$ with a group structure and a compatible descent datum for $K/k$,
whose base change to $k_s$ is the datum on $J_s$. Since
$\operatorname{Spec}K\to\operatorname{Spec}k$ is finite locally free
and surjective, the descent datum on the projective scheme $J_K$ is
effective [Stacks, Tag 0CCJ](https://stacks.math.columbia.edu/tag/0CCJ). We get a commutative group scheme $J_0$ over
$k$ with $J_0\times_kk_s\simeq J_s$. Properness and smoothness descend
along $K/k$, and connectedness and dimension may be checked over $\bar k$, so $J_0$ is an abelian variety of dimension $g$.

It remains to show that $J_0$ represents $F$. Both functors are
locally of finite presentation: for $J_0$ this is [Stacks, Tag 01ZC](https://stacks.math.columbia.edu/tag/01ZC), and
for $F$ it follows from Lemma [sk-prop-picard-pic-split] once the
finite stages contain a field of definition of a point of $C_0$,
because invertible sheaves, rigidifications and their isomorphisms are
of finite presentation. Hence, for affine $T$ over $k$, a section of
either functor over $T_{k_s}$, or over $T_{k_s\otimes_kk_s}$, comes from
a finite stage, and two sections that agree over $T_{k_s}$ agree over
a finite stage. The identification $J_0(T_{k_s})\simeq F(T_{k_s})$ is
compatible with the descent data. Given a section of one functor over
$T$, we transport its image over $T_{k_s}$, descend the result to some
$T_L$ with $L/k$ finite, enlarge $L$ so that its two pullbacks to
$T_{L\otimes_kL}$ agree, and descend it to $T$ since both functors are
fppf sheaves. The same argument applied to equalities shows that the
result is unique. We obtain inverse bijections $J_0(T)\simeq F(T)$,
natural in affine $T$, and hence an isomorphism of sheaves.

Since the Picard sheaf and the degree commute with field extension,
$J_0\times_kk'$ represents the degree-zero Picard sheaf of
$C_0\times_kk'$ for every $k'/k$. Over $\bar k$, rigidification and
$\operatorname{Pic}(\bar k)=0$ show that the Picard sheaf has the Picard
group as its value, which gives the displayed identification. For
$\gamma\in\operatorname{Gal}(\bar k/k)$, naturality with respect to
$\operatorname{Spec}(\gamma)$ says that this group isomorphism
intertwines the Galois action on points with pullback of invertible
sheaves; here $\operatorname{Gal}(\bar k/k)=\operatorname{Gal}(k_s/k)$
because $\bar k/k_s$ is purely inseparable.
