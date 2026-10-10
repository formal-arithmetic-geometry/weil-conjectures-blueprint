+++
id = "sk-lem-induction"
kind = "section"
title = "The induction step in relative dimension one"
order = 1414
uses = ["sk-def-bc", "sk-lem-universal-datum", "sk-thm-vanishing"]
lean = ["AlgebraicGeometry.Etale.UniversalBaseChangeProperty.of_forall_lt"]
+++
*Lemma (sketch).*

Let $f:X\to S$ be affine smooth of relative dimension one with $X$
affine, let $\Lambda$ be a commutative ring, and let $n$ be an integer
invertible on $S$ with $n\Lambda=0$. Let $q\ge1$. If
$\mathrm{BC}(f,\Lambda,q')$ holds universally for every $q'<q$
([sk-def-bc]), then $\mathrm{BC}(f,\Lambda,q)$ holds universally.

## Proof

*Contradiction.* Suppose $\mathrm{BC}(f,\Lambda,q)$ does not hold
universally: it fails for some base change $f_1:X_1=X\times_SS_1\to S_1$
of $f$. Being an isomorphism is local on the base, and restriction to an
open of $S_1$ is pullback along an étale map, with which the base-change
map commutes; so the failure persists over some affine open of $S_1$, and
we may assume $S_1$ affine. Then $f_1$ is affine smooth of relative
dimension one with $X_1$ affine (affine over the affine $S_1$),
$\mathrm{BC}(f_1,\Lambda,q')$ holds universally for every $q'<q$ (a base
change of $f_1$ is a base change of $f$), $n$ is invertible on $S_1$ and
$n\Lambda=0$, and $\mathrm{BC}(f_1,\Lambda,q)$ fails. By
[sk-lem-universal-datum] applied to $f_1$ there is a universal curve-test
datum: a base change $f':X'\to S'$ of $f_1$, hence of $f$, over an affine,
integral, normal $S'$ with algebraically closed fraction field, its fibre
$h:Y\to X'$ over a geometric generic point $\Spec K\to S'$, and an integer
$d\mid n$ invertible on $S'$ with $R^qh_*(\Lambda/d\Lambda)\neq0$. Being a
base change of $f$, $f'$ is affine smooth of relative dimension one, and
$X'$ is affine since $f'$ is affine and $S'$ is affine; so
[sk-thm-vanishing] applies to that datum and gives
$R^qh_*(\Lambda/d\Lambda)=0$. Contradiction.
