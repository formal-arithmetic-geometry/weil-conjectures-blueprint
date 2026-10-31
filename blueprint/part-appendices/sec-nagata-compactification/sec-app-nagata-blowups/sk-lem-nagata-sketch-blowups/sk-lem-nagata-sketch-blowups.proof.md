+++
kind = "proof"
of = "sk-lem-nagata-sketch-blowups"
uses = ["sk-lem-nagata-sketch-closure", "sk-def-nagata-admissible"]
+++
Let $\mathcal I,\mathcal J$ be ideals. The blow-up of their product
factors through both blow-ups. Indeed, on the blow-up of
$\mathcal I\mathcal J$ the product is invertible, and hence so is each
factor, and the factorization follows from the universal property of
each blow-up. More explicitly, blowing up first $\mathcal I$ and then
the pullback of $\mathcal J$ yields the blow-up of
$\mathcal I\mathcal J$ [Stacks, Tag 080A](https://stacks.math.columbia.edu/tag/080A). The first assertion follows by
induction. The same fact proves the composition assertion when the
second center is pulled back from $T$. In general the second center
lives only on the first blow-up, and the composite is a blow-up of $T$
by the calculation with ideals of finite type in [Stacks, Tag 080B](https://stacks.math.columbia.edu/tag/080B).
For the extension assertion we extend a quasi-coherent ideal of finite
type from a quasi-compact open, keeping the center outside $U$. The
precise result on admissible extensions is
[Stacks, Tag 080M](https://stacks.math.columbia.edu/tag/080M).
