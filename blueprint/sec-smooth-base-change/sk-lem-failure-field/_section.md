+++
id = "sk-lem-failure-field"
kind = "section"
title = "A failure is detected on the generic fibre"
order = 1391
uses = ["sk-def-bc"]
+++
*Lemma (sketch).*

(Stacks Project, Lemma 59.88.6, Tag `0F07`.) If
$\mathrm{BC}(f,n,q-1)$ holds but $\mathrm{BC}(f,n,q)$ fails, then
there is a counterexample over a field: $S'\to S$ affine,
$T=\Spec K$, $K$ a field, and a $\Z/n\Z$-sheaf $\mathcal F$ on
$\Spec K$ with
$f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ not an
isomorphism.

## Proof

Apply [sk-lem-minimal] to the property ``the chosen cokernel
element survives'' (an element $\xi$ of the stalk of
$R^qh_*e^{-1}\mathcal F$ at a geometric point $\bar x$ not in the
image): thickenings do not change the étale site; limits work by
the limit theorem for higher direct images; the closed–open split
uses the injectivity of [sk-prop-injectivity] applied to an
embedding $\mathcal F'\to j_*\mathcal J\oplus i_*i^{-1}\mathcal F'$
(with $\mathcal J$ injective on the open $V$), the exactness of
$i_*$ and $j_*$ for closed/open immersions, and the induction
hypothesis for the $j_*$-summand.

Uses: [sk-def-bc]
