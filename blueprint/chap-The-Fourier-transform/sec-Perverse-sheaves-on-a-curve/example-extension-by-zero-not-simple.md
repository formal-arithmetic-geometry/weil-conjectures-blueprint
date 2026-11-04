+++
id = "example-extension-by-zero-not-simple"
kind = "example"
title = "Extension by zero is not simple"
order = 1251
uses = ["lemma-boundary-stalk", "lemma-largest-punctual-subsheaf"]
+++
Let $j:\mathbf G_m\hookrightarrow\mathbf A^1$ and $i:0\hookrightarrow\mathbf A^1$
be the inclusions over $k$, and put $\delta_0=i_*E$. The sheaf $j_!E$ has no punctual subsheaf, as
its stalk at the origin is zero, so $j_!E[1]$ is perverse. It is not
simple. Rotating the triangle of the exact sequence
$0\to j_!E\to E\to\delta_0\to0$ gives the triangle
$\delta_0\to j_!E[1]\to E[1]\to$. Its three terms are perverse, and
so

$$
0\longrightarrow\delta_0\longrightarrow j_!E[1]
\longrightarrow E[1]\longrightarrow0
$$

is exact in the perverse heart. Among sheaves the skyscraper is a
quotient of $E$; in the perverse heart it becomes a subobject of
$j_!E[1]$. The middle extension of $E|_{\mathbf G_m}$ is $E$ itself
(Lemma [lemma-boundary-stalk]), and $E[1]$ is simple. On the other
hand $(E\oplus\delta_0)[1]$ is not perverse, because $\mathcal H^{-1}$
has the punctual subsheaf $\delta_0$. This is the subsheaf $F_{\rm p}$
of Lemma [lemma-largest-punctual-subsheaf], the kernel of
$E\oplus\delta_0\to j_*j^*(E\oplus\delta_0)=E$.
