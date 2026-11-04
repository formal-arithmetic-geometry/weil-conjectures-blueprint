+++
kind = "proof"
of = "lemma-sp-reduction"
order = 763
uses = ["lemma-flat-models-generators", "proposition-adjunction-projective-line", "proposition-exceptional-inverse-image-smooth-morphism", "proposition-six-operations-change-coefficients"]
+++
The comparison $b$ for $Rf_!$ is a direct computation, and $c_{A,B}$ is
then determined by the adjunction. To see that $c_{A,B}$ is invertible we
use the explicit form of $f^!$ on a chart, where it is an ordinary inverse
image.

The map $b$ is the change of coefficients for $Rf_!$ (Proposition [proposition-six-operations-change-coefficients]).
Extension by zero commutes with $-\otimes^{\mathbf L}_AB$. For $R\bar f_*$ we resolve
$B$ by finite free $A$-modules and use the flat models of Lemma [lemma-flat-models-generators].
The comparison holds on each free term, being a finite direct sum. Since
$R\bar f_*$ has finite cohomological dimension, only finitely many terms of
the resolution contribute in each degree, and so the comparison holds for every $B$.
We define $c_{A,B}(K)$ as the transpose of the right-hand side of (9.16).
Whether it is an isomorphism is a local question, so we may restrict to a chart
$f|_U=p_d\circ e$ of Proposition [proposition-exceptional-inverse-image-smooth-morphism](1). There the counit is built from
the trace of the projective line and sums over the fibres of $e$, which commute with
extension of coefficients (Proposition [proposition-adjunction-projective-line]).
On the chart, therefore, $c_{A,B}(K)$ is the transpose of the comparison
for pullback $(e^*p_d^*K(d)[2d])_B\simeq e^*p_d^*(K_B)(d)[2d]$, which is an
isomorphism. Hence $c_{A,B}(K)$ is an isomorphism on every chart.
Transitivity holds
because both sides have the same transpose: for $A\to B\to C$, the counit
identity (9.16) for $A\to C$ is obtained by applying the
one for $B\to C$ after the one for $A\to B$.
