+++
kind = "proof"
of = "lemma-coherent-base-change-invertible-sheaves"
order = 1531
uses = ["definition-constructible-sheaves", "lemma-acyclic-resolutions", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "theorem-chow-s-lemma-projective-form"]
+++
This is base change for coherent cohomology along a proper morphism,
applied to a flat finitely presented module, together with the openness
criterion for a perfect complex (see [Stacks, [0B91](https://stacks.math.columbia.edu/tag/0B91), [0B9S](https://stacks.math.columbia.edu/tag/0B9S)]).
To construct the complex, one may use a projective embedding,
sufficiently large twists and a finite affine Čech complex; by Serre
vanishing we then obtain models that are finite locally free.
Given such a model, openness follows from a calculation with matrices. Indeed, near a point $t$
where the derived fibre of the complex has cohomology only in degree
$0$, of dimension $1$, we may cancel the differentials that are
invertible at $t$, and what remains is an invertible module in
degree $0$.

This proves the lemma for locally Noetherian $T$. If $T$ is an arbitrary
$k$-scheme, then locally on $T$ the sheaf $\mathcal L$ is pulled back from
$C_{T_0}$ for some $k$-scheme $T_0$ of finite type, and the base change
isomorphism for $T\to T_0$ reduces every assertion to $T_0$. The open
locus is the preimage of the locus for $T_0$, and by base change it does
not depend on $T_0$.
