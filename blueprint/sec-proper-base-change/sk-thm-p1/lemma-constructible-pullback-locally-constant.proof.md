+++
kind  = "proof"
of    = "lemma-constructible-pullback-locally-constant"
uses = ["lemma-constructible-pullback-constant"]
+++
*The localised site.* Let $\pi\colon U\to X$ be étale. An object of the
localised site is an étale $X$-scheme $V$ with an $X$-morphism $V\to U$;
this morphism is étale, since a morphism between étale $X$-schemes is étale,
so $V$ is an étale $U$-scheme. Conversely an étale $U$-scheme $W$ is an étale
$X$-scheme via $W\to U\xrightarrow{\pi}X$, with its structure map to $U$.
These assignments are mutually inverse on objects and morphisms and preserve
fibre products and jointly surjective families, so they give an equivalence
of sites between $\et X$ localised at $U$ and $\et U$. For an étale $U$-scheme
$W$, the pullback $\pi^*\mathcal F$ along the étale morphism $\pi$ has
$(\pi^*\mathcal F)(W)=\mathcal F(W\to U\to X)$, i.e. $\pi^*\mathcal F$ is the
restriction of $\mathcal F$ to the localised site transported along this
equivalence. An equivalence of sites carries constant sheaves to constant
sheaves, so the restriction is constant if and only if $\pi^*\mathcal F$ is.

*Pullback.* Let $(U_i\to X)_i$ be a trivialising datum for $\mathcal F$. The base
change $(U_i\times_XY\to Y)_i$ is an étale cover of $Y$, since étale
morphisms and jointly surjective families are stable under base change.
The restriction of $g^*\mathcal F$ to $\et{U_i\times_XY}$ is the pullback,
along the projection $g_i\colon U_i\times_XY\to U_i$, of the restriction
of $\mathcal F$ to $\et{U_i}$: pullback along $g$ followed by restriction to
the localised site equals restriction followed by pullback along $g_i$,
because both are the sheaf pullback along the composite of the base change
functors, which agree. By the first part, the restriction of $\mathcal F$ to $\et{U_i}$ is
constant, and pullbacks of constant sheaves are constant by
[lemma-constructible-pullback-constant]. By the first part again, $g^*\mathcal F$ restricted to the localised site
at $U_i\times_XY$ is constant. Hence
$(U_i\times_XY\to Y)_i$ is a trivialising datum for $g^*\mathcal F$.
