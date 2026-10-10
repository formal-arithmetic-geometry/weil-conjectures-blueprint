+++
kind  = "proof"
of    = "thm-pc-criterion"
uses = ["lem-pc-schemes-criterion"]
+++
*Reduction to functors on all schemes.* [lem-pc-schemes-criterion] is
stated for functors on the category of all schemes. To a functor $H$ on
$\mathit{Sch}/k$ associate the functor $\tilde H$ on all schemes with
$\tilde H(T)=\coprod_{a:T\to\operatorname{Spec}k}H(T,a)$, where $(T,a)$ is
$T$ viewed as a $k$-scheme via $a$. Then $\tilde H$ is a Zariski sheaf if
$H$ is (a Zariski covering of $T$ refines to coverings of the $k$-schemes
$(T,a)$, and the structure morphisms glue uniquely), subfunctors of $H$
give subfunctors of $\tilde H$, a $k$-scheme $P$ representing $H$ gives the
scheme $P$ representing $\tilde H$ (a morphism $T\to P$ is the same as a
$k$-structure $a$ on $T$ together with a $k$-morphism $(T,a)\to P$),
representability by open immersions is preserved (the base change along
$h_T\to\tilde H$ only involves the $k$-structure carried by the element),
and conversely a scheme $P$ representing $\tilde H$ comes with the morphism
$P\to\operatorname{Spec}k$ induced by $\tilde H\to h_{\operatorname{Spec}k}$,
$(a,\xi)\mapsto a$, and then represents $H$ as a $k$-scheme. So it
suffices to apply [lem-pc-schemes-criterion] to $\tilde G$ and the family
$(\tilde F_i)_{i\in I}$ constructed below; we argue with $G$ and the $F_i$,
the translation being the one just described.

*The family.* Let $I=G(k)$; it is a set because the values of $G$ are
small by (1), so $(F_i)_{i\in I}$ is a family indexed by a set, as
[lem-pc-schemes-criterion] requires. For
$i=g'\in I$ let $F_i\subseteq G$ be the subfunctor

$$
F_i(T):=\{g\in G(T):g'g\in F(T)\}.
$$

Then $F_i\cong F$ via multiplication by $g'$ (a natural isomorphism
because $G$ is a functor with values in groups), so $F_i$ is
representable by (2)(a), and $F_i\subseteq G$ is representable by open
immersions: the map $F_i\to G$ is isomorphic (via multiplication by
$g'$) to the inclusion $F\to G$ of (2)(b), and the base change of a
natural isomorphism is a natural isomorphism. The family
$(F_i)_{i\in I}$ covers $G$ ([def-pc-cover]): given $g\in G(T)$, for each point $t\in T$
let $\kappa=\kappa(t)$ and let $j:\operatorname{Spec}\kappa\to T$; by (2)(c) applied to
$j^*g\in G(\kappa)$ there is $g'\in G(k)$ with
$g'j^*g\in F(\kappa)$, i.e. $j^*g\in F_{g'}(\kappa)$. By (2)(b) (the
open-immersion property for the pair $(T,\xi)$ with $\xi=g$, in the sense
of [def-pc-subfunctor]) there is an open
$U_\xi^{g'}\subseteq T$ such that a morphism $u:T'\to T$ factors through
$U_\xi^{g'}$ iff $u^*g\in F_{g'}(T')$; taking $T'=\operatorname{Spec}\kappa$ with
$j$ and noting that $j$ factors through the open $U$ iff the image point
$t$ lies in $U$, we find $t\in U_g^{g'}$ for the suitable $g'$, so the
open sets $U_g^{g'}$ ($g'\in G(k)$) cover $T$, and
$g|_{U_g^{g'}}\in F_{g'}(U_g^{g'})$ by the criterion. This verifies
(2)(c) of [lem-pc-schemes-criterion] (in the form of the covering
condition [def-pc-subfunctor]), while (2)(a), (2)(b) for the family
$(F_i)$ are what we just proved and (1) is the hypothesis; hence $G$ is
representable by a scheme. As $G$ takes values in groups and the
representing object is unique up to unique isomorphism, the group
structure on $G$ makes it a group scheme (the group-valued sheaf
structure is given; see the usual Yoneda argument, cf. [def-pc-representable-functor]).
