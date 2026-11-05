+++
kind = "proof"
of = "lemma-sheaves-finite-support-finite-morphisms--1"
order = 1597003
uses = ["lemma-finite-morphisms", "lemma-finite-morphisms-cohomology"]
+++
For each $x\notin U$, write $i_x:\operatorname{Spec}\kappa(x)\to X$.
The adjunction units give

$$
F\longrightarrow\bigoplus_{x\notin U}i_{x,*}i_x^*F.
$$

This is an isomorphism: it suffices to pull back to $U$ and to each
$i_x$, since these morphisms are jointly surjective. On $U$ both sides
vanish. At $x$, the other summands vanish by finite base change
[lemma-finite-morphisms], and the $x$-summand is identified with $i_x^*F$
by the adjunction for the closed immersion. On the spectrum of a
separably closed field the constant sheaf $\mathbf Z$ is projective,
so positive cohomology vanishes. Lemma [lemma-finite-morphisms-cohomology]
and additivity of cohomology for finite direct sums give the first assertion.

For the second assertion, a finite type scheme of dimension at most zero
over $k$ is Artinian, hence finite and discrete; its residue fields are
$k$. Apply the first assertion with $U=\varnothing$, and identify sheaf
cohomology with the cohomology of derived global sections.
The singleton opens form a finite disjoint cover, so sections are the
product of sections over these opens. Each singleton open, pointed by
$s_x$, is initial among pointed étale neighbourhoods of $s_x$:
topological invariance along its residue-field inclusion gives a section
through the chosen point of every such neighbourhood, and the open
equalizer of two sections gives uniqueness. Thus sections on that open
are the stalk $G_{s_x}$. The resulting product map is the canonical germ
map, and the degree-zero derived-to-underived comparison gives the
displayed isomorphism.
