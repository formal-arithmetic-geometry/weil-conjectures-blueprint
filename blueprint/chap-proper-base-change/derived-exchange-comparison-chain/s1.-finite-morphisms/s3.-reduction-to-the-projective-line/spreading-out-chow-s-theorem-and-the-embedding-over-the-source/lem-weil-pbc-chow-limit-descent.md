+++
id = "lem-weil-pbc-chow-limit-descent"
kind = "lemma"
title = "Spreading out to a noetherian base"
order = 1589
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $Y=\operatorname{Spec}A$ be affine and let $f:X\to Y$ be proper *and
locally of finite presentation*. Then there exist a finitely generated
$\mathbf Z$-subalgebra $A_0\subseteq A$ (so $Y_0=\operatorname{Spec}A_0$ is
noetherian, and $Y$ is the limit of the affine schemes $Y_0$ indexed by the
directed set of finitely generated $\mathbf Z$-subalgebras of $A$) and a
proper morphism $X_0\to Y_0$ with

$$
 X=X_0\times_{Y_0}Y.
$$

The assertion is stable under further base change along $A_0\subseteq
A_1\subseteq A$.

**Status.** The hypothesis of local finite presentation is essential and
cannot be dropped: for $A=\mathbf F_p[x_1,x_2,\dots]$, $J=(x_1,x_2,\dots)$ and
$X=\operatorname{Spec}(A/J)\to\operatorname{Spec}A$ the morphism is a closed
immersion, hence proper, but not finitely presented, and a descent
$X=X_0\times_{Y_0}Y$ along a finitely generated $\mathbf Z$-subalgebra $A_0$
would exhibit $X\to Y$ as the base change of a morphism between noetherian
schemes, hence as finitely presented, a contradiction. For the general
finite-type case this blueprint does not assert such a descent; see the status
note at [thm-weil-pbc-chow].

## Proof

Let $\mathcal S$ be the directed set of finitely generated $\mathbf
Z$-subalgebras of $A$; then $A=\operatorname{colim}_{A_0\in\mathcal S}A_0$,
and $Y=\lim_{A_0}Y_0$ with affine transition morphisms. This is the
spreading-out (limit-descent) statement for finitely presented morphisms over
an affine limit, Stacks Project, Limits of Schemes, Tag
[01ZM](https://stacks.math.columbia.edu/tag/01ZM) (Lemma 32.10.1), whose
hypothesis *locally of finite presentation* is exactly the one imposed above;
the reductions quoted there are Tag
[01ZJ](https://stacks.math.columbia.edu/tag/01ZJ) (Proposition 32.9.6) and Tag
[01ZA](https://stacks.math.columbia.edu/tag/01ZA) (Proposition 32.5.4,
absolute noetherian approximation). Concretely, local finite presentation
supplies a cover of $X$ by finitely many affine $\operatorname{Spec}B_j$ with
$B_j$ finitely presented as an $A$-algebra together with finitely many glue
data; all the finitely many elements of $A$ occurring in the generators,
relations and glue data lie in some $A_0\in\mathcal S$, and gluing the
corresponding $A_0$-algebras gives a locally finitely presented $X_0\to Y_0$
with $X=X_0\times_{Y_0}Y$. Properness of $X_0\to Y_0$ is the corresponding
spreading-out statement for properness, also part of Tag 01ZM: a morphism of
finite presentation over a limit of affine schemes is proper if and only if
its base change to some member of the limit system is proper. The earlier
argument instead appealed to the valuative criterion and assumed that a
valuation-theoretic diagram over $Y_0$ lifts to $Y$; that step had no
justification and is replaced here. Properness of the base change along
$A_0\subseteq A_1$ is the stability of properness under base change.
