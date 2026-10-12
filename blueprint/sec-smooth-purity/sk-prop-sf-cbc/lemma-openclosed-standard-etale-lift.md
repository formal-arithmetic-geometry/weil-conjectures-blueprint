+++
id = "lemma-openclosed-standard-etale-lift"
kind = "lemma"
title = "Lifting a standard étale algebra along a quotient"
order = 1874
lean = ["Algebra.IsStandardEtale.exists_algEquiv_quotient_tensor"]
+++
Let $R$ be a commutative ring and $I\subseteq R$ an ideal. Recall that a
*standard étale pair* over a ring $S$ is a pair of polynomials
$(f,g)$ in $S[T]$ with $f$ monic and $g^n\in(f',f)$ for some $n$, and that
its algebra is $S[T][1/g]/(f)$, which is étale over $S$.

Let $(\bar f,\bar g)$ be a standard étale pair over $R/I$. Then there is a
standard étale pair $(F,H)$ over $R$ and an isomorphism of $R/I$-algebras

$$
(R/I)\otimes_R\bigl(R[T][1/H]/(F)\bigr)
\cong(R/I)[T][1/\bar g]/(\bar f).
$$

In words: every standard étale algebra over $R/I$ is the base change of a
standard étale algebra over $R$.
