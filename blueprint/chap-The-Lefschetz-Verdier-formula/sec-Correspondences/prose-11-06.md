+++
id = "prose-11-06"
kind = "hidden"
title = "Correspondences (1)"
order = 903
+++
As in topology, a pair of maps $c_1,c_2:C\to X$ should act on
$R\Gamma_c(X,K)$ by pulling back along $c_2$ and pushing forward along $c_1$. The pullback $R\Gamma_c(X,K)\to R\Gamma_c(C,c_2^*K)$ exists when $c_2$ is proper. To push forward we then need a map $Rc_{1!}L\to K$, where $L$ is
the complex on $C$ we have arrived at. By the adjunction $Rc_{1!}\dashv c_1^!$ there is
a canonical such map exactly when $L=c_1^!K$, namely the counit. What connects
the two steps is therefore a map $u:c_2^*K\to c_1^!K$. The resulting
endomorphism $T_c(u)$ is defined in Definition [definition-action-correspondence].

With $c_1^*$ in place of $c_1^!$ the second step fails, since there may
be no nonzero map $Rc_{1!}c_1^*K\to K$. For example, for
the inclusion $i$ of a rational point $y$ into a smooth curve $X$,

$$
\operatorname{Hom}(i_*i^*\Lambda_X,\Lambda_X)
=\operatorname{Hom}(\Lambda_y,i^!\Lambda_X)
=\operatorname{Hom}(\Lambda_y,\Lambda_y(-1)[-2])=0,
$$

so the only map $Ri_!i^*\Lambda_X\to\Lambda_X$ is zero. When $c_1$ is
finite étale, smooth purity gives $c_1^!=c_1^*$, and the counit is
summation over the fibres. Then $T_c(u)$ is pullback along $c_2$
followed by a sum over the fibres of $c_1$, as for a Hecke operator.

The Lefschetz–Verdier formula
(Theorem [theorem-proper-pushforward-lefschetz-verdier]) is stated in this generality.
For the trace formula we apply it to the graph of Frobenius
(Definition [definition-frobenius-correspondences-their-operators]).
