+++
kind = "proof"
of = "sk-prop-p1-adjunction-rational"
uses = ["sk-prop-diagonal-tower", "sk-prop-geo-p1-adjunction", "sk-thm-sf-pf-field"]
+++
All products are over $Y$. Let
$p_1,p_2:\mathbf P^1_Y\times\mathbf P^1_Y\to\mathbf P^1_Y$ be the projections
and $\delta_\Lambda$, $\operatorname{Tr}$ the class and traces of
[sk-prop-diagonal-tower]. The unit and counit are defined as in
[sk-prop-geo-p1-adjunction]. For $M\in\Loc(\Dbc(\mathbf P^1_Y,\Lambda))$ the
unit is the morphism in $\Loc(\Dbc(\mathbf P^1_Y,\Lambda))$

$$
\eta_M:M=Rp_{2*}\Delta_*M\longrightarrow Rp_{2*}\bigl(p_1^*M(1)[2]\bigr)
\simeq q^*Rq_*M(1)[2],
$$

where $Rp_{2*}$ is the direct image
$\Loc(\Dbc(\mathbf P^1_Y\times\mathbf P^1_Y,\Lambda))\to\Loc(\Dbc(\mathbf P^1_Y,\Lambda))$,
the first arrow is $Rp_{2*}$ of $1\otimes\delta_\Lambda$ under
$\Delta_*M\simeq p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda_{\mathbf P^1_Y}$, and
the second is proper base change. The isomorphism
$\Delta_*M\simeq p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda_{\mathbf P^1_Y}$ holds
for every $M$: both sides restrict to $M$ on the diagonal and to $0$ on its
complement, and these two restrictions are jointly conservative (Stacks, Tag
09AD). For $K\in\Loc(\Dbc(Y,\Lambda))$ the counit is the morphism in
$\Loc(\Dbc(Y,\Lambda))$

$$
\varepsilon_K:Rq_*q^*K(1)[2]\simeq K\otimes^{\mathbf L}Rq_*\Lambda_{\mathbf P^1_Y}(1)[2]
\xrightarrow{1\otimes\operatorname{Tr}_q}K,
$$

using the projection formula.

The triangle identities are verified by the calculation in the proof of
[sk-prop-geo-p1-adjunction]. That calculation uses only the projection
formula, proper base change and composition of derived direct images, each
applied to the canonical maps, and these hold on $\Loc(\Dbc(-,\Lambda))$ by
[sk-thm-sf-pf-field]. It moves the factor $M$, respectively $q^*K$, outside
the direct image by the projection formula; the base change map, being
defined by the adjunction counit, cancels against restriction to the diagonal
and gives $Rp_{i*}\Delta_*=\mathrm{id}$. The result is the pair of equalities
of endomorphisms in $\Loc(\Dbc(Y,\Lambda))$ and
$\Loc(\Dbc(\mathbf P^1_Y,\Lambda))$

$$
\begin{aligned}
\varepsilon_{Rq_*M}\circ Rq_*(\eta_M)
&=Rq_*\bigl(1_M\otimes(\operatorname{Tr}_{p_1}\circ Rp_{1*}\delta_\Lambda)\bigr),\\
q^*(\varepsilon_K)(1)[2]\circ\eta_{q^*K(1)[2]}
&=1_{q^*K(1)[2]}\otimes(\operatorname{Tr}_{p_2}\circ Rp_{2*}\delta_\Lambda),
\end{aligned}
$$

where the projection formula for $p_i$ identifies the morphism in parentheses
with an endomorphism of $\Lambda_{\mathbf P^1_Y}$. By the integration
identities of [sk-prop-diagonal-tower] both endomorphisms are the identity, so
both triangle identities hold. Uniqueness of right adjoints gives
$q^!\simeq q^*(1)[2]$.
