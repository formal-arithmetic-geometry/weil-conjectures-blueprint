+++
kind = "proof"
of = "proposition-pro-etale-site-separably-closed--2"
order = 173005
uses = ["proposition-pro-etale-site-separably-closed--1", "proposition-topos-functoriality"]
+++
By [proposition-pro-etale-site-separably-closed--1] and the comparison
theorem for a dense subsite, restriction of abelian sheaves along
$S\mapsto(\operatorname{Spec}\Omega)[S]$ is an equivalence. It is the
right adjoint of $p_\Omega^*$, obtained by composing direct image along
$\operatorname{Spec}\Omega\to\operatorname{Spec}\mathbf Z$ with
restriction along $S\mapsto\operatorname{Spec}LC(S,\mathbf Z)$.
The composite adjunction therefore makes $p_\Omega^*$ an equivalence.

For the algebraically closed formulation, apply the same dense-subsite
comparison to sets, abelian groups and rings. The specified point
adjunctions consequently have invertible units and counits. The test
functor preserves finite limits, so it sends the singleton to a terminal
object; its canonical map to $\operatorname{Spec}\Omega$ is therefore
an isomorphism. Finally, transport scalar actions along the restriction
equivalences for sets and abelian groups. The module laws can be checked
on the dense subsite, which gives the asserted equivalence for modules
over each ring sheaf $R$.
