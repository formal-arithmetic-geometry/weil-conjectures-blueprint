+++
kind = "proof"
of = "corollary-continuity-cohomology--2"
order = 106004
uses = ["proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "proposition-pro-etale-coverings", "lemma-stability"]
+++
Replace $I$ by an equivalent small category. First consider $q=0$.
By [proposition-pro-etale-affines-form-basis], it suffices to test the
comparison on affine objects $V$ of $Y_{\mathrm{pro}\acute{e}t}$. Put
$W=X\times_YV$. This scheme is quasi-compact and quasi-separated, and
$$
(f_*F)(V)=F(W).
$$
Finite affine coverings and their Čech overlaps, as in
[proposition-pro-etale-coverings] and [lemma-stability], show that
sections on $V$ and $W$ commute with filtered colimits. Thus $f_*$
preserves these colimits.

A filtered colimit of injective sheaves is $f_*$-acyclic. To see this,
restrict the diagram to each $W=X\times_YV$ with $V$ affine. Pullback
to this localized pro-étale site preserves colimits and injective
sheaves. The finite Čech-cover criterion shows that the resulting
colimit has no positive cohomology on $W$: Čech complexes commute with
the filtered colimit and those of the injective sheaves are exact in
positive degrees. The comparison of derived sections with sheaf
cohomology, tested on the affine basis, gives the required acyclicity.

Induct on $q$, starting with $R^0f_*\simeq f_*$. Embed the diagram
functorially into injectives with cokernel diagram $(Q_i)$. Exactness
of filtered colimits gives the corresponding short exact sequence of
colimits. The long exact sequences of higher direct images give a
commuting diagram of exact rows ending in $R^{q+1}f_*$ and zero. The
comparison maps in degree $q$ are isomorphisms by induction, and the
colimit of the injectives is acyclic by the preceding argument. The
cokernel comparison therefore gives the isomorphism in degree $q+1$.
