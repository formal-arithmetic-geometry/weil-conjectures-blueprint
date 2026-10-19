+++
kind = "proof"
of = "sk-lem-universal-datum"
uses = ["sk-lem-failure-field", "sk-lem-sbc-integral-tests", "sk-prop-injectivity"]
+++
[sk-lem-failure-field] gives a failure with direct image
from the spectrum of a field $K$, and [sk-lem-sbc-integral-tests]
lets us replace $K$ by an algebraic closure. On this geometric point a
sheaf of $\mathbf Z/n$-modules is a $\mathbf Z/n$-module, hence a direct
sum of cyclic groups $\mathbf Z/d$ with $d\mid n$. The exchange map
commutes with this direct sum by continuity of qcqs direct images, so
some summand $\mathbf Z/d$ still fails. Its positive-degree direct image
from the geometric point vanishes, because every étale scheme over
the point is a disjoint union of copies of it. The source of the
exchange map is therefore zero, and the failure means that the target
$R^qh_*\underline{\mathbf Z/d}$ is nonzero.

If the base is $\operatorname{Spec}B$, replace it by
$\operatorname{Spec}A$, where $A$ is the integral closure in $K$ of the
image of $B$. The morphism $\operatorname{Spec}A\to\operatorname{Spec}B$
is integral, so [sk-lem-sbc-integral-tests] keeps the failure.
The fraction field $L$ of $A$ is the algebraic closure of
$\operatorname{Frac}(\operatorname{im}(B\to K))$ in $K$, hence
algebraically closed. In general $K/L$ is transcendental. This is the
situation of [Stacks, Tag 0F08](https://stacks.math.columbia.edu/tag/0F08).

*Complement.* In the notation of [sk-def-bc]:

*Step 1 (a failure over a field).* By [sk-lem-failure-field] there are
an affine $S_1$ with a morphism $S_1\to S$, the base change
$f_1:X_1\to S_1$ of $f$, a field $K_0$ with $g_0:\Spec K_0\to S_1$, and a
sheaf $\mathcal F_0$ of $\Lambda$-modules on $(\Spec K_0)_{\Et}$ for which
the degree-$q$ base-change map of $f_1$ along $g_0$ is not an isomorphism.

*Step 2 (algebraically closed field).* Let $K$ be an algebraic closure of
$K_0$; $\pi:\Spec K\to\Spec K_0$ is integral and surjective. Since
$\mathrm{BC}(f_1,\Lambda,q-1)$ holds (part of the universal hypothesis), the
base-change map in degree $q$ is injective, and the integral surjective
base-change lemma of this subsection shows that the failure persists
for the square of $f_1$ along $g_0\circ\pi$ and the sheaf
$\pi^{-1}\mathcal F_0$: surjectivity on a geometric point makes the same
cokernel element survive.

*Step 3 (normal base).* Let $A_1=\Gamma(S_1,\mathcal O_{S_1})$ and let $B$ be
the integral closure of the image of $A_1$ in $K$; put $S'=\Spec B$. Then
$S'$ is affine, integral and normal, its fraction field $L$ is the
algebraic closure in $K$ of the fraction field of the image of $A_1$, hence
algebraically closed, $S'\to S_1$ is integral, and $\Spec K\to S_1$
factors as the geometric generic point $g:\Spec K\to S'$ followed by
$S'\to S_1$. Higher direct images along integral morphisms vanish, so the
integral base-change lemma of this subsection identifies the base-change map
of $f_1$ along $\Spec K\to S_1$ with that of the base change
$f':X'=X\times_SS'\to S'$ along $g$; hence the latter, for
$\mathcal F=\pi^{-1}\mathcal F_0$, is not an isomorphism.

*Step 4 (the target is nonzero).* $\mathrm{BC}(f',\Lambda,q-1)$ holds by the
universal hypothesis, so by [sk-prop-injectivity] (1) the base-change map
$f'^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ is injective. It is not
an isomorphism, so its target $R^qh_*e^{-1}\mathcal F$ is nonzero.

*Step 5 (constant coefficients $\Lambda/d\Lambda$).* As $K$ is algebraically
closed, $\mathcal F$ is the constant sheaf with value the $\Lambda$-module
$M=\mathcal F(\Spec K)$, so $e^{-1}\mathcal F$ is the constant sheaf $M$
on $Y$. The higher direct images of a sheaf of $\Lambda$-modules are those of
its underlying abelian sheaf, and $R^qh_*$ commutes with direct sums because
$h$ is quasi-compact and quasi-separated (it is affine, as a base change of
the affine $f$). Since $n\Lambda=0$, $M$ is an abelian group of exponent
dividing $n$, hence a direct sum of cyclic groups $\Z/\ell^k$ with $\ell$
prime and $\ell^k\mid n$; so $R^qh_*(\Z/\ell^k)\neq0$ for one of them, and
the exact sequences $0\to\Z/\ell^{j-1}\to\Z/\ell^j\to\Z/\ell\to0$ give
$R^qh_*(\Z/\ell)\neq0$ for that prime $\ell\mid n$. The element of order
$\ell$ of $M$ in that summand shows that $\ell$ is not a unit of $\Lambda$,
so $\Lambda/\ell\Lambda$ is a nonzero $\mathbf F_\ell$-vector space; as an
abelian sheaf the constant sheaf $\Lambda/\ell\Lambda$ is a nonzero direct
sum of copies of $\Z/\ell$, and therefore
$R^qh_*(\Lambda/\ell\Lambda)\neq0$. Put $d=\ell$; it divides $n$, so it is
invertible on $S$ and on $S'$.

*Step 6 (the datum).* $S'\to S$ is the composite $S'\to S_1\to S$, and
$f'$ is the base change of $f$ along it; affineness, smoothness and relative
dimension one are stable under base change, so $f'$ is affine and smooth of
relative dimension one. This is the datum of the statement.
