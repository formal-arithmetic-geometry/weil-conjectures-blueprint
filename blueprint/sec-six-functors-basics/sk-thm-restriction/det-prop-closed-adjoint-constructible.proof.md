+++
kind = "proof"
of    = "det-prop-closed-adjoint-constructible"
uses = ["sk-lem-formal-closed-support", "sk-prop-open-coefficients", "sk-prop-sf-existence"]
+++
Let $K\in\Dbc(X,\Lambda)$. The triangle above comes from the localization
sequence (Stacks, Tag 09AH) and exactness of $i_*$ (Stacks, Tag 09BM). Its
third term $Rj_*j^*K$ is bounded constructible by
[sk-prop-open-coefficients], so $i_*R\underline\Gamma_ZK$ is bounded
constructible. Applying $i^*$, and using $i^*i_*\simeq\mathrm{id}$ (Stacks, Tag
09AA), gives $R\underline\Gamma_ZK\in\Dbc(Z,\Lambda)$.

Both $i^!K$ and $R\underline\Gamma_ZK$ now lie in $\Loc(\Dbc(Z,\Lambda))$. For
$A$ in this category, $Ri_!=i_*$ and [sk-prop-sf-existence] give
$\Hom(A,i^!K)=\Hom(i_*A,K)$, with Hom groups in $\Loc(\Dbc(Z,\Lambda))$ and
$\Loc(\Dbc(X,\Lambda))$, and [sk-lem-formal-closed-support](1) gives the same
identity $\Hom(A,R\underline\Gamma_ZK)=\Hom(i_*A,K)$ in
$D(Z_{\mathrm{proét}},\Lambda)$ and $D(X_{\mathrm{proét}},\Lambda)$, whose full
subcategories these are. By the Yoneda lemma, $i^!K\simeq R\underline\Gamma_ZK$,
naturally in $K$.
