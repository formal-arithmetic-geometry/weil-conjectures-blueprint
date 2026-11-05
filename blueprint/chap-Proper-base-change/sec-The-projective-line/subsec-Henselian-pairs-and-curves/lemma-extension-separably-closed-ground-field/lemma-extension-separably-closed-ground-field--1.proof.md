+++
kind = "proof"
of = "lemma-extension-separably-closed-ground-field--1"
order = 364002
uses = ["definition-torsion-sheaves"]
+++
Choose compatible algebraic closures $K$ of $k$ and $K'$ of $k'$, and put
$D=C_K$ and $D'=C'_{K'}$. The projections $p:D\to C$ and $p':D'\to C'$
are universal homeomorphisms, since the two algebraic extensions are
purely inseparable. There is a cartesian square $D'\to D$ over
$\operatorname{Spec}K'\to\operatorname{Spec}K$; write $a:D'\to D$ for its
upper map. Then $\iota'\circ p'=p\circ a$. Properness is preserved by
base change, and $p$ is a homeomorphism, so $D$ is proper over $K$ with
$\dim D\leq1$.

Let $A$ be the underlying abelian sheaf of $F$, and put $G=p^*F$.
Pullback preserves torsion of geometric stalks. Moreover, the underlying
abelian sheaf of $G$ is canonically isomorphic to $p^*A$: forgetting
module structure commutes with pullback. Applying the assumed
algebraically closed assertion to $G$, and using naturality of
cohomological pullback in this isomorphism, shows that

$$
H^q(D_{\acute{e}t},p^*A)\longrightarrow
H^q(D'_{\acute{e}t},a^*p^*A)
$$

is an isomorphism.

Topological invariance of the étale site makes the pullbacks along $p$
and $p'$ isomorphisms on cohomology. Functoriality of cohomological
pullback, with the canonical identifications of composite inverse
images, identifies the composite through $C'$ with the composite
through $D$. The latter is an isomorphism by the preceding paragraph
and topological invariance for $p$. Cancelling the isomorphism induced
by $p'$ proves that pullback along $\iota'$ is an isomorphism in every
degree.
