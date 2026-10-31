+++
kind = "proof"
of = "sk-lem-universal-datum"
uses = ["sk-lem-failure-field", "sk-lem-sbc-integral-tests", "sk-prop-injectivity"]
+++
By Lemma [sk-lem-failure-field] there is a failure with direct image
from the spectrum of a field $\Omega$, and by Lemma [sk-lem-sbc-integral-tests]
we may replace $\Omega$ by an algebraic closure. On this geometric point, a
sheaf of $\mathbf Z/n$-modules is a $\mathbf Z/n$-module, hence a direct
sum of cyclic groups $\mathbf Z/m$ with $m\mid n$. The base change map
commutes with this direct sum by continuity of qcqs direct images, and so
base change still fails for some summand $\mathbf Z/m$. The source of the
base change map is the pullback of $R^qf_*\underline{\mathbf Z/m}$ for
$f:\operatorname{Spec}\Omega\to T$. The stalk of this sheaf at a geometric point $\bar t$
of $T$ is the cohomology of
$\operatorname{Spec}\Omega\times_T\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{T,\bar t}$,
which is a limit of étale $\Omega$-schemes. Since $\Omega$ is algebraically closed,
these are disjoint unions of copies of $\operatorname{Spec}\Omega$, and by
continuity of cohomology the stalk vanishes for $q\geq1$.
Therefore the source of the base change map is zero, and the failure means that
the target $R^qh_*\underline{\mathbf Z/m}$ is nonzero.

If the base is $\operatorname{Spec}B$, we replace it by
$\operatorname{Spec}R$, where $R$ is the integral closure in $\Omega$ of the
image of $B$. Since the morphism $\operatorname{Spec}R\to\operatorname{Spec}B$
is integral, the failure persists by Lemma [sk-lem-sbc-integral-tests].
The fraction field $L$ of $R$ is the algebraic closure of
$\operatorname{Frac}(\operatorname{im}(B\to \Omega))$ in $\Omega$, hence
algebraically closed, while in general $\Omega/L$ is transcendental. This is the
situation of [Stacks, Tag 0F08](https://stacks.math.columbia.edu/tag/0F08).
