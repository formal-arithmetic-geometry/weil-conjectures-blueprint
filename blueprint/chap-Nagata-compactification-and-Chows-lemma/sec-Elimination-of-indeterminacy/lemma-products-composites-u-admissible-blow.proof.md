+++
kind = "proof"
of = "lemma-products-composites-u-admissible-blow"
order = 1431
uses = ["lemma-schematic-closure-uniqueness"]
+++
All three assertions are statements about ideals, because products of ideals
dominate blow-ups, composites are computed by products of ideals, and
extension from an open amounts to extending a quasi-coherent ideal of
finite type.
Let $\mathcal I,\mathcal J$ be ideals, both equal to $\mathcal O$ on
$U$, so that their product is too. Then the blow-up of their product
factors through both blow-ups. Indeed, on it the product
$\mathcal I\mathcal J$ is invertible, hence so is each factor, and the
universal property of each blow-up then gives the factorization. The
first assertion follows by induction. For the second, blowing up first $\mathcal I$ and
then the pullback of $\mathcal J$ yields the blow-up of
$\mathcal I\mathcal J$ [Stacks, [080A](https://stacks.math.columbia.edu/tag/080A)], which proves the composition
assertion when the second center is pulled back from $T$. In general, however, the second center
lives only on the first blow-up, and the composite is a blow-up of $T$
by the calculation with ideals of finite type in [Stacks, [080B](https://stacks.math.columbia.edu/tag/080B)].
For the extension assertion we extend a quasi-coherent ideal of finite
type from a quasi-compact open, keeping the center outside $U$; such
an extension exists because on a qcqs scheme every quasi-coherent
sheaf is the union of its quasi-coherent subsheaves of finite type, and the
precise result on admissible extensions is
[Stacks, [080M](https://stacks.math.columbia.edu/tag/080M)].
