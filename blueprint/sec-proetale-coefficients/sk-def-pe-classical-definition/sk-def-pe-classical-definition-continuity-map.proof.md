+++
kind = "proof"
of = "det-pe-classical-definition-continuity-map"
+++
The only points to check are well-definedness. In item 2, a filtered colimit
of sets is the quotient of $\coprod_iF(U_i)$ by the relation identifying
$s\in F(U_i)$ with $F(u_{ji})(s)\in F(U_j)$; the maps $F(u_i)$ respect this
relation since $F(u_j)F(u_{ji})=F(u_{ji}\circ u_j)=F(u_i)$, so $c_{F,U}$ exists
and is unique. Naturality in $F$ holds because a morphism of sheaves commutes
with all restriction maps.

In item 3, for a module sheaf the forgetful functor from $\Lambda$-modules to
sets commutes with filtered colimits, so the module colimit has the set colimit
as underlying set and $c_{F,U}$ is the same map of sets. Each $F(u_i)$ is
$\Lambda$-linear, hence so is $c_{F,U}$. A $\Lambda$-linear bijection is an
isomorphism of modules, so a module sheaf is classical as a module sheaf if and
only if its underlying sheaf of sets is classical.

In item 4, a quasi-isomorphism, and more generally an isomorphism in the
derived category, induces isomorphisms on all cohomology sheaves. Classicality
of a sheaf is invariant under isomorphism of sheaves by naturality of
$c_{F,U}$, so the condition depends only on the isomorphism class.
