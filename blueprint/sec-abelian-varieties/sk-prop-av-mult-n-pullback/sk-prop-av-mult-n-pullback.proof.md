+++
kind  = "proof"
of    = "sk-prop-av-mult-n-pullback"
uses = ["sk-prop-av-rigidity", "sk-prop-av-cube"]
+++
An abelian variety is geometrically integral: it is geometrically
reduced because it is smooth, and geometrically irreducible because the
identity component of a group scheme over a field is geometrically
irreducible (Stacks [0B7R](https://stacks.math.columbia.edu/tag/0B7R)) and $A$ is connected.

For commutativity, consider $h:A\times A\to A$,
$h(x,y)=xyx^{-1}y^{-1}$. It maps $A\times\{e\}$ to $e$, so by
[sk-prop-av-rigidity], applied with the first factor as the
proper one, there are an open $V\ni e$ and $g:V\to A$ with
$h|_{A\times V}=g\circ\operatorname{pr}_2$. Composing with
$(e,\operatorname{id}):V\to A\times V$ gives $g=h(e,-)=e$, so $h=e$ on
$A\times V$. The scheme $A\times A$ is smooth, hence reduced, and
irreducible, so the nonempty open $A\times V$ is scheme-theoretically
dense; as $A$ is separated, $h=e$ everywhere (Stacks [056D](https://stacks.math.columbia.edu/tag/056D), [01RH](https://stacks.math.columbia.edu/tag/01RH)).
From now on we write the group law additively.

Every group scheme of finite type over a field is quasi-projective
(Stacks [0BF7](https://stacks.math.columbia.edu/tag/0BF7)); we do not reproduce this argument, which constructs an
ample divisor from the complement of an affine open. A quasi-projective
proper scheme is projective (Stacks [0B45](https://stacks.math.columbia.edu/tag/0B45)). If $\mathcal L$ is ample, then
$\mathcal N=\mathcal L\otimes[-1]^*\mathcal L$ is symmetric and ample.

For every invertible sheaf $\mathcal L$ on $A$, ample or not, consider
on $A\times A\times A$ the invertible sheaf

$$
 \mathcal M=m_{123}^*\mathcal L\otimes m_{12}^*\mathcal L^{-1}\otimes
 m_{13}^*\mathcal L^{-1}\otimes m_{23}^*\mathcal L^{-1}\otimes
 p_1^*\mathcal L\otimes p_2^*\mathcal L\otimes p_3^*\mathcal L,
$$

where the $p_i$ are the projections and $m_{12}$, $m_{13}$, $m_{23}$,
$m_{123}$ are the sums of the indicated coordinates. On
$e\times A\times A$, with coordinates $(x_2,x_3)$, the seven factors
restrict to $\mathcal L$ pulled back along $x_2+x_3$, $x_2$, $x_3$,
$x_2+x_3$, the constant map $e$, $x_2$ and $x_3$, with exponents
$1,-1,-1,-1,1,1,1$; the pullback along the constant map is trivial, and
the others cancel. The same holds on $A\times e\times A$ and
$A\times A\times e$, so $\mathcal M$ is trivial by
[sk-prop-av-cube]. We claim that

$$
 [n]^*\mathcal L\simeq
 \mathcal L^{\otimes n(n+1)/2}\otimes
 ([-1]^*\mathcal L)^{\otimes n(n-1)/2}.
$$

Pulling the trivial sheaf $\mathcal M$ back along
$x\mapsto(x,x,[n-1]x)$ for $n\ge0$ yields

$$
 [n+1]^*\mathcal L\otimes\mathcal L^{\otimes2}
       \otimes[n-1]^*\mathcal L
 \simeq [2]^*\mathcal L\otimes([n]^*\mathcal L)^{\otimes2}.
$$

For $n=0$, since $[0]^*\mathcal L$ is trivial, this gives the case $n=2$
of the claim, and then the formula follows by induction on $n$
(Stacks [0BFF](https://stacks.math.columbia.edu/tag/0BFF)).
For symmetric $\mathcal N$ the two exponents add up to $n^2$.
