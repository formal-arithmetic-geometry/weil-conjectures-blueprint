+++
kind = "proof"
of = "sk-lem-nagata-boundary-divisor"
uses = ["sk-def-nagata-admissible"]
+++
Choose a quasi-coherent ideal $\mathcal I$ of finite type with
$V(\mathcal I)=T\setminus U$. Such an ideal exists because $U$ is a
quasi-compact open in a qcqs scheme [Stacks, Tag 01PH](https://stacks.math.columbia.edu/tag/01PH). We blow up this
ideal, and the extended ideal defines the exceptional Cartier divisor.
On the affine charts, its local equation $a$ is a nonzerodivisor, and
hence each chart ring injects into its localization at $a$. It follows
that the complement of the divisor, which is the inverse image of $U$,
is schematically dense.

This density persists under subsequent admissible blow-ups. To see this,
let $a$ be a local equation of the boundary divisor. Multiplication by $a$
is injective on each power of a further blow-up ideal, since those powers
are submodules of the structure sheaf of $T'$. Therefore multiplication by $a$ is injective
on the Rees algebra and on its localized charts in degree zero, and the
pullback of $a$ still defines a Cartier divisor whose complement is
the inverse image of $U$.
