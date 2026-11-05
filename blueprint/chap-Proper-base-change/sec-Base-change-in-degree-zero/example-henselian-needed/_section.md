+++
id = "example-henselian-needed"
kind = "example"
title = "Why the pair must be henselian"
order = 330
+++
Let $k$ be a field of characteristic $\neq2$ and let
$R=k[t]_{(t)}$, the local ring of $\mathbf A^1_k$ at the origin, with
maximal ideal $J=(t)$. The finite $R$-algebra $B=R[x]/(x^2-1-t)$ is a domain,
because $1+t$ is not a square in $k(t)$. Hence $Z=\operatorname{Spec}B$ is
connected and $\Gamma(Z,\mathbf Z/2)=\mathbf Z/2$. The closed fibre, on the other hand, is
$\operatorname{Spec}k[x]/(x^2-1)$, which consists of the two points
$x=\pm1$, and so $\Gamma(Z_0,\mathbf Z/2)=(\mathbf Z/2)^2$. Thus the
conclusion of the theorem fails for $(R,J)$. The reason is that
$(R,J)$ is not henselian: the factorization $x^2-1=(x-1)(x+1)$ modulo $t$
does not lift. In the henselization, by contrast, and in $k[[t]]$, the element $1+t$
has the square root $1+t/2-t^2/8+\cdots$. There the factorization lifts,
and $Z$ splits into two copies of the base, so both sides become
$(\mathbf Z/2)^2$.
