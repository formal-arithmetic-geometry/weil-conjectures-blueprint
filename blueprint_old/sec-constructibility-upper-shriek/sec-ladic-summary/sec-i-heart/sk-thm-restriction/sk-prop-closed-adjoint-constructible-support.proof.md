+++
kind = "proof"
of = "det-prop-closed-adjoint-constructible-support"
+++
For a sheaf (or K-injective complex) $I$, the sequence
$0\to i_*\underline\Gamma_ZI\to I\to j_*j^*I$ is exact, and it is exact on the
right when $I$ is injective ([Stacks, Tag 09AH](https://stacks.math.columbia.edu/tag/09AH)), since then $I\to j_*j^*I$ is
surjective. Applying this to a K-injective resolution of $K$ and using that
$i_*$ is exact ([Stacks, Tag 09BM](https://stacks.math.columbia.edu/tag/09BM)), so that $i_*R\underline\Gamma_Z$ is
computed termwise, gives the distinguished triangle; its maps are the counit
and unit, as $R\underline\Gamma_Z$ is the right adjoint of $i_*$
([sk-lem-formal-closed-support](1)).

The middle term $K$ is in $\Dbc(X,\Lambda)$ by hypothesis. The restriction
$j^*K$ lies in $\Dbc(U,\Lambda)$, and $Rj_*j^*K\in\Dbc(X,\Lambda)$ by
[sk-prop-open-coefficients] ($j$ is quasi-compact because $X$ is
Noetherian). Since $\Dbc(X,\Lambda)$ is a triangulated subcategory, the
fibre $i_*R\underline\Gamma_ZK$ lies in $\Dbc(X,\Lambda)$. Pullback preserves
$\Dbc$, and $i^*i_*\simeq\mathrm{id}$ ([Stacks, Tag 09AA](https://stacks.math.columbia.edu/tag/09AA)), so
$R\underline\Gamma_ZK\simeq i^*i_*R\underline\Gamma_ZK\in\Dbc(Z,\Lambda)$.
