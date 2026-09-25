+++
id = "lem-pod-twist-interchange"
kind = "lemma"
title = "Internal Hom with an invertible twist"
order = 2379
uses = ["def-coefficient-twists-detailed", "def-weil-derived-pullback-tensor-hom", "lem-pod-finite-projective-tensor-hom", "prop-pod-perfect-dualizable"]
+++
In the Poincare duality conventions of this chapter (the fixed setting), let $K\in D^b_{ctf}(X,\Lambda)$ be perfect over $\Lambda _X$, let $M\in D^b_{ctf}(X,\Lambda )$, and let $m\in \mathbf Z$. The twist $\Lambda (m)_X$ is an invertible locally constant rank-one sheaf, and the canonical natural map

$$
R\mathcal Hom_X\bigl(K,M\otimes ^L_{\Lambda _X}\Lambda (m)_X\bigr) \xrightarrow {\  \sim \  } R\mathcal Hom_X(K,M)\otimes ^L_{\Lambda _X}\Lambda (m)_X
$$

is an isomorphism. In particular

$$
R\mathcal Hom_X\bigl(K,\Lambda _X(m)[n]\bigr) \xrightarrow {\  \sim \  }K^\vee (m)[n] \qquad (n\in \mathbf Z).
$$

## Proof

Step 1: by [def-coefficient-twists-detailed] each $\Lambda (m)_X$ is an invertible locally constant rank-one sheaf, and

$$
\Lambda (m)_X\otimes ^L_{\Lambda _X}\Lambda (-m)_X\cong \Lambda _X
$$

with the canonical maps, so $T_m=-\otimes ^L_{\Lambda _X}\Lambda (m)_X$ is an exact autoequivalence of $D^b_{ctf}(X,\Lambda )$ with quasi-inverse $T_{-m}$. Step 2: since $T_m$ is an exact functor and carries K-injective objects to K-injective objects (it is an equivalence), it commutes with the derived internal Hom in the following sense: the canonical natural map

$$
T_m\bigl(R\mathcal Hom_X(K,M)\bigr) \longrightarrow R\mathcal Hom_X(K,T_mM)
$$

is the derived version of the pointwise identification of $\mathcal Hom_X$-modules, and both sides are exact functors of $M$ agreeing on $M=\Lambda _X^{\oplus r}$, a generator: for $M=\Lambda _X$, both sides identify with $K^\vee \otimes ^L\Lambda (m)_X$ by the tensor–internal-Hom adjunction of [def-weil-derived-pullback-tensor-hom]. Step 3: by [prop-pod-perfect-dualizable] the derived internal Hom is computed by a bounded complex of finite projective modules when the first variable is perfect, and then the termwise identifications give the map directly: with $P^\bullet \to K$ a bounded complex of finite projective modules,

$$
\mathcal Hom_X^\bullet \bigl(P^\bullet ,I(M)\otimes \Lambda (m)_X\bigr) \cong \mathcal Hom_X^\bullet (P^\bullet ,I(M))\otimes \Lambda (m)_X
$$

termwise by [def-weil-derived-pullback-tensor-hom] (the finite projective modules being dualizable, as in [lem-pod-finite-projective-tensor-hom]), and the differentials are compatible; the identification is independent of the chosen resolutions, again by [def-weil-derived-pullback-tensor-hom]. Step 4: setting $M=\Lambda _X$ and using the shift of the second variable, $R\mathcal Hom_X(K,\Lambda _X(m)[n])=\bigl(R\mathcal Hom_X(K,\Lambda _X)\bigr)(m)[n] =K^\vee (m)[n]$, by the definition of $K^\vee (m)$ from the twist $K^\vee (m)=K^\vee \otimes ^L\Lambda (m)_X$ of [def-coefficient-twists-detailed] and the shift axiom of the derived functor of [def-weil-derived-pullback-tensor-hom].
