+++
kind  = "proof"
of    = "lem-pur-co-smooth-etale-locality"
+++
Use the source cover and geometric points of [def-weil-scheme-morphism-properties]. The evaluation and inverse tensor object below are the ones supplied by [def-weil-derived-pullback-tensor-hom], [def-weil-derived-tensor].
Step 1: etale maps. For an etale $u$, the etale normalization
$Ru^!\simeq Lu^*$ of [def-weil-exceptional-inverse-image] is
natural and preserved by arbitrary base change, so all three conditions
of [def-pur-co-smoothness] are immediate
($\omega_u\simeq\Lambda$, $\theta_{u,K}$ is the identity, and
the base-change map is the canonical one).

Step 2: the dualizing object. Compose exceptional inverse images
(the [def-weil-exceptional-inverse-image] composition rule) to
obtain an isomorphism of already existing global objects

$$
Lu^*\omega_f=Ru^!Rf^!\Lambda_Y
\simeq R(fu)^!\Lambda_Y=\omega_{fu}.
$$

Tensor-invertibility is etale local: pull the evaluation map

$$
\omega_f\otimes^L\Lambda_X\operatorname{RHom}(\omega_f,\Lambda_X)\to\Lambda_X
$$

back to $U$; it becomes an isomorphism because $\omega_{fu}$ is
invertible, its cone is bounded constructible with zero geometric
stalks, hence zero ([def-weil-derived-cohomology-sheaves]).

Step 3: the canonical map. Pulling $\theta_{f,K}$ back to $U$
and using the isomorphism of Step 2 gives $\theta_{fu,K}$ (both are
written from the adjunction counit, and the counits for the ordinary
composite $fu$ are transitive); its cone is therefore zero after
pullback to the surjective etale cover, hence zero by the same stalk
argument (equivalently, by [lem-pur-etale-iso-descent]).

Step 4: base change. Fix an arbitrary base change $Y'\to Y$ and
pull the base-change comparison for $\omega_f$ back to
$U'=U\times_XX'$. Exceptional composition identifies it with the
base-change comparison for $\omega_{fu}$, an isomorphism by
hypothesis; its cone has zero geometric stalks. This proves all three
conditions without descending an object or a morphism in a derived
category.
