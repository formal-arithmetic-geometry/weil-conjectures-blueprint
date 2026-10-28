+++
kind = "proof"
of = "sk-prop-p1-adjunction-rational"
uses = ["sk-prop-geo-p1-adjunction", "sk-thm-sf-pf-field", "sk-prop-proper-base-change-unbounded", "sk-prop-diagonal-tower"]
+++
Define the unit and counit by the formulas of [sk-prop-geo-p1-adjunction], using
$\Delta_*M\simeq p_1^*M\otimes^{\mathbf L}\Delta_*\Lambda$
([Stacks, Tag 09AD](https://stacks.math.columbia.edu/tag/09AD)) and $\delta_\Lambda$,
$\operatorname{Tr}_q$. The torsion calculation uses only the projection formula and proper
base change, which hold here by [sk-thm-sf-pf-field] and
[sk-prop-proper-base-change-unbounded], and it reduces the triangle identities to the
identities $\operatorname{Tr}_{p_i}\circ Rp_{i*}(\delta_\Lambda)=1$ of
[sk-prop-diagonal-tower]. Uniqueness of adjoints gives the last claim.
