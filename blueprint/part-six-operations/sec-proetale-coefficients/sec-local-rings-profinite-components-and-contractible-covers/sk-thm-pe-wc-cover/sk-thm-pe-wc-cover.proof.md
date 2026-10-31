+++
kind = "proof"
of = "sk-thm-pe-wc-cover"
+++
The construction is that of (BS, Theorem 2.4.9) and
[Stacks, Tag 0983](https://stacks.math.columbia.edu/tag/0983). We first make the local rings strictly henselian, and
then replace the profinite space of components by an extremally
disconnected one surjecting onto it, which does not change the local
rings. In the first stage we construct
a faithfully flat ind-étale $R$-algebra $C$ that is w-strictly local.
To do so we first replace $R$ by an ind-Zariski algebra whose spectrum is
w-local, and then take a filtered colimit of étale neighbourhoods of
the closed points, which makes the local rings at the closed points
strictly henselian. This is the construction of simultaneous strict
localizations in [Stacks, Tag 097X](https://stacks.math.columbia.edu/tag/097X). Each step is a filtered colimit of
étale algebras, so $C$ is ind-étale over $R$ by
Lemma [sk-lem-pe-weakly-etale-stability].

For the second stage, choose a surjection
$S\to\pi_0(\operatorname{Spec}(C))$ with $S$ extremally disconnected using
Proposition [sk-prop-pe-stonean], and realize this map by an ind-Zariski
$C$-algebra $D$ such that

$$
|\operatorname{Spec}(D)|
\simeq |\operatorname{Spec}(C)|
\times_{\pi_0(\operatorname{Spec}(C))}S
$$

as topological spaces. Concretely, write $S$ as a limit of finite
quotients, use finite products of $C$, restrict to the relevant
closed sets of components by idempotent localizations, and take a
filtered colimit; see [Stacks, Tag 097D](https://stacks.math.columbia.edu/tag/097D). This construction identifies local
rings, is surjective when $S$ is, and preserves w-locality. Hence
$C\to D$ is faithfully flat and the local rings at closed points of
$D$ remain strictly henselian. The space of components of
$\operatorname{Spec}(D)$ is $S$, so $D$ is
w-contractible, and the composite $R\to C\to D$ is ind-étale and
faithfully flat.
