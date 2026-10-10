+++
kind  = "proof"
of    = "thm-galois-lc-etale"
+++
We work with the categories $\mathrm{F\acute Et}(Y)$ and
$\mathrm{FLC}(Y)$ of [def-galois-categories], and with the
$M$-torsors of [def-weil-pbc-finite-torsors].
Step 1: the sheaf is finite locally constant. By
[lem-fet-locally-trivial] there is a surjective etale $Y'\to Y$
with $P\times_YY'\cong Y'\times S$; then
$\underline{\operatorname{Hom}}_Y(Y'\times S,T)= \underline S(Y'\times_YT)$ is constant of value $S$, so the sheaf is
locally constant with finite fibres.
Step 2: full faithfulness. For finite etale $P,Q$ the comparison map
$\operatorname{Hom}_Y(P,Q)\to\operatorname{Hom}( \underline{\operatorname{Hom}}(-,P),\underline{\operatorname{Hom}}(-,Q))$
is injective since a morphism is determined by its graph, a closed
subscheme, hence a subsheaf; it is surjective because a morphism of sheaves
is, after applying Step 1 to $P$ and $Q$ over a common cover, given by
a map of finite sets compatible with the descent data, which descends by
[lem-galois-descent], Step 1.
Step 3: essential surjectivity. Let $\mathcal F\in\mathrm{FLC}(Y)$ and
choose a surjective etale $Y'\to Y$ with $\mathcal F|_{Y'}\cong \underline S$. Put $P'=Y'\times S$, finite etale over $Y'$. The
glueing isomorphisms of $\mathcal F$ over $Y''$, transported through
the Yoneda bijection of Step 2 over $Y''$, give a descent datum for
$P'$; by [lem-galois-descent] there is a finite etale $P\to Y$
with $P\times_YY'\cong P'$, and then
$\underline{\operatorname{Hom}}(-,P)\cong\mathcal F$ because both are
locally constant with value $S$ over the cover and the sheaf condition
glues the identification.
Step 4: the compatibilities and the torsor statement are as in the
statement: the fibre of the sheaf of morphisms is
$\operatorname{Hom}_{\bar y}(\bar y,P)=|P_{\bar y}|$, and an $M$-action
on $P$ corresponds to one on the sheaf, the map
$M\times P\to P\times_YP$ being an isomorphism exactly when the action on
each fibre is simply transitive.
