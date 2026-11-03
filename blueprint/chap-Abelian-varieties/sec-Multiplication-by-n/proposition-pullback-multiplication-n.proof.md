+++
kind = "proof"
of = "proposition-pullback-multiplication-n"
order = 1495
+++
The idea is to produce one
trivial sheaf $\mathcal M$ on $A\times A\times A$ by the theorem of the
cube, and to pull it back
along maps $A\to A\times A\times A$ chosen so that the result is a
relation between $[n+1]^*\mathcal L$, $[n]^*\mathcal L$ and
$[n-1]^*\mathcal L$. The theorem of the cube applies because $A$ is
geometrically integral (Lemma [lemma-abelian-variety-commutative]).

Consider
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
$1,-1,-1,-1,1,1,1$. The pullback along the constant map is trivial, and
the others cancel. The same holds on $A\times e\times A$ and
$A\times A\times e$. Hence $\mathcal M$ is trivial by
Theorem [theorem-theorem-cube]. Pulling the trivial sheaf $\mathcal M$ back along
$x\mapsto(x,x,[n-1]x)$ for $n\ge0$ yields

$$
[n+1]^*\mathcal L\otimes\mathcal L^{\otimes2}
\otimes[n-1]^*\mathcal L
\simeq [2]^*\mathcal L\otimes([n]^*\mathcal L)^{\otimes2}.
$$

To see this, note that the composites of $x\mapsto(x,x,[n-1]x)$ with
$m_{123}$, $m_{12}$, $m_{13}$, $m_{23}$, $p_1$, $p_2$, $p_3$ are
$[n+1]$, $[2]$, $[n]$, $[n]$, $\mathrm{id}$, $\mathrm{id}$, $[n-1]$.
The cases $n=0$ and $n=1$ of the formula are clear. For $n=0$, since
$[0]^*\mathcal L$ is trivial, the relation reads
$\mathcal L^{\otimes3}\otimes[-1]^*\mathcal L\simeq[2]^*\mathcal L$.
This is the case $n=2$ of the formula. In general, the relation
expresses $[n+1]^*\mathcal L$ in terms of $[n]^*\mathcal L$ and
$[n-1]^*\mathcal L$, and the exponents in the formula satisfy the same
second order recursion. The formula therefore follows by induction on
$n$ [Stacks, [0BFF](https://stacks.math.columbia.edu/tag/0BFF)].
For symmetric $\mathcal N$ the two exponents add up to $n^2$.
