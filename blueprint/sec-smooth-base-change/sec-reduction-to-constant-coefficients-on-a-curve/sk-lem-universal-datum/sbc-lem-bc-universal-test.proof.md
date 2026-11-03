+++
kind  = "proof"
of    = "sbc-lem-bc-universal-test"
+++
By [sbc-lem-bc-failure-field] there are a morphism $S'\to S$ with
$S'$ affine, the base change $f':X'\to S'$, a field $K$ with a morphism
$T=\operatorname{Spec}K\to S'$, and a sheaf $\mathcal F$ on $T$
annihilated by $n$ for which the degree-$q$ base-change map of $f'$
along $T\to S'$ is not an isomorphism. By
[sbc-lem-bc-integral-surjective] (whose hypothesis, $\mathrm{BC}(f,n,q-1)$
universally, is part of ours) applied to
the base change $\pi:\operatorname{Spec}K'\to\operatorname{Spec}K$
to an algebraic closure $K'$ of $K$ (an integral surjective morphism),
we may assume $K$ is algebraically closed. A sheaf of
$\mathbf Z/n\mathbf Z$-modules on a geometric point is a direct sum of
copies of $\mathbf Z/d\mathbf Z$ for varying $d\mid n$, so by the
finite direct-sum and retract case of the map, we may assume
$\mathcal F$ is constant with value $\mathbf Z/d\mathbf Z$ for some
$d\mid n$ (the cokernel of the base-change map
$\bigl(R^qh_*(c)\bigr)$ decomposes accordingly). Finally, by
[sbc-lem-bc-integral-base] applied to
$\pi:S''\to S'$ the normalization of $S'$ in
$\operatorname{Spec}K$ (integral: the integral closure of the normal
domain $A'$ in $K$ is integral over $A'$, commutative algebra),
with $X''=X'\times_{S'}S''$, we may replace $S'$ by $S''$, which is
affine, integral, and normal with algebraically closed function field
$K$; this is the datum of the statement.
