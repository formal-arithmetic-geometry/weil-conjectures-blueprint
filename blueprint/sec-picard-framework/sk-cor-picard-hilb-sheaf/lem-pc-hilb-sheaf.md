+++
id = "lem-pc-hilb-sheaf"
kind = "lemma"
title = "$\\operatorname{Hilb}^d$ is an fppf sheaf"
order = 778
uses = ["def-pc-finite-locally-free", "def-pc-fppf-site", "def-pc-hilb-functor"]
+++
(Picard Schemes of Curves, Lemma 44.2.1, Tag
[0B95](https://stacks.math.columbia.edu/tag/0B95), which asserts the
sheaf property for the fpqc topology; the fppf case asserted here is the
consequence of it used below.) Let $X\to S$ be
a morphism of schemes and $d\geq0$. The functor
$\operatorname{Hilb}^d_{X/S}$ satisfies the sheaf
property for the fppf topology.

## Proof

Let $\{T_i\to T\}_{i\in I}$ be an fppf covering of schemes over $S$
([def-pc-fppf-site]; an fppf covering is flat, locally of finite
presentation and surjective, hence faithfully flat: it is an fpqc
covering in particular) and let $Z_i\in\operatorname{Hilb}^d_{X/S}(T_i)$ be objects
such that $Z_i$ and $Z_{i'}$ map to the same element of
$\operatorname{Hilb}^d_{X/S}(T_i\times_TT_{i'})$; say $Z_i$ corresponds to a closed
subscheme $\varphi_i:Z_i\hookrightarrow X_{T_i}$ (the definition
[def-pc-hilb-functor]) and the compatibility means: the two
pullbacks of $\varphi_i$ and $\varphi_{i'}$ to
$X_{T_i\times_TT_{i'}}$ are equal (in particular their composite
closed subschemes agree). Note that
$\{X_{T_i}\to X_T\}_{i\in I}$ is an fpqc covering of $X_T$ (base
change of an fpqc covering; the standard statement) and that
$X_{T_i\times_TT_{i'}}=X_{T_i}\times_{X_T}X_{T_{i'}}$. By effective
descent for closed immersions (Descent, Lemma 35.37.2, Tag
[03I0](https://stacks.math.columbia.edu/tag/03I0); the classical
statement: closed subschemes form an fpqc sheaf) there is a closed
immersion $\varphi:Z\hookrightarrow X_T$ whose base change along
$X_{T_i}\to X_T$ is $\varphi_i$ for every $i$: this uses exactly the
given compatibility of the $Z_i$'s over the double intersections.
The morphism $Z\to T$ then has base change $Z_i\to T_i$, which is
finite locally free of degree $d$ ([def-pc-finite-locally-free]);
the property of being finite locally free of a given degree descends
along fpqc coverings (Descent, Lemma 35.23.32, Tag
[02VO](https://stacks.math.columbia.edu/tag/02VO): the
classical: finite flat of finite presentation is of fpqc-local nature
on the target, and the rank is locally constant and can be detected
on a covering), so $Z\to T$ is finite locally free of degree $d$: thus
$Z\in\operatorname{Hilb}^d_{X/S}(T)$. Uniqueness up to unique isomorphism is the
corresponding uniqueness in the descent statements; hence $\operatorname{Hilb}^d$
satisfies the sheaf property for fppf coverings.
