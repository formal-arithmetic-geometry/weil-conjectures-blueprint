+++
id = "sk-lem-failure-field"
kind = "section"
title = "A failure is detected on the generic fibre"
order = 1387
uses = ["sk-def-bc"]
lean = ["AlgebraicGeometry.Etale.FieldFailure", "AlgebraicGeometry.Etale.nonempty_fieldFailure"]
+++
*Lemma (sketch).*

(Stacks Project, Lemma 59.88.6, Tag `0F07`.) If
$\mathrm{BC}(f,n,q-1)$ holds but $\mathrm{BC}(f,n,q)$ fails, then
there is a counterexample over a field: $S'$ an affine scheme (so that
$S'\to S$ is an affine morphism when $S$ is separated),
$T=\Spec K$, $K$ a field, and a $\Z/n\Z$-sheaf $\mathcal F$ on
$\Spec K$ with
$f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ not an
isomorphism.

## Proof

Let $g:T\to S$, $\mathcal F$ be a failing datum, so $g$ is a
quasi-compact quasi-separated *morphism* ([sk-def-bc]) but $T$
need not be a qcqs scheme, as [sk-lem-minimal] requires. Being an
isomorphism is local on $X$, and restriction to an affine open
$S'\subseteq S$ is pullback along an étale map, with which
$R^qg_*$, $R^qh_*$ and the base-change map commute; so the map already
fails over some affine open $S'$, and replacing $S$ by $S'$, $X$ by
$X\times_SS'$ and $T$ by $T\times_SS'$ we may assume $S$ affine (this
is the $S'$ of the statement). Now $T$, being qcqs over the affine
$S$, is a qcqs scheme. Apply [sk-lem-minimal] to the property ``the chosen cokernel
element survives'' (an element $\xi$ of the stalk of
$R^qh_*e^{-1}\mathcal F$ at a geometric point $\bar x$ not in the
image): it fails for the empty scheme, over which the stalk of
$R^qh_*e^{-1}\mathcal F$ is $0$, so the image of $\xi$ is $0$ and
lies in the image; thickenings do not change the étale site; limits work by
the limit theorem for higher direct images; the closed–open split
uses the injectivity of [sk-prop-injectivity] applied to an
embedding $\mathcal F'\to j_*\mathcal J\oplus i_*i^{-1}\mathcal F'$
(with $\mathcal J$ injective on the open $V$), the exactness of
$i_*$ and $j_*$ for closed/open immersions, and the induction
hypothesis for the $j_*$-summand.

Uses: [sk-def-bc]
