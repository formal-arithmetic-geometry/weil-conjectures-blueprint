+++
id = "det-pe-finite-local-systems-hom"
kind = "lemma"
title = "Hom sheaves out of a finitely presented constant sheaf"
uses = ["sk-prop-pe-comparison-morphism", "det-pe-classical-sheaves-modules"]
+++
Let $\Lambda$ be a discrete commutative ring and $X$ a scheme. For a
$\Lambda$-module $M$ write $\underline M=\nu_X^*M_{X,\Et}$ for its constant sheaf
on $X_{\Proet}$, where $M_{X,\Et}$ is the constant étale sheaf. Let
$\Lambda^m\xrightarrow{a}\Lambda^n\to M\to0$ be a finite presentation.

1. For every $\Lambda_X$-module sheaf $N$ on $X_{\Proet}$ there is a natural
   isomorphism $\mathcal Hom_{\Lambda_X}(\underline M,N)\cong
   \ker\bigl(a^{\mathsf T}\colon N^n\to N^m\bigr)$.
2. For $M,M'$ finitely presented,
   $\mathcal Hom_{\Lambda_X}(\underline M,\underline{M'})\cong
   \underline{\Hom_\Lambda(M,M')}$, compatibly with composition.
3. $\mathcal Aut_{\Lambda_X}(\underline M)\cong\nu_X^*\bigl(\operatorname{Aut}_\Lambda(M)_{X,\Et}\bigr)$
   as sheaves of groups; in particular it is a classical sheaf of groups.
