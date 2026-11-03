+++
kind  = "proof"
of    = "lem-wf-dense-open-pi1-surjective"
+++
*Step 0 ($V$ is integral).* The local rings of the normal scheme $V$
are domains, so $V$ is reduced and a point lies on only one irreducible
component (two components through it would give two minimal primes of
its local domain). The finitely many components are therefore disjoint
and closed, hence open, and connectedness leaves only one: $V$ is
integral. The same argument applies to every connected normal
Noetherian scheme below.

*(1).* Let $W\to V$ be a connected finite etale cover. Its image is
open (etale) and closed (finite) and nonempty, so $W\to V$ is surjective
since $V$ is connected. The scheme $W$ is Noetherian, being finite over
$V$, so by [lem-fin-etale-normal-components] it is a finite disjoint
union of open-and-closed normal integral schemes; being connected, $W$
is itself integral. Its open subscheme $W':=W\times_VV'$ is nonempty,
because $W\to V$ is surjective and $V'\neq\emptyset$; a nonempty open
of an irreducible scheme is irreducible, so $W'$ is connected. This is
the second formulation.

To get surjectivity, note that pullback along $k$ is compatible with the
fibre functors at $\bar v$, which gives the map of automorphism groups
$\pi_1(V',\bar v)\to\pi_1(V,\bar v)$ of [def-galois-fibre-functor],
continuous for the profinite topologies; under the equivalences of
[thm-galois-fundamental] the fibre of $W'$ is the fibre of $W$ with
$\pi_1(V',\bar v)$ acting through this map. Its image $H$ is compact,
hence closed in $G:=\pi_1(V,\bar v)$. If $H\neq G$, then, a closed
subgroup of a profinite group being the intersection of the open
subgroups containing it, there is an open subgroup $H\subseteq
U\subsetneq G$. The finite continuous $G$-set $G/U$ is transitive, so by
[thm-galois-fundamental] it is the fibre of a finite etale $W\to V$
which is connected: a decomposition $W=W_1\sqcup W_2$ into nonempty
open-and-closed pieces would split $G/U$ into two nonempty $G$-stable
subsets, both pieces being surjective over $V$ as above. On the other
hand, $H\subseteq U$ fixes the coset $U$, and $|G/U|\geq2$, so
$\pi_1(V',\bar v)$ does not act transitively on the fibre of $W'$. Since
$(\mathrm{F\acute Et}(V'),F_{\bar v})$ is a Galois category by
[lem-fet-galois-category], [lem-galois-transitive] shows that $W'$ is
not connected, contradicting the first paragraph. Hence $H=G$. This is
SGA 1, Exp. V, Prop. 8.2.

*(2).* The base change $V\to V_0$ is universally open, so $V'$ is a
dense open of $V$, and (1) applies to $V'\subseteq V$. Choose $\bar v$
in $V'$. The morphism $V'_0\to V_0$ is a $k_0$-morphism, so the map
$\pi_1(V'_0,\bar v)\to\pi_1(V_0,\bar v)$ lies over
$\operatorname{Gal}(k/k_0)$ and hence induces a map of the fibre
products
$W(-)=\pi_1(-,\bar v)\times_{\operatorname{Gal}(k/k_0)}\langle\Phi\rangle$
of [def-wf-fundamental-representation] which is the identity on the
factor $\langle\Phi\rangle$; this is the compatibility with the degree
maps of [def-wf-weil-group]. By [lem-wf-weil-group-exact-sequence] the
kernels of the degree maps are the geometric groups $\pi_1(V')$ and
$\pi_1(V)$, and the induced map between them is the map of (1). Now let
$w\in W(V_0)$ have degree $n$. By [lem-wf-weil-group-exact-sequence]
there is $w'\in W(V'_0)$ of degree $n$; its image $\bar w'$ has degree
$n$, so $w\bar w'^{-1}$ lies in $\pi_1(V)$ and, by (1), is the image of
some $g\in\pi_1(V')$. Then $gw'\mapsto w$.

*(3).* For a finite locally constant sheaf over a finite ring it suffices to
evaluate on affine etale $T\to V$. Such $T$ is Noetherian, so by
[lem-fin-etale-normal-components] it is a finite disjoint union of
normal integral $T_i$, and it suffices to treat each $T_i$. The open
$T'_i:=T_i\times_VV'$ is nonempty (the image of $T_i$ is a nonempty open
of the integral $V$, hence meets $V'$), hence dense in $T_i$. Pick a
geometric point $\bar t$ of $T'_i$. Sections of $\mathcal N$ over the
connected $T_i$ are morphisms from the constant sheaf, so by
[cor-galois-lisse-representations] they are the invariants
$\mathcal N_{\bar t}^{\pi_1(T_i,\bar t)}$; likewise
$(k_*k^*\mathcal N)(T_i)=\mathcal N(T'_i)
=\mathcal N_{\bar t}^{\pi_1(T'_i,\bar t)}$, and restriction is the
inclusion of invariants. By (1) applied to $T'_i\subseteq T_i$ the two
groups have the same image in $\operatorname{Aut}(\mathcal N_{\bar t})$,
so the invariants agree.

*(4).* The open $U'_0$ is again a curve in the sense of [d-real-setup]
(a nonempty open of the irreducible smooth $U$ is connected), and $U$,
$U'$ share the geometric generic point $\bar\eta$. By
[prop-wf-weil-sheaf-representation-equivalence] on $U_0$ and on
$U'_0$, lisse Weil sheaves are the representations of the Weil groups
on their generic stalks, and $k^*$ corresponds to restriction along
$W(U'_0)\to W(U_0)$: the stalk at $\bar\eta$ is unchanged and the
fundamental representation of [def-wf-fundamental-representation] is
formed from pullbacks of the same covers. This map is surjective by (2)
(normality of $U$ being smoothness). Hence
$\operatorname{Hom}_{W(U_0)}(V_1,V_2)=\operatorname{Hom}_{W(U'_0)}(V_1,V_2)$,
which is full faithfulness, and the $W(U_0)$-stable and
$W(U'_0)$-stable subspaces of a stalk coincide. Since subobjects match
under the equivalence, lisse subsheaves of $\mathcal N$ and of
$k^*\mathcal N$ correspond, which gives the statement on irreducibility.
The geometric version is the same argument with
[thm-lisse-qlbar-representations] and (1).

