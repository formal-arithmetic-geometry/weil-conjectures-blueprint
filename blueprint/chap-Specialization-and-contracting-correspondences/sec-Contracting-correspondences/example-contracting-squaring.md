+++
id = "example-contracting-squaring"
kind = "example"
title = "Squaring on the line"
order = 1693
+++
Let $X=C=\mathbf A^1=\operatorname{Spec}k[x]$, let $Z$ be the origin,
with $I=(x)$, and let $c_1=\mathrm{id}$ and $c_2(x)=x^2$, so that
$c_2^*x=x^2$. Then $I_1=(x)$ and $I_2=(x^2)=I_1^2$, so $c$ contracts
towards $Z$ with $n=1$. The fixed scheme is $V(x^2-x)$. It consists of
the two reduced points $0$ and $1$, and only the first meets $Z$.

The deformation to the normal cone is
$\operatorname{Spec}k[t]_{(t)}[x,x/t]$. This is the constant family
$\mathbf A^1_T$ in the coordinate $x'=x/t$. In this coordinate the first
leg is the identity and the second is $x'\mapsto x^2/t=tx'^2$. On the
special fibre $t=0$ the second leg is the constant map to $0$, as (2) of
the lemma predicts, and the deformed fixed scheme there is the point
$x'=0$. On the generic fibre there are two fixed points. One is $x'=0$,
the constant family of the origin. The other is $x'=1/t$, the point
$x=1$. It leaves every bounded region of the $x'$-line as $t\to0$, and
so it does not reach the special fibre.

Corollary [corollary-contracting-local-terms-point] below therefore
gives $\operatorname{LT}_0(u)=\operatorname{tr}_A(u_{\bar 0}\mid K_{\bar
0})$ for every $K$ and $u$. For instance, the local term is zero if
$K=j_!A$ with $j:\mathbf G_m\hookrightarrow\mathbf A^1$, as
$K_{\bar 0}=0$. The condition fails for the identity correspondence.
There $I_2=I_1$, the inclusion $I_1^n\subset I_1^{n+1}$ is false for
every $n$, and the fixed scheme is all of $X$.
