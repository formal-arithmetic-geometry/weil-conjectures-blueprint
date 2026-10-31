+++
id = "prose-12-11"
kind = "hidden"
title = "Trace classes and the Lefschetz–Verdier formula"
order = 556
+++
We want to write $\operatorname{tr}(T_c(u))$ as a sum of contributions
from the fixed locus. The first guess, a sum over fixed points of the
traces of $u$ on stalks, does not make sense in general, because the
fixed locus need not be finite. For the identity correspondence of
$\mathbf P^1$ and $K=A$, every point is fixed and the trace on
$R\Gamma(\mathbf P^1,A)=A\oplus A(-1)[-2]$ is $1+1=2$,
the self-intersection of the diagonal. What does make sense is a class
on $\Fix(c)$. By Lemma [sk-thm-sf-kunneth-verdier], $u$ is a section of
$c^!(K\boxtimes\mathbb D_XK)$, and the trace morphism restricts it to a
section of $\omega_{\Fix(c)}$. On a proper piece $B$ such a section can
be integrated: $H^0(B,\omega_B)=\operatorname{Hom}(Ra_{B!}A_B,A)$, and
composing with the unit $A\to Ra_{B*}A_B=Ra_{B!}A_B$, which uses that
$B$ is proper, gives an element of $A$. In the example, $H^0(\mathbf P^1,\omega_{\mathbf P^1}) =H^2(\mathbf P^1,A(1))\simeq A$, and by
Theorem [sk-p-proper], since the degree map
$H^2(\mathbf P^1,A(1))\to A$ is an isomorphism, the trace class is $2$ times the
class of a point. The trace class is additive in $K$
(Proposition [sk-i-additivity]) and compatible with proper
pushforward (Theorem [sk-p-proper]). At an isolated
fixed point the local term can still differ from the trace on the stalk
(Remark [sk-rem-tf-locality-warning]), and for Frobenius the two are
shown to agree in Proposition [sk-p-frob].
