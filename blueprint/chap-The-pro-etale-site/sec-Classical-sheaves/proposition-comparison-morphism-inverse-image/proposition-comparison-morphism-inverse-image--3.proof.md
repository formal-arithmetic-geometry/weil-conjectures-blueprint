+++
kind = "proof"
of = "proposition-comparison-morphism-inverse-image--3"
order = 112006
uses = ["proposition-comparison-morphism-inverse-image--2", "definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-pro-etale-affines-form-basis"]
+++
First consider the presheaf left Kan extension defining $\nu_X^*$.
Maps from a cofiltered limit of quasi-compact, quasi-separated schemes
with affine transition maps to an étale $X$-scheme commute with that
limit, since the target is locally of finite presentation over $X$.
The corresponding colimit property for representable presheaves passes
to the left Kan extension.

On the affine pro-étale subsite, this presheaf is already a sheaf:
coverings descend to finite coverings at étale stages, and exactness of
filtered colimits in $A$ passes the sheaf condition to the limit.
Density of this subsite [proposition-pro-etale-affines-form-basis] shows
that sheafification does not change sections there. This proves the
claim when all the $U_i$ are affine.

In general, choose a stage $i_0$ and a finite affine open covering of
$U_{i_0}$, together with finite affine open coverings of its pairwise
intersections. Pull these opens back to all stages over $i_0$ and to $U$.
The transition maps are affine, so the resulting diagrams have affine
terms and satisfy the case just proved. These coverings give finite
$1$-hypercovers at each stage and at the limit. Apply the sheaf condition
to their finite diagrams of sections and commute filtered colimits with
finite limits in $A$. Finally, the category of stages over $i_0$ is
cofinal for these filtered colimits, giving the required colimit over
$I^{\mathrm{op}}$.
