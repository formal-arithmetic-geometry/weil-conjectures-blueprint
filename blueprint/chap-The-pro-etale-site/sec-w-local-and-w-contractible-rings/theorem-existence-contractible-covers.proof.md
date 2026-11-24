+++
kind = "proof"
of = "theorem-existence-contractible-covers"
order = 60
uses = ["proposition-etale-implications", "lemma-stability", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers"]
+++
The construction is that of [bhatt-scholze15, Theorem 2.4.9] and
[Stacks, [0983](https://stacks.math.columbia.edu/tag/0983)]. We first make the local rings strictly henselian, and
then replace the profinite space of components by an [extremally
disconnected](@definition-w-local-w-strictly-local) one surjecting onto it, which does not change the local
rings.

In the first stage we construct
a faithfully flat [ind-étale](@definition-ind-etale-pro-etale-weakly) $R$-algebra $C$ that is [w-strictly local](@definition-w-local-w-strictly-local).
To do so we first replace $R$ by an ind-Zariski algebra whose spectrum is
[w-local](@definition-w-local-w-strictly-local), and then take a filtered colimit of étale neighbourhoods of
the closed points, which makes the local rings at the closed points
strictly henselian. This is the construction of simultaneous strict
localizations in [Stacks, [097X](https://stacks.math.columbia.edu/tag/097X)]. Each step is a filtered colimit of
étale algebras, so $C$ is [ind-étale](@definition-ind-etale-pro-etale-weakly) over $R$ by
Lemma [lemma-stability].

For the second stage, choose a surjection
$S\to\pi_0(\operatorname{Spec}(C))$ with $S$ [extremally disconnected](@definition-w-local-w-strictly-local) using
Lemma [lemma-extremally-disconnected-covers], and realize this map by an ind-Zariski
$C$-algebra $D$ such that

$$
|\operatorname{Spec}(D)|
\simeq |\operatorname{Spec}(C)|
\times_{\pi_0(\operatorname{Spec}(C))}S
$$

as topological spaces. Concretely, write $S$ as a limit of finite
quotients, use finite products of $C$, restrict to the relevant
closed sets of components by idempotent localizations, and take a
filtered colimit; see [Stacks, [097D](https://stacks.math.columbia.edu/tag/097D)]. This construction identifies local
rings, is surjective when $S$ is, and preserves [w-locality](@definition-w-local-w-strictly-local). Hence
$C\to D$ is faithfully flat and the local rings at closed points of
$D$ remain strictly henselian. The space of components of
$\operatorname{Spec}(D)$ is $S$, so $D$ is
[w-contractible](@definition-w-local-w-strictly-local), and the composite $R\to C\to D$ is [ind-étale](@definition-ind-etale-pro-etale-weakly) and
faithfully flat.
