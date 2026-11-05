+++
kind = "proof"
of = "lemma-twisting-h-0-1-h--2"
order = 1540004
uses = ["lemma-twisting-h-0-1-h--1", "theorem-riemann-roch-coherent-serre-duality"]
+++
We induct on $t$. If $t=0$, take $\mathcal M_0=\mathcal M$. Otherwise
put $\mathcal F=\mathcal L\otimes\mathcal M_{k'}$ and choose a nonzero
section $s$ of $\mathcal F$. The curve $C_{k'}$ is reduced, so the
nonvanishing locus of $s$ is a nonempty open. The points $x_{k'}$ with
$x\in C(k)$ are dense in $C_{k'}$: the projection $C_{k'}\to C$ is
open, its fibre over a $k$-rational point has just one point, and
$C(k)$ is dense in $C$. Thus there is an $x\in C(k)$ at which $s$
does not vanish after base change.

Replace $\mathcal M$ by $\mathcal M(-x)$. By
[lemma-twisting-h-0-1-h--1], this lowers $h^0(\mathcal F)$ by exactly
one. The degree of a twist is

$$
\deg(\mathcal L\otimes\mathcal M_{k'})
=\deg\mathcal L+\deg\mathcal M,
$$

and $\deg\mathcal O_C(-x)=-1$. Since
$\deg\mathcal F=\chi(C_{k'},\mathcal F)-\chi(C_{k'},\mathcal O_{C_{k'}})$,
the Euler characteristic also drops by one. The identity
$\chi=h^0-h^1$ therefore shows that $h^1$ remains zero. The induction
hypothesis applies to the new twist, which is still defined over $k$.

For the application to the main lemma, $C$ is connected. Choose
$x\in C(k)$; the invertible sheaf $\mathcal O_C(x)$ has degree one.
Write $g'=h^1(C_{k'},\mathcal O_{C_{k'}})$ and set

$$
n=\max\{0,2g'-\deg\mathcal L\},\qquad
\mathcal M=\mathcal O_C(nx).
$$

Then $\mathcal F=\mathcal L\otimes\mathcal M_{k'}$ has degree at
least $2g'$. We have $H^0(C,\mathcal O_C)=k$, and flat base change
gives $H^0(C_{k'},\mathcal O_{C_{k'}})=k'$. Riemann–Roch and Serre
duality [theorem-riemann-roch-coherent-serre-duality] give
$h^0(\mathcal F)=\deg\mathcal F+1-g'\geq1$ and $h^1(\mathcal F)=0$.
Apply the induction just proved with $t=h^0(\mathcal F)-1$.
Finally, finite-dimensionality identifies $h^1=0$ with $H^1=0$.
