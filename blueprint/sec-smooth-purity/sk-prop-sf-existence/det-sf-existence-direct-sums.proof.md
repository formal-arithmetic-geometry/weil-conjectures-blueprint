+++
kind = "proof"
of = "det-sf-existence-direct-sums"
uses = ["det-sf-existence-brown", "det-sf-comp-coherence-single"]
+++
Let $G\in\Dctf(X,\Lambda)$ be one of the compact generators and $n\in\mathbf Z$.
Since $G[n]$ is compact in $\Loc(\Dctf(X,\Lambda))$,
$\Hom(G[n],\bigoplus_\alpha f^!N_\alpha)=\bigoplus_\alpha\Hom(G[n],f^!N_\alpha)
=\bigoplus_\alpha\Hom(Rf_!G[n],N_\alpha)$ by adjunction. On the other side,
$\Hom(G[n],f^!\bigoplus_\alpha N_\alpha)=\Hom(Rf_!G[n],\bigoplus_\alpha N_\alpha)$,
and $Rf_!G[n]$ lies in $\Dctf(Y,\Lambda)$ ([det-sf-comp-coherence-single]),
whose objects are compact in $\Loc(\Dctf(Y,\Lambda))$, so this group is
$\bigoplus_\alpha\Hom(Rf_!G[n],N_\alpha)$. The canonical map induces the identity
between these descriptions (both are induced by the inclusions of the
summands). Let $C$ be a cone of the canonical map; the long exact
$\Hom(G[n],-)$-sequences show $\Hom(G[n],C)=0$ for all generators $G$ and all
$n$. The objects $M$ with $\Hom(M[n],C)=0$ for all $n$ form a localizing
subcategory containing $\Dctf(X,\Lambda)$, hence containing $C$; so
$\mathrm{id}_C=0$, $C=0$, and the canonical map is an isomorphism.
