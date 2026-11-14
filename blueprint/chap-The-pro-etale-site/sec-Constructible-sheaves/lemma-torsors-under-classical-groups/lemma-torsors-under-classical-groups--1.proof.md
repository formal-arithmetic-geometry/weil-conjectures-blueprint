+++
kind = "proof"
of = "lemma-torsors-under-classical-groups--1"
order = 143002
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--1", "lemma-stability--3", "lemma-stability--5", "lemma-stability--7", "lemma-stability--8", "proposition-topos-functoriality--1", "proposition-topos-functoriality--2", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2", "theorem-classical-sheaves-essential-image--1"]
+++
Write the group as $\nu_X^*G_0$. We may work on an affine open of $X$.
Using Theorem [theorem-pro-etale-refinements-weakly-etale] and finite affine
refinements, we refine a trivializing covering to a single faithfully
flat ind-étale affine $U\to X$, and we write $U=\varprojlim_iU_i$ with
$U_i$ affine étale over $X$. A trivialization over $U$ determines a
transition element in $\nu_X^*G_0(U\times_XU)$. By continuity for affine
limits it descends to $G_0(U_i\times_XU_i)$ for some $i$, and the cocycle
identity on the triple product holds after enlarging $i$. Since
$U\to X$ is surjective, each $U_i\to X$ is an étale covering. Gluing the
trivial torsor along this cocycle, we get an étale torsor whose
pullback is isomorphic to the given torsor. Hence the given torsor is
classical by Theorem [theorem-classical-sheaves-essential-image], and it is trivialized by
the étale covering $U_i\to X$. See [Stacks, [099X](https://stacks.math.columbia.edu/tag/099X)].

*Source:* the proof of Lemma [lemma-torsors-under-classical-groups].
