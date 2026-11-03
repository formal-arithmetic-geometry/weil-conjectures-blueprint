+++
kind = "proof"
of = "det-formal-closed-support-ii-left-exact"
+++
By part (1) of [sk-lem-formal-closed-support], $R\underline\Gamma_Z$ is right adjoint to
$i_*\colon\D(Z_{\mathrm{proét}},\Lambda)\to\D(X_{\mathrm{proét}},\Lambda)$. The functor $i_*$ on sheaves is exact
([Stacks, Tag 09BM](https://stacks.math.columbia.edu/tag/09BM)), so its derived functor is $i_*$ applied termwise and carries
$\D^{\leq -1}(Z_{\mathrm{proét}},\Lambda)$ into $\D^{\leq-1}(X_{\mathrm{proét}},\Lambda)$.

Let $K\in\D^{\geq0}(X_{\mathrm{proét}},\Lambda)$. For every $A\in\D^{\leq-1}(Z_{\mathrm{proét}},\Lambda)$,

$$
\Hom(A,R\underline\Gamma_ZK)=\Hom(i_*A,K)=0,
$$

since $i_*A\in\D^{\leq-1}$ and $K\in\D^{\geq0}$. Taking $A=\tau_{\leq-1}R\underline\Gamma_ZK$, the
truncation map is zero, so $\tau_{\leq-1}R\underline\Gamma_ZK=0$ and
$R\underline\Gamma_ZK\in\D^{\geq0}$.

The open restriction $u^*$ is exact on sheaves, hence $t$-exact on derived categories, so
$u^*R\underline\Gamma_ZK\in\D^{\geq0}(S_{\mathrm{proét}},\Lambda)$ as well.
