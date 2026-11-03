+++
kind  = "proof"
of    = "lemma-weil-pbc-pushout-monicity"
+++
The pushout $P=B\amalg_AC$ is the cokernel of
$(i_B,-i_C):A\to B\oplus C$, and the map $C\to P$ is the composite of the
inclusion $C\to B\oplus C$ with the cokernel map. Its kernel is therefore the
pullback of the image of $(i_B,-i_C)$ along $C\to B\oplus C$. If
$x:K\to C$ factors through this pullback, then, after replacing $K$ by an
epimorphic cover, $(0,x)=(i_B,-i_C)\circ a$ for some $a:K\to A$; so
$i_B\circ a=0$, hence $a=0$ since $i_B$ is monic, and $x=-i_C\circ a=0$.
Thus the kernel is zero and $C\to P$ is a monomorphism. (For sheaves this is
the familiar local computation: a section of $C$ dying in $P$ is locally the
image of a section of $A$ killed by $i_B$, hence locally zero, hence zero.)
