+++
id = "sk-l-dl-general-quasifinite"
kind = "section"
title = "Quasi-finite morphisms"
order = 2817
lean = ["AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite", "AlgebraicGeometry.LAdicWeilSheaf.IsMixedOfWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.LAdicWeilSheaf.HasWeightsAtMost.higherLowerShriek_zero_of_quasiFinite"]
uses = ["sk-d-dl-general-weights", "sk-prop-sf-cbc"]
+++
*Lemma (sketch).*

Let $f_0:X_0\to Y_0$ be a separated, quasi-finite morphism of finite
type of $k_0$-schemes, with $Y_0$ quasi-separated of finite type over
$k_0$. Then $R^if_{0!}F=0$ for every Weil sheaf $F$ and every $i>0$;
and if $F$ is $\iota$-mixed of weights at most $w$ (resp. has all local
Frobenius eigenvalues of weight at most $w$), then so is (resp. has)
$f_{0!}F=R^0f_{0!}F$.

## Proof

Compact-support base change identifies the stalks with cohomology of a
finite geometric fiber, concentrated in degree zero. Thus $f_{0!}$ is
exact. At a closed point $y$, Frobenius permutes the stalk summands.
For an orbit of length $e$, an eigenvalue $\alpha$ upstairs gives
eigenvalues $\beta$ downstairs with $\beta^e=\alpha$; since
$q_x=q_y^e$, their normalized weights agree. Hence an upper bound $w$
on the weights of all local Frobenius eigenvalues of $F$ passes to
$f_{0!}F$, pure sheaves stay pure, and exactness transports a mixed
filtration.
