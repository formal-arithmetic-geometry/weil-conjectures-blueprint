+++
kind = "proof"
of = "lemma-reduction-curve-over-normal-base"
order = 677
uses = ["lemma-reduction-field", "lemma-integral-changes-source-base"]
+++
We first simplify the source of the direct image and the coefficients,
then show that the source of the base change map vanishes, and finally
replace the base by a normal one.

By Lemma [lemma-reduction-field] there is a failure with direct image
from the spectrum of a field $\Omega$. The map from the spectrum of an
algebraic closure of $\Omega$ to $\operatorname{Spec}\Omega$ is integral
and surjective, so by Lemma [lemma-integral-changes-source-base]
we may replace $\Omega$ by an algebraic closure. On this geometric point, a
sheaf of $\mathbf Z/n$-modules is a $\mathbf Z/n$-module, hence a direct
sum of cyclic groups $\mathbf Z/m$ with $m\mid n$. The base change map
commutes with this direct sum by continuity of qcqs direct images. Hence
base change still fails for some summand $\mathbf Z/m$.

The source of the base change map is the pullback of
$R^qf_*\underline{\mathbf Z/m}$ for $f:\operatorname{Spec}\Omega\to T$, and
we show that it is zero. The stalk of this sheaf at a geometric point
$\bar t$ of $T$ is the cohomology of
$\operatorname{Spec}\Omega\times_T\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{T,\bar t}$.
This scheme is a limit of étale $\Omega$-schemes. Since $\Omega$ is
algebraically closed, these are disjoint unions of copies of
$\operatorname{Spec}\Omega$. By continuity of cohomology the stalk vanishes
for $q\geq1$. As the source of the base change map is zero, the failure
means that the target $R^qh_*\underline{\mathbf Z/m}$ is nonzero.

The extension theorem for covers will require a normal base with
algebraically closed fraction field.
If the base is $\operatorname{Spec}B$, we replace it by
$\operatorname{Spec}R$, where $R$ is the integral closure in $\Omega$ of the
image of $B$. The morphism $\operatorname{Spec}\Omega\to\operatorname{Spec}B$
factors through $\operatorname{Spec}R$, and $\operatorname{Spec}R\to\operatorname{Spec}B$
is integral, so the failure persists by
Lemma [lemma-integral-changes-source-base].
The fraction field $L$ of $R$ is the algebraic closure of
$\operatorname{Frac}(\operatorname{im}(B\to \Omega))$ in $\Omega$, hence
algebraically closed. In general $\Omega/L$ is transcendental. We are now
in the situation of [Stacks, [0F08](https://stacks.math.columbia.edu/tag/0F08)].
