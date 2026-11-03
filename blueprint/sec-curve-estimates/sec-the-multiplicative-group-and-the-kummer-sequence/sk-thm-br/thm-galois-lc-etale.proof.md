+++
kind  = "proof"
of    = "thm-galois-lc-etale"
+++
We work with the categories $\mathrm{F\acute Et}(Y)$ and
$\mathrm{FLC}(Y)$ of [def-galois-categories], and with the
$M$-torsors of [def-weil-pbc-finite-torsors].
Step 1: the sheaf is finite locally constant. By
[lem-fet-locally-trivial] there is an etale covering $\{U_i\to Y\}$
with $P\times_YU_i\cong\coprod_{s\in S_i}U_i$ for finite sets $S_i$;
over $U_i$ the sheaf $\underline{\operatorname{Hom}}_Y(-,P)$ is
therefore the constant sheaf of value $S_i$, so it is locally constant
with finite fibres.
Step 2: full faithfulness. For finite etale $P,Q$ the comparison map
$\operatorname{Hom}_Y(P,Q)\to\operatorname{Hom}( \underline{\operatorname{Hom}}(-,P),\underline{\operatorname{Hom}}(-,Q))$
is injective since a morphism is determined by its graph, a closed
subscheme, hence a subsheaf; it is surjective because a morphism of sheaves
is, after applying Step 1 to $P$ and $Q$ over a common etale covering, given on each member by
a map of finite sets compatible with the descent data, which descends
because the base change functor of [lem-galois-descent] is fully
faithful.
Step 3: essential surjectivity. Let $\mathcal F\in\mathrm{FLC}(Y)$ and
choose an etale covering $\{U_i\to Y\}$ with $\mathcal F|_{U_i}$
constant of finite value $S_i$; let $Y'=\coprod_iU_i$, a surjective etale
$Y$-scheme, and $P'=\coprod_i\coprod_{s\in S_i}U_i$, finite etale over
$Y'$, so that $\mathcal F|_{Y'}$ is represented by $P'$. The
glueing isomorphisms of $\mathcal F$ over $Y''$, transported through
the Yoneda bijection of Step 2 over $Y''$, give a descent datum for
$P'$; by [lem-galois-descent] there is a finite etale $P\to Y$
with $P\times_YY'\cong P'$, and then
$\underline{\operatorname{Hom}}(-,P)\cong\mathcal F$ because both are
represented by $P'$ over $Y'$ and the sheaf condition
glues the identification.
Step 4: the compatibilities and the torsor statement are as in the
statement: the inverse image along $Y'\to Y$ of the sheaf represented by
$P$ is represented by $P\times_YY'$, the inverse image being left adjoint
to the direct image; the fibre of the sheaf of morphisms is
$\operatorname{Hom}_{\bar y}(\bar y,P)=|P_{\bar y}|$, and an $M$-action
on $P$ corresponds to one on the sheaf, the map
$M\times P\to P\times_YP$ being an isomorphism exactly when the action on
each fibre is simply transitive, which is condition (1) of
[def-weil-pbc-finite-torsors]; condition (2), that the sheaf has sections
locally, holds exactly when $P\to Y$ is surjective: a surjective finite
etale $P\to Y$ is an etale covering of $Y$ over which $P$ acquires the
diagonal section, and conversely sections over a covering force
surjectivity.
