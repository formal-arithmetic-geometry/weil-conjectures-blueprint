+++
kind = "proof"
of = "det-prop-closed-adjoint-constructible-yoneda"
+++
By [det-prop-closed-adjoint-constructible-support],
$R\underline\Gamma_ZK\in\Dbc(Z,\Lambda)\subset\Loc(\Dbc(Z,\Lambda))$. For a
closed immersion the trivial compactification gives $Ri_!=i_*$ on the
localizing categories, so for every $A\in\Loc(\Dbc(Z,\Lambda))$ the adjunction
of [sk-prop-sf-existence] gives a bijection, natural in $A$ and $K$,
$\Hom(A,i^!K)\simeq\Hom(i_*A,K)$, induced by the counit. The adjunction
$i_*\dashv R\underline\Gamma_Z$ of [sk-lem-formal-closed-support](1) gives a
bijection $\Hom(A,R\underline\Gamma_ZK)\simeq\Hom(i_*A,K)$, also induced by
the counit, with Hom groups in $D(Z_{\mathrm{proét}},\Lambda)$ and
$D(X_{\mathrm{proét}},\Lambda)$. The categories $\Loc(\Dbc(-,\Lambda))$ are
full subcategories of these, so both bijections are between the same groups.
Thus $i^!K$ and $R\underline\Gamma_ZK$ represent the same functor on
$\Loc(\Dbc(Z,\Lambda))$, and the Yoneda lemma gives a unique isomorphism
$i^!K\simeq R\underline\Gamma_ZK$ compatible with the counits; uniqueness
makes it natural in $K$. In particular $i^!K\in\Dbc(Z,\Lambda)$.
