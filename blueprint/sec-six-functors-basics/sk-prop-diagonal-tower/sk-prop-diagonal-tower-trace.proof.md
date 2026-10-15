+++
kind = "proof"
of = "det-prop-diagonal-tower-trace"
+++
(1) The map of systems
$(1,h_\bullet):\mathbf Z/\ell^\bullet\oplus\mathbf Z/\ell^\bullet(-1)[-2]\to Rq_*\mathbf Z/\ell^\bullet$,
where $h_\bullet$ is the class of a section built as in
[det-prop-diagonal-tower-system] from the Cartier extension of the section
(a morphism of systems by the same construction), is defined in the derived
category of inverse systems. Derived direct image of a system is computed
levelwise ([det-prop-diagonal-tower-limit](1)), and at level $n$ the map is the
isomorphism of [sk-lem-geo-p1-cohomology] (compare
[thm-amb-p1-decomposition]). Cohomology of systems is computed levelwise, so
its cone is acyclic and the map is an isomorphism. Twisting by $(1)[2]$ and
composing its inverse with the projection to the summand
$\mathbf Z/\ell^\bullet$ gives the trace on systems, and $R\varprojlim$ gives
$\operatorname{Tr}_q$. Since $Rq_*$ commutes with $R\varprojlim$, its source is
$Rq_*\Zl(1)[2]$ and its target $\Zl$; derived direct image preserves derived
completeness, so source and target are complete, and the equivalence of
[det-prop-diagonal-tower-limit](3) makes it linear over the completed
coefficient sheaf on $Y$. Its level-$n$ reduction is the projection of
[def-amb-p1-trace], the torsion trace.

(2) By [det-prop-diagonal-tower-limit](1) the composite
$\operatorname{Tr}_{p_i}\circ Rp_{i*}(\delta)$ is $R\varprojlim$ of the
corresponding composite of morphisms of systems,
$e_\bullet:\mathbf Z/\ell^\bullet=Rp_{i*}\Delta_*\mathbf Z/\ell^\bullet\to\mathbf Z/\ell^\bullet$,
in the derived category of inverse systems on
$(\mathbf P^1_Y)_{\mathrm{proét}}$. The object $\mathbf Z/\ell^\bullet$ is
concentrated in degree $0$, and endomorphisms of an object in degree $0$ in a
derived category of an abelian category are its endomorphisms in the abelian
category. Here these are endomorphisms of inverse systems of sheaves, that is,
compatible families of endomorphisms of the levels $\mathbf Z/\ell^n$. So
$e_\bullet$ is determined by its levels, and at each level it is the
identity by the torsion integration identities of
[sk-prop-geo-p1-adjunction] (compare [lem-amb-p1-diagonal-integrals]). Hence
$e_\bullet=1$ and $R\varprojlim e_\bullet=1_{\Zl}$. (For morphisms between
arbitrary objects of the derived category of inverse systems, equality at
every level would not imply equality; this is why the identity is checked on
an object in degree $0$.)
