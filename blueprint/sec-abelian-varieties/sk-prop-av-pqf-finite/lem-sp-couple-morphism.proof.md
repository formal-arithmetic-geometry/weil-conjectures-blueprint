+++
kind  = "proof"
of    = "lem-sp-couple-morphism"
+++
The derived couple construction is functorial in the couple
([def-sp-exact-couple]): $t_D$ restricts to a map from
$\operatorname{im}\alpha$ to $\operatorname{im}\alpha'$ because it commutes
with $\alpha$, and $t_E$ is a morphism of complexes $(E,g\circ f)\to(E',g'\circ
f')$ because it commutes with $f$ and $g$, so it induces a map on their
cohomology; these maps between the derived couples commute with the structure
maps of the derived couples, since those are defined by restriction and
passage to subquotients. Iterating gives morphisms of all derived
couples, and on each page the map on $E_r$ commutes with $d_r=g_r\circ f_r$;
by construction the map on $E_{r+1}$ is the map induced on the cohomology of
$(E_r,d_r)$. Under the hypotheses of [thm-sp-half-plane-convergence], the
filtration of $D^{0,n}$ is $G_qD^{0,n}=\operatorname{im}(\alpha^{n-q}:
D^{n-q,q}\to D^{0,n})$; since $t_D$ commutes with every power of $\alpha$, it
sends $\operatorname{im}(D^{n-q,q}\to D^{0,n})$ into
$\operatorname{im}(D'^{n-q,q}\to D'^{0,n})$, so it preserves the filtrations.
All these constructions commute with composition of morphisms of couples.
