+++
kind = "proof"
of = "det-thm-sf-pf-field-localizing"
+++
Both sides lie in $\Loc(\Dbc(Y,\Lambda))$: $p^*$ and $Rp_*$ restrict to exact,
direct-sum preserving functors between the localizing categories, and these
are closed under $\otimes^{\mathbf L}$ by [det-thm-sf-pf-field-tensor](2). The
projection map is natural in $A$ and $B$ and compatible with shifts and
cones.

Fix $B\in\Dbc(Y,\Lambda)$. As functors of $A$, both sides are exact and
preserve direct sums (tensor product, $p^*$ and $Rp_*$ do). The map is an
isomorphism for $A\in\Dbc(X,\Lambda)$ by the projection formula on bounded
constructible complexes ([sk-thm-sfb-proper-base-change]). A natural
transformation between exact, direct-sum preserving functors on
$\Loc(\Dbc(X,\Lambda))$ which is an isomorphism on $\Dbc(X,\Lambda)$ is an
isomorphism everywhere ([sk-lem-sf-determination]): the objects on which it
is an isomorphism form a localizing subcategory. Hence the map is an
isomorphism for all $A$. Now fix $A\in\Loc(\Dbc(X,\Lambda))$; as functors of
$B$ both sides are again exact and direct-sum preserving, and the map is an
isomorphism for $B\in\Dbc(Y,\Lambda)$ by the first step, so the same argument
gives it for all $B$.
