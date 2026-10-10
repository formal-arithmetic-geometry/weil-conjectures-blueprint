+++
kind  = "proof"
of    = "lem-pc-projective-space-canonical"
+++
Kähler differentials commute with localization, which gives the
canonical isomorphisms used for the gluing; they are compatible on
triple intersections because all of them are the canonical
identifications with the differentials of the common localization
$\Gamma(U_i\cap U_j\cap U_l,\mathcal O_P)$. For the polynomial ring
$R_i$, $\Omega^1_{R_i/A}$ is free with basis $d(x_k/x_i)$, $k\ne i$, so
$\Omega^1_{P/A}$ is locally free of rank $n$, and
$\Lambda^n\Omega^1_{R_i/A}$ is free of rank one with basis $\eta_i$.

Fix $i\ne j$ and write $t_k=x_k/x_j$ ($k\ne j$) for the coordinates of
$U_j$; on $U_i\cap U_j$ the element $t_i$ is a unit, and
$x_j/x_i=t_i^{-1}$, $x_k/x_i=t_k/t_i$ for $k\notin\{i,j\}$. Hence

$$
d(x_j/x_i)=-t_i^{-2}\,dt_i,\qquad
d(x_k/x_i)=t_i^{-1}dt_k-t_kt_i^{-2}\,dt_i\quad(k\notin\{i,j\}).
$$

In the wedge $\bigwedge_{k\ne i}d(x_k/x_i)$ the factor in position $j$
is a multiple of $dt_i$, so the $dt_i$-terms of the other factors
contribute zero ($dt_i\wedge dt_i=0$). The wedge equals
$-t_i^{-2}\cdot t_i^{-(n-1)}$ times the wedge of the $dt_k$, $k\ne j$,
taken in the order of the indices $\{0,\ldots,n\}\smallsetminus\{i\}$
with $dt_i$ in the slot of $j$. Moving $dt_i$ to its increasing
position passes the $|i-j|-1$ factors $dt_k$ with $k$ strictly between
$i$ and $j$, so

$$
\bigwedge_{k\ne i}d(x_k/x_i)=(-1)^{|i-j|}\,t_i^{-(n+1)}
\bigwedge_{k\ne j}dt_k,
\qquad\text{i.e.}\qquad
\eta_i=(-1)^i(-1)^{i+j}(x_i/x_j)^{-(n+1)}(-1)^j\eta_j
=(x_i/x_j)^{-(n+1)}\eta_j .
$$

This is exactly the transition rule
$e_i^{(-n-1)}=(x_i/x_j)^{-n-1}e_j^{(-n-1)}$ of
[def-pc-projective-space-twist]. Hence the isomorphisms
$\omega_P|_{U_i}\to\mathcal O_P(-n-1)|_{U_i}$, $\eta_i\mapsto
e_i^{(-n-1)}$, agree on the overlaps, and they glue to an isomorphism
of $\mathcal O_P$-modules (the sheaf axiom on the cover by the $U_i$;
the glued map is an isomorphism because it is one locally). The
statement on $H^n$ follows from the rank-one basis of
$H^n(P,\mathcal O_P(-n-1))$. For $n=1$: $\eta_0=d(x_1/x_0)=dt$,
$\eta_1=-d(x_0/x_1)=-ds$, and the rule reads
$dt=(x_0/x_1)^{-2}(-ds)=-t^2ds$, in accordance with $s=t^{-1}$.
