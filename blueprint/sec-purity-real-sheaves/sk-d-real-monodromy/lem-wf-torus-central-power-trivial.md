+++
id = "lem-wf-torus-central-power-trivial"
kind = "lemma"
title = "A power of the Frobenius acts trivially on the central torus"
order = 2850
uses = ["def-wf-algebraic-character", "def-wf-algebraic-representations", "def-wf-algebraic-torus", "def-wf-arithmetic-monodromy-extension", "def-wf-monodromy-data", "def-wf-semisimple-module", "lem-wf-central-torus-weight-decomposition", "lem-wf-reductive-connected-centre", "lem-wf-weight-lattice-generates"]
+++
In the setting of [def-wf-monodromy-data], let
$H=H_{\mathrm{geom}}$ be connected, and suppose that $V$ is a
faithful semisimple $H$-module.
Put $T=Z(H)^\circ$, a torus by
[lem-wf-reductive-connected-centre], and let
$\zeta=\rho(s)$ for a degree-one element $s\in W(X_0)$.
Then there is $m\ge1$ with

$$
\operatorname{Int}(\zeta^m)|_T=\mathrm{id}_T .
$$

## Proof

Let $\Lambda\subseteq X^*(T)$ be the set of $T$-weights of the
faithful module $V$, finite by
[lem-wf-central-torus-weight-decomposition] and generating
$X^*(T)$ by [lem-wf-weight-lattice-generates]. Conjugation by
$\zeta$ preserves $H$ and hence the characteristic subgroup
$T=Z(H)^\circ$. For $v\in V_\lambda$ and $t\in T$,

$$
t\cdot(\zeta v)=\zeta\cdot\bigl((\zeta^{-1}t\zeta)v\bigr)
=\lambda\bigl(\operatorname{Int}(\zeta^{-1})t\bigr)\,(\zeta v),
$$

so $\zeta\cdot V_\lambda=V_{\theta(\lambda)}$ with
$\theta(\lambda):=\lambda\circ\operatorname{Int}(\zeta^{-1})$, the
twist of [def-wf-arithmetic-monodromy-extension]. Hence $\theta$
is a permutation of the finite set $\Lambda$, so
$\theta^{|\Lambda|!}=\mathrm{id}_\Lambda$; by
[lem-wf-weight-lattice-generates] this gives
$\theta^{|\Lambda|!}=\mathrm{id}_{X^*(T)}$, i.e.

$$
\lambda\circ\bigl(\operatorname{Int}(\zeta^{-|\Lambda|!})|_T\bigr)
=\lambda\qquad\text{for every }\lambda\in X^*(T),
$$

By [def-wf-algebraic-character], [def-wf-algebraic-torus], the
coordinate characters of a split torus separate its points; therefore
$\operatorname{Int}(\zeta^{|\Lambda|!})|_T=\mathrm{id}_T$.
Take $m=|\Lambda|!$ (or any multiple).
