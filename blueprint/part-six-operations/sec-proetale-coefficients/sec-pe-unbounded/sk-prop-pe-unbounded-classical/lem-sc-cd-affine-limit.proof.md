+++
kind  = "proof"
of    = "lem-sc-cd-affine-limit"
+++
Let $p_i:X\to X_i$ and, for $j\geq i$, $p_{ji}:X_j\to X_i$ be the
projection and transition maps, and first let $F$ be killed by a fixed
integer $n>0$. Set $F_i=p_{i*}F$. Since $p_i=p_{ji}\circ p_j$, one has
$F_i=p_{ji*}F_j$, and the transition arrow
$\phi_{ji}:p_{ji}^*F_i\to F_j$ is the map adjoint, under
$p_{ji}^*\dashv p_{ji*}$, to this identification. For $k\geq j\geq i$
the relation $p_{ji}\circ p_{kj}=p_{ki}$ gives
$\phi_{ki}=\phi_{kj}\circ p_{kj}^*\phi_{ji}$, so the pullbacks
$p_j^*\phi_{ji}:p_i^*F_i\to p_j^*F_j$ form a filtered system on $X$, and
the maps $p_i^*F_i\to F$ adjoint to the identity of $F_i=p_{i*}F$ are
compatible with it. This gives the canonical map
$c:\varinjlim_ip_i^*F_i\to F$; we show that it is an isomorphism, testing on
sections over affine etale $U\to X$, which form a basis of the etale site.
By the limit results for schemes of finite presentation
([Stacks, Tag 01ZM]), every such $U$ is $U_i\times_{X_i}X$ for an affine
etale $U_i\to X_i$ at some stage $i$, every morphism between two such
objects descends to a later stage, and a finite etale covering of $U$ by
affines descends to a finite etale covering at a later stage.
*Surjectivity.* A section $s\in F(U)$ is an element of
$F_i(U_i)=F(U_i\times_{X_i}X)=F(U)$, and its image under
$p_i^*F_i\to F$ is $s$. *Injectivity.* A local section of
$\varinjlim_ip_i^*F_i$ over $U$ is, after refining by a finite affine
etale covering, represented by $t\in F_i(W_i)$ for an affine etale
$W_i\to X_i$ together with a morphism $U\to W_i\times_{X_i}X$. Descending
$U$, the covering and this morphism to a stage $j\geq i$, the image of $t$
in $F_j(U_j)=F(U)$ is its image under $c$; if that image vanishes, the
representative vanishes at stage $j$, hence in the colimit. No
constructibility of the $F_i$ is used. These are the same
finite-presentation descent and finite-cover arguments used in
[lemma-weil-pbc-etale-cohomology-continuity].

For each fixed $i$, that theorem gives

$$
H^q(X,p_i^*F_i)=\varinjlim_{j\geq i}
H^q(X_j,p_{ji}^*F_i)=0\quad(q>c).
$$

Now apply [lem-weil-pbc-cohomology-filtered-colimit] to
the preceding sheaf colimit. Finally remove the fixed exponent
using [lemma-weil-pbc-torsion-filtered-union] and the same
commutation of cohomology with filtered colimits.
