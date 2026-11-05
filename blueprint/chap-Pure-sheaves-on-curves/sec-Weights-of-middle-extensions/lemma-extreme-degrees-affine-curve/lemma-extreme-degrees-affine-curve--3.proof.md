+++
kind = "proof"
of = "lemma-extreme-degrees-affine-curve--3"
order = 1186006
uses = ["lemma-extreme-degrees-affine-curve--2", "proposition-weights-under-usual-operations", "lemma-degree-zero-top-cohomology"]
+++
Put $W=H^0(U,F^\vee)^\vee$ as in
[lemma-extreme-degrees-affine-curve--2]. Lean first uses
`AlgebraicGeometry.WeilSheaf.isPureOfWeightOver_geometricCoinvariants`
to show that $W$ is $\iota$-pure of weight $w$. Indeed, if $\beta$
is an eigenvalue on $H^0(U,F^\vee)$, the corresponding nonzero
morphism from a constant Weil twist has nonzero image at some
closed point $x$. Thus $\beta^{\deg(x)}$ is an eigenvalue on
$(F^\vee)_{\bar x}$. Purity of the dual gives
$|\iota(\beta)|=q^{-w/2}$, and dualizing gives weight $w$ on $W$.
This supplies the coinvariant weight calculation underlying
[lemma-degree-zero-top-cohomology].

The twist $(-1)$ multiplies Frobenius eigenvalues by $q$, raising
the weight to $w+2$ ([proposition-weights-under-usual-operations]);
Lean uses `FrobeniusModule.IsPureOfWeight.tateTwist`. Transport this
purity across the isomorphism of
[lemma-extreme-degrees-affine-curve--2], using
`FrobeniusModule.IsPureOfWeight.of_equiv`.
