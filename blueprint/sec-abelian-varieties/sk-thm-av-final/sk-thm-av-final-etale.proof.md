+++
kind  = "proof"
of    = "det-av-final-etale"
+++
(1) Let $m:B\times B\to B$ be the group law. Identify
$T_{(e,e)}(B\times B)=T_eB\oplus T_eB$. Since $m(x,e)=x=m(e,x)$, the
differential $dm_{(e,e)}$ restricts to the identity on each summand, so
$dm_{(e,e)}(v,w)=v+w$. Now $[n]=m\circ([n-1]\times\mathrm{id})\circ\Delta$
for $n\ge2$, and $d\Delta_e(v)=(v,v)$; by induction
$d[n]_e(v)=d[n-1]_e(v)+v=nv$, starting from $[1]=\mathrm{id}$. As $n$ is a
unit in $k$, multiplication by $n$ is invertible on the $k$-vector space
$T_eB$.

(2) Work over $\bar k$. For $x\in B(\bar k)$ let $\tau_x$ denote
translation by $x$, an automorphism of $B_{\bar k}$. Since $[n]$ is a
homomorphism ([sk-prop-av-mult-hom]; $B$ is commutative),
$[n]\circ\tau_x=\tau_{nx}\circ[n]$. Differentiating at $e$ gives
$d[n]_x\circ d(\tau_x)_e=d(\tau_{nx})_e\circ d[n]_e$, and the
differentials of translations are isomorphisms, so $d[n]_x$ is an
isomorphism by (1).

(3) $B$ is smooth of dimension $g$ over $k$, and $[n]$ is a morphism of
smooth $k$-varieties of the same dimension. By (2), for every closed point
$x$ of $B_{\bar k}$ the map $[n]^*\Omega^1_{B}\to\Omega^1_{B}$ is an
isomorphism on fibres at $x$ (it is dual to $d[n]_x$). Both sheaves are
locally free of rank $g$, so the map is an isomorphism near every closed
point of $B_{\bar k}$, hence everywhere, hence over $k$ by faithfully flat
descent; thus $\Omega^1_{B/B}=0$ for the source over the target, i.e.
$[n]$ is unramified. It is flat: it is finite and surjective
([sk-prop-av-mult-finite], [sk-prop-av-mult-surjective]) between regular
schemes of the same dimension (miracle flatness), or directly by
[sk-prop-av-isogeny]. Flat, unramified and of finite presentation means
étale. Étale morphisms are stable under base change, so the fibre
$B[n]=[n]^{-1}(e)=B\times_{[n],B,e}\Spec k$ is étale over $k$; it is
finite of rank $\deg[n]$, the rank of the finite locally free
$[n]_*\cO_B$.
