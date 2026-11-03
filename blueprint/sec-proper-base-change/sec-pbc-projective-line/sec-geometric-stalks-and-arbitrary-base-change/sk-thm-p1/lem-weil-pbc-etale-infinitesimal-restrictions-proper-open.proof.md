+++
kind = "proof"
of = "lem-weil-pbc-etale-infinitesimal-restrictions-proper-open"
uses = ["def-pc-base-change"]
+++
Set $h=f\circ g:X\to\operatorname{Spec}A$. The complement $C=X\setminus W$ is closed, and $h$ is proper, in particular closed, so $h(C)$ is closed in $\operatorname{Spec}A$; write $h(C)=V(K)$ for an ideal $K\subseteq A$. Suppose $x\in C$. Then $K$ is contained in the prime ideal $h(x)$, which is contained in a maximal ideal $\mathfrak m$. Thus $\mathfrak m\in V(K)$, so $\mathfrak m=h(t)$ for some $t\in C$.

Since $A$ is $I$-adically complete, $I$ is contained in the Jacobson radical of $A$, hence $I\subseteq\mathfrak m$. The image of $\operatorname{Spec}(A/I)\to\operatorname{Spec}A$ is $V(I)$, and the image of the projection $Y_0=Y\times_{\operatorname{Spec}A}\operatorname{Spec}(A/I)\to Y$ is $f^{-1}(V(I))$ [def-pc-base-change]. As $f(g(t))=\mathfrak m\in V(I)$, the point $g(t)$ lies in that image. The containment hypothesis puts $t$ in $W$, contradicting $t\in C$. Thus $C=\emptyset$ and $W=X$.
