+++
id = "sk-lem-failure-field"
kind = "lemma"
title = "A failure is detected on the generic fibre"
order = 1387
uses = ["sk-def-bc"]
lean = ["AlgebraicGeometry.Etale.FieldFailure", "AlgebraicGeometry.Etale.nonempty_fieldFailure"]
tags = ["sketch"]
+++
Let $f:X\to S$ be a morphism of schemes, $\Lambda$ a commutative ring,
and $q\ge1$. If $\mathrm{BC}(f,\Lambda,r)$ holds universally for every
$r\le q-1$ ([sk-def-bc]: base change in all degrees $\le q-1$, after
every preliminary base change of $f$) but $\mathrm{BC}(f,\Lambda,q)$ does
not hold, then there is a counterexample over a field: a morphism
$S'\to S$ with $S'$ an affine scheme (so that $S'\to S$ is an affine
morphism when $S$ is separated), the base change
$f':X'=X\times_SS'\to S'$, a field $K$ with a morphism
$g:\Spec K\to S'$, the Cartesian square of $f'$ along $g$ with
$Y=X'\times_{S'}\Spec K$, $h:Y\to X'$, $e:Y\to\Spec K$, and a sheaf
$\mathcal F$ of $\Lambda$-modules on $(\Spec K)_{\Et}$ with
$f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ not an
isomorphism.

The hypothesis in degrees $\le q-1$ has to be the universal one: the
closed–open step of the proof applies it to a base change of $f$.
