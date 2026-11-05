+++
id = "proposition-compactifying-union-two-opens--1"
kind = "proposition"
title = "Properness of the final common modification"
name_showing = false
order = 1458001
aliases = ["bp-r455-1"]
lean = ["AlgebraicGeometry.TwoOpenPreparation.FinalModification.isProper_w", "AlgebraicGeometry.TwoOpenPreparation.FinalModification.compactification"]
uses = ["definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-admissible-blow-up", "lemma-gluing-after-admissible-blow-ups"]
+++
Let $S$ be Noetherian, let $M\to S$ be of finite type, and let
$M_1,M_2\subseteq M$ be opens with dense intersection $D=M_1\cap M_2$.
For $i=1,2$, suppose that $X_i$ is proper over $S$, that
$M_i\subseteq V_i\subseteq X_i$ are open immersions with $M_i$ dense
in $X_i$, and that $\psi_i:V_i\to M$ is a proper $S$-morphism whose
restriction above $M_i$ is the given isomorphism
$\psi_i^{-1}(M_i)=M_i$.

For $\{i,j\}=\{1,2\}$, put

$$
Z_i=M\setminus M_j,\qquad
B_{i,r}=\overline{\psi_i^{-1}(Z_r)}\subseteq X_i.
$$

Assume that $B_{i,1}\cap B_{i,2}=\varnothing$ for $i=1,2$.
Let $X_{12}$ be the scheme-theoretic image of
$V_1\times_M V_2\to X_1\times_S X_2$, with projections $p_i$, and
assume that

$$
p_1^{-1}(B_{1,2})\cap p_2^{-1}(B_{2,1})=\varnothing.
$$

Form $W_i=M\coprod_{M_i}(X_i\setminus B_{i,j})$. Let $W\to S$ be
any common modification of $W_1,W_2$ along $M$ as in
[lemma-gluing-after-admissible-blow-ups]: it is separated of finite
type, covered by open images of $M$-admissible blow-ups
$W_i'\to W_i$ whose copies of $M$ agree in $W$.
Then $W\to S$ is proper, and the induced open immersion $M\to W$
gives a compactification of $M\to S$.
