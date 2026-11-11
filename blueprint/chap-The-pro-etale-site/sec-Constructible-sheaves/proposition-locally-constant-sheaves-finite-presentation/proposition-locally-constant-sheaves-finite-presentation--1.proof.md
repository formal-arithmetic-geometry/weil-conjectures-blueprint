+++
kind = "proof"
of = "proposition-locally-constant-sheaves-finite-presentation--1"
order = 146002
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "proposition-pro-etale-coverings--2", "proposition-comparison-morphism-inverse-image--1", "theorem-classical-sheaves-essential-image--1", "proposition-locally-constant-sheaves-finite-presentation--2"]
+++
A locally constant sheaf with model $M$ is the same as a torsor under the
automorphism sheaf of the constant sheaf $\underline M$, so the
proposition follows from the lemma once we know that this automorphism
sheaf is classical.

Decompose $X$ into the open pieces on which the constant model has a
fixed isomorphism type, and fix a finitely presented module $M$. A
presentation $\Lambda^m\to\Lambda^n\to M\to0$ identifies the internal
endomorphism sheaf of $\underline M$ with the kernel of
$\underline M^{\,n}\to\underline M^{\,m}$. Since the constant sheaf
functor is exact, this kernel is the constant sheaf on
$\operatorname{End}_\Lambda(M)$, and so the automorphism sheaf of
$\underline M$ is the constant discrete group
$\operatorname{Aut}_\Lambda(M)$. Hence
$\mathit{Isom}(\underline M,F)$ is a torsor under this classical group,
and by Lemma [lemma-torsors-under-classical-groups] it has sections étale locally.
Since $F$ is obtained from this torsor by twisting $\underline M$, it is
the pullback of the corresponding twist of the constant étale sheaf,
and so it is classical. This is the descent argument of [Stacks, [099Y](https://stacks.math.columbia.edu/tag/099Y)].

*Source:* the proof of Proposition [proposition-locally-constant-sheaves-finite-presentation].
