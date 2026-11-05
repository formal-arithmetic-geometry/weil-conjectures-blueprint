+++
id = "prose-11-11"
kind = "hidden"
title = "Trace classes and local terms (1)"
order = 915
+++
We want to write $\operatorname{tr}(T_c(u))$ as a sum of contributions
from the fixed locus. The first guess, a sum over fixed points of the
traces of $u$ on stalks, does not make sense in general, because the
fixed locus need not be finite. For example, for the identity correspondence of $\mathbf P^1$ and $K=A$, every point is fixed. The trace on
$R\Gamma(\mathbf P^1,A)=A\oplus A(-1)[-2]$ is $1+1=2$,
the self-intersection of the diagonal.

What does make sense is a class on $\Fix(c)$. By
Lemma [lemma-external-duality-trace-morphism], $u$ is a section of
$c^!(K\boxtimes\mathbb D_XK)$, and composing with the trace morphism we
obtain a section of $\omega_{\Fix(c)}$. Such a section can be integrated
over a proper piece $B$ of the fixed locus. Indeed,
$H^0(B,\omega_B)=\operatorname{Hom}(Ra_{B!}A_B,A)$, and
$Ra_{B*}A_B=Ra_{B!}A_B$ for proper $B$. Composing with the unit
$A\to Ra_{B*}A_B$ therefore gives an element of $A$. In the example above, $H^0(\mathbf P^1,\omega_{\mathbf P^1})=H^2(\mathbf P^1,A(1))$ and the
degree map $H^2(\mathbf P^1,A(1))\to A$ is an isomorphism, so Theorem [theorem-proper-pushforward-lefschetz-verdier] shows that the trace class is $2$ times the class of a point.

We will see that the trace class is additive in $K$
(Proposition [proposition-additivity-trace-classes]) and compatible with proper
pushforward (Theorem [theorem-proper-pushforward-lefschetz-verdier]). However, at an isolated fixed point the local term can still differ from the trace on the stalk
(Remark [remark-locality-warning]). For Frobenius the two are
shown to agree in Proposition [proposition-frobenius-local-term-curve].
