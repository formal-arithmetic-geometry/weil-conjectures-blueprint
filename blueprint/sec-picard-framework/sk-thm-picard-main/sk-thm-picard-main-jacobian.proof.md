+++
kind  = "proof"
of    = "det-picard-main-jacobian"
+++
(1) By [det-picard-main-degree] (3), $J(C)$ is an open and closed subgroup
scheme; by [det-picard-main-geometry] (3) it is a smooth proper
geometrically connected variety of dimension $g$. The group law is the
tensor product of invertible sheaves, which is commutative. A smooth
proper connected group variety is an abelian variety.

(2) A $k$-point is a class in $\operatorname{Pic}_{C/k}(\Spec k)$, which by
rigidification along $P$ (and $\operatorname{Pic}(\Spec k)=0$) is
$\operatorname{Pic}(C)$; those in $J(C)$ are the classes of degree $0$
([det-picard-main-degree] (2)).

(3) Let $k[\epsilon]=k[x]/(x^2)$ and $C[\epsilon]=C\times_k\Spec k[\epsilon]$,
which has the same underlying space as $C$. The tangent space at $0$ is
the kernel of $J(C)(k[\epsilon])\to J(C)(k)$; since the point
$\Spec k[\epsilon]$ is connected and $J(C)$ is open and closed, this equals
the kernel of $\underline{\operatorname{Pic}}_{C/k}(k[\epsilon])\to\underline{\operatorname{Pic}}_{C/k}(k)$,
i.e. (as $\operatorname{Pic}(\Spec k[\epsilon])=0$, the local ring
$k[\epsilon]$ having trivial Picard group) the kernel of
$\operatorname{Pic}(C[\epsilon])\to\operatorname{Pic}(C)$. On $|C|$ there
is an exact sequence of abelian sheaves

$$
0\longrightarrow\cO_C\xrightarrow{\ a\mapsto1+\epsilon a\ }\cO_{C[\epsilon]}^\times\longrightarrow\cO_C^\times\longrightarrow1
$$

($u+\epsilon v$ is a unit iff $u$ is, and $(1+\epsilon a)(1+\epsilon b)=1+\epsilon(a+b)$).
Its cohomology sequence reads
$H^0(\cO_{C[\epsilon]}^\times)=k[\epsilon]^\times\to H^0(\cO_C^\times)=k^\times\to H^1(C,\cO_C)\to\operatorname{Pic}(C[\epsilon])\to\operatorname{Pic}(C)$,
using $H^0(C,\cO_C)=k$. The first map is surjective, so
$H^1(C,\cO_C)\xrightarrow{\sim}\ker(\operatorname{Pic}(C[\epsilon])\to\operatorname{Pic}(C))$:
concretely a Čech cocycle $(a_{ij})$ goes to the line bundle with
transition functions $1+\epsilon a_{ij}$, and coboundaries correspond to
changes of trivialization. The rigidification along $P$ removes only
scalar automorphisms and does not change this kernel. The bijection is
additive; it is $k$-linear because the $k$-vector space structure on the
tangent space is induced by the endomorphisms $\epsilon\mapsto\lambda\epsilon$
of $k[\epsilon]$, which act on $1+\epsilon a_{ij}$ by
$a_{ij}\mapsto\lambda a_{ij}$.

(4) For a $K$-scheme $T$, $C_K\times_KT=C\times_kT$, so the presheaves
$T\mapsto\operatorname{Pic}(C_T)/\operatorname{Pic}(T)$ of $C/k$ and of
$C_K/K$ agree on $K$-schemes, and the fppf site of $\Spec K$ is the
slice of that of $\Spec k$; hence sheafification commutes with this
restriction, and $\operatorname{Pic}_{C_K/K}$ is the restriction of
$\operatorname{Pic}_{C/k}$ ([def-pc-picard-functor]). A $K$-morphism
$T\to\underline{\operatorname{Pic}}_{C/k}\times_kK$ is the same as a
$k$-morphism $T\to\underline{\operatorname{Pic}}_{C/k}$, so
$\underline{\operatorname{Pic}}_{C/k}\times_kK$ represents
$\operatorname{Pic}_{C_K/K}$. Fibrewise degrees are computed on the same
fibres, so the degree components and in particular the degree-zero
component are compatible with base change.
