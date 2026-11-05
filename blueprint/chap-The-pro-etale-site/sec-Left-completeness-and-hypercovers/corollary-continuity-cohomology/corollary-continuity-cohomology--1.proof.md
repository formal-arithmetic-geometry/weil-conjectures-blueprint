+++
kind = "proof"
of = "corollary-continuity-cohomology--1"
order = 106003
uses = ["proposition-pro-etale-coverings", "lemma-stability", "proposition-topos-functoriality"]
+++
Consider the objects of $U_{\mathrm{pro}\acute{e}t}$ whose underlying
schemes are quasi-compact and quasi-separated. Every covering sieve of
such an object contains a finite affine covering, by
[proposition-pro-etale-coverings]. Its Čech nerve again consists of
quasi-compact and quasi-separated objects: finite fibre products have
this property, and remain in the site by [lemma-stability].

Sections on these objects commute with filtered colimits. Indeed,
sections of the sheaf colimit lift locally to a member of the diagram.
Choose a finite covering and pass to a common index for these lifts.
Their differences on the overlaps vanish at a later common index, so
the lifts glue. The same finite-cover argument shows that a section
which vanishes in the colimit vanishes at a later index. Consequently,
the Čech complexes of these finite coverings commute with filtered colimits. The Čech
complexes of injective sheaves are exact in positive degrees, so the
Čech criterion shows that a filtered colimit of injective sheaves has
no higher cohomology.

We now argue by induction on $q$. Degree zero is the assertion about
sections. In the Grothendieck abelian category of abelian sheaves,
embed the diagram functorially into a diagram $(I_i)$ of injective
sheaves, with cokernels $(Q_i)$. Filtered colimits are exact, giving
$$
0\longrightarrow\varinjlim_i F_i\longrightarrow\varinjlim_i I_i
\longrightarrow\varinjlim_i Q_i\longrightarrow0.
$$
Compare the long exact cohomology sequences before and after taking
the colimit. The induction hypothesis and the vanishing just proved
give both representation of classes and eventual vanishing in the
next degree.
