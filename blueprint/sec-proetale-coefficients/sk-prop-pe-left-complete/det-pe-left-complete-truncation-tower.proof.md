+++
kind = "proof"
of = "det-pe-left-complete-truncation-tower"
+++
*1.* The canonical truncation $\tau_{\geq-n}K$ is the complex
$0\to K^{-n}/\operatorname{im}d^{-n-1}\to K^{-n+1}\to K^{-n+2}\to\cdots$, a quotient of $K$.
Its cohomology is $H^q(K)$ for $q\geq-n$, via the quotient map, and $0$ for $q<-n$. The
transition map is compatible with the quotient maps from $K$, so for $n\geq-q$ it is the
identity of $H^q(K)$ under these identifications, and for $n<-q$ its target is $0$.

*2.* By 1 the tower $(H^q(\tau_{\geq-n}K))_n$ has epimorphic transitions, so
$R^1\varprojlim=0$ by [det-pe-milnor-epimorphic]. Its limit is the limit of a tower that is
constant equal to $H^q(K)$ with identity maps from $n=\max(0,-q)$ on, hence $H^q(K)$, the
identification being induced by the maps $K\to\tau_{\geq-n}K$.
