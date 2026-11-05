+++
kind  = "proof"
of    = "lemma-constructible-hom-constant-locally"
+++
By the adjunction between constant sheaves and global sections,
$\Hom(M_X,N_X)=\Hom_\Lambda(M,\Gamma(X,N_X))$. A global section of $N_X$
over $X$ is, on an étale cover, a section of the constant presheaf, that
is, an element of $N$; hence, on an étale cover $(U_i\to X)_i$ obtained by
intersecting the covering sieves for the finitely many sections $\varphi(m)$,
$m\in M$, every $\varphi(m)$ is the constant section $n_{i,m}$ over $U_i$.
Over a nonempty $U_i$ the map $N\to\Gamma(U_i,N_X)$ is injective (a
section of the constant presheaf which becomes zero in the sheafification
vanishes on a covering sieve, whose members are nonempty), so
$m\mapsto n_{i,m}$ is $\Lambda$-linear, giving $f_i\colon M\to N$ with
$\varphi|_{U_i}$ the morphism of constant sheaves induced by $f_i$ (both
morphisms out of the constant sheaf $M_{U_i}$ have the same adjoint
$M\to\Gamma(U_i,N_X)$; here one uses that the restriction of a constant
sheaf to $\et{U_i}$ is the constant sheaf, compatibly with the unit maps).
Empty $U_i$ are discarded from the cover.
Since restriction to $\et{U_i}$ is exact and the constant sheaf functor is
exact (a composite of the exact constant presheaf functor and
sheafification), the kernel and cokernel of $\varphi|_{U_i}$ are the
constant sheaves on $\ker f_i$ and $\operatorname{coker}f_i$.
