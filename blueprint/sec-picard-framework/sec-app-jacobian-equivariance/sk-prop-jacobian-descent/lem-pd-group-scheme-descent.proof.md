+++
kind  = "proof"
of    = "lem-pd-group-scheme-descent"
+++
A group scheme structure on $V$ over $X$ is a triple of morphisms
$m:V\times_XV\to V$, $e:X\to V$ and
$i:V\to V$ over $X$ satisfying the group axioms, which are equalities between
morphisms built from $m,e,i$ by composition and projection; this is the
group scheme structure of [def-sc-group-scheme] over the base $X$, and all
fibre products below are the base changes of [def-pc-base-change]. Base
change along $p$ commutes with fibre products, so
$(V_0\times_YV_0)\times_YX=V\times_XV$, and the
[def-pd-descent-datum] on $V$ induces
one on $V\times_XV$; the descent datum on $X$ itself is the trivial one.

*The inverse is compatible as well.* On points, the descent datum transports
a $T$-point $a$ of $V$ lying over $f_1:T\to X$ to a $T$-point of $V$ lying over
$f_2:T\to X$, for any $f_1,f_2$ with $p\circ f_1=p\circ f_2$; this transport is a
bijection between the groups of such points. By hypothesis it respects
products and the unit, so it is a group isomorphism, and hence it also respects
inverses. Thus $i$ is compatible with the descent datum.

*Descent of the structure.* Applying [lem-pd-morphisms-descend] to $m$, to
$e$ and to $i$ produces morphisms $m_0,e_0,i_0$ over $Y$ whose base changes
to $X$ are $m,e,i$. Each group axiom for $(m_0,e_0,i_0)$ asserts the equality of
two morphisms over $Y$ whose base changes to $X$ are the two sides of the
corresponding axiom for $(m,e,i)$; these sides agree, so the two morphisms over
$Y$ are both descents of the same compatible morphism, and they agree by the
uniqueness in [lem-pd-morphisms-descend]. Hence $(m_0,e_0,i_0)$ is a group
scheme structure on $V_0$ over $Y$ whose base change is the given one.
Uniqueness: a second such structure has multiplication, unit and inverse which
are again descents of $m$, $e$ and $i$, so it coincides with
$(m_0,e_0,i_0)$ by the same uniqueness. If $V$ is commutative, $m_0\circ s_0$
and $m_0$ (with $s_0$ the swap of the two factors of $V_0\times_YV_0$) are
descents of $m\circ s=m$, hence equal, so $V_0$ is commutative.
