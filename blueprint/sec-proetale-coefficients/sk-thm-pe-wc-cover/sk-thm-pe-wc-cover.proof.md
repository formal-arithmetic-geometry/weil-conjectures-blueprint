+++
kind = "proof"
of = "sk-thm-pe-wc-cover"
+++
*Construction and its algebraic inputs.* The construction has two stages, following
Bhatt–Scholze, Theorem 2.4.9, and Stacks, Tag 0983. The first constructs a faithfully flat
ind-étale $R$-algebra $C$ that is w-strictly local: w-localize using finite Zariski
decompositions ([def-weil-pbc-w-localization], [lem-weil-pbc-w-localization-points]),
adjoin solutions to étale lifting problems in a filtered construction
([def-weil-pbc-etale-contraction], [lem-weil-pbc-etale-contraction]), and then refine the
w-localization so that the local rings at closed points are strictly henselian
([def-weil-pbc-retained-localization], [lem-weil-pbc-retained-localization]). This is the
simultaneous strict-localization construction of Stacks, Tag 097X, recorded as
$C=C_R$ in [def-weil-pbc-strict-w-cover] and [lem-weil-pbc-strict-w-cover]. The finite
stages are what make the result ind-étale.

For the second stage, choose a Stonean surjection $S\to\pi_0(\operatorname{Spec}(C))$ using
[sk-prop-pe-stonean], and realize this map by an ind-Zariski $C$-algebra $D$ such that

$$
|\operatorname{Spec}(D)|\simeq|\operatorname{Spec}(C)|\times_{\pi_0(\operatorname{Spec}(C))}S
$$

as topological spaces. Concretely, write $S$ as a limit of finite quotients, use finite
products of $C$, restrict to the relevant closed sets of components by idempotent
localizations, and take a filtered colimit (Stacks, Tag 097D). This construction identifies
local rings, is surjective when $S$ is, and preserves w-locality. Hence $C\to D$ is
faithfully flat and the local rings at closed points of $D$ remain strictly henselian. Its
component space is $S$, so $D$ is w-contractible, and the composite $R\to C\to D$ is
ind-étale and faithfully flat by [sk-lem-pe-weakly-etale-stability]. The second stage is
[det-pe-wc-cover-second-stage].
