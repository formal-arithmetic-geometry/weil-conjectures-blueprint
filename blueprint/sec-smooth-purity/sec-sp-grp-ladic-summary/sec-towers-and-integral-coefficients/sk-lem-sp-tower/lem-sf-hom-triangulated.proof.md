+++
kind  = "proof"
of    = "lem-sf-hom-triangulated"
+++
Choose a K-injective resolution $I\to M$, which exists by
[prop-weil-pbc-kinjective-resolutions-exist] and
[def-sp-kinjective-bridge]. By
[def-weil-derived-pullback-tensor-hom] the object
$R\mathcal Hom_A(K,M)$ is represented by the Hom-complex
$\mathcal Hom^\bullet_A(K,I)$, and represent the first variable by a
complex of the same name. The Hom-complex of complexes of modules is
triangulated in each variable: the standard termwise identity
$\operatorname{Hom}^\bullet(\operatorname{Cone}(u),I)\cong \operatorname{Cone}(\operatorname{Hom}^\bullet(u,I))[-1]$ exhibits the
first sequence as a triangle, and the identity
$\operatorname{Hom}^\bullet(K,\operatorname{Cone}(v))\cong \operatorname{Cone}(\operatorname{Hom}^\bullet(K,v))$, valid because a
complex of injectives is degreewise injective, exhibits the second. This
is the basic homological algebra of the Hom-complex, and it applies to the
sheaves of [def-weil-pbc-etale-site] termwise because the Hom-complex
is formed degreewise in the abelian category of module sheaves.
