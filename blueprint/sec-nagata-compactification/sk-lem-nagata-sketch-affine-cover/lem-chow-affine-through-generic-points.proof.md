+++
kind  = "proof"
of    = "lem-chow-affine-through-generic-points"
uses = ["lem-chow-disjoint-affines"]
+++
After renumbering, let $x\in Z_i$ precisely for $i\leq r$, so that $x\notin
Z_k$ for $k>r$.

*Step 1: an affine open $W$ around $x$ avoiding the components not through
$x$.* For $k>r$, the complement $X\setminus Z_k$ is an open neighbourhood of
$x$, hence so is the finite intersection $O:=\bigcap_{k>r}(X\setminus Z_k)$.
Since the affine open subschemes form a basis of the topology, we may choose
an affine open $W$ with $x\in W\subseteq O$; then $W\cap Z_k=\emptyset$ for
$k>r$.

*Step 2: the generic points $\eta_i$, $i\leq r$, lie in $W$.* For $i\leq r$
the intersection $W\cap Z_i$ is nonempty (it contains $x$) and is an open
subset of the irreducible space $Z_i$; every nonempty open subset of an
irreducible space contains its generic point, so $\eta_i\in W\cap Z_i\subseteq
W$.

*Step 3: disjoint affine opens around $\eta_{r+1},\dots,\eta_n$.* Apply
[lem-chow-disjoint-affines] to the components
$Z_{r+1},\dots,Z_n$: for every $k>r$ there is an affine open $V_k\ni\eta_k$
with $V_k\cap Z_l=\emptyset$ for $l>r,\ l\neq k$, and the $V_k$ are pairwise
disjoint.

*Step 4: shrinking the $V_k$ away from $W$.* Let $k>r$. Quasi-separatedness of
$X$ means that the diagonal $X\to X\times_{\mathbf Z}X$ is quasi-compact; the
open $W\cap V_k$ is the base change of the diagonal along $W\times_{\mathbf
Z}V_k\to X\times_{\mathbf Z}X$, so $W\cap V_k\to W\times_{\mathbf Z}V_k$ is
quasi-compact, and the target is affine, whence $W\cap V_k$ is quasi-compact.
Writing $V_k=\operatorname{Spec}R_k$, the point $\eta_k$ corresponds to a
minimal prime $\mathfrak p_k$ of $R_k$: indeed $Z_k\cap V_k$ is an irreducible
component of $V_k$ (otherwise its closure in $X$ would contain a closed
irreducible subset strictly larger than $Z_k$), and it is the closure of
$\{\eta_k\}$, so $\mathfrak p_k$ is a minimal prime. By Algebra, Lemma 10.26.4
(Stacks Project, Tag [00EV](https://stacks.math.columbia.edu/tag/00EV)),
applied to $R:=R_k$, the minimal prime $\mathfrak p_k$, and the quasi-compact
open $W\cap V_k\subseteq\operatorname{Spec}R_k$ which does not contain
$\mathfrak p_k$ (as $W\cap Z_k=\emptyset$), there is $f_k\in
R_k\setminus\mathfrak p_k$ with $D(f_k)\cap(W\cap V_k)=\emptyset$. Put
$V_k':=D(f_k)\subseteq V_k$: this is an affine open containing $\eta_k$ and
disjoint from $W$.

*Step 5: the union.* The opens $W$ and $V_k'$ ($k>r$) are pairwise disjoint
and each is affine, so their union

$$
 U:=W\cup\bigcup_{k>r}V_k'
$$

is affine: by Schemes, Lemma 26.6.8 (Tag
[01I5](https://stacks.math.columbia.edu/tag/01I5)) a disjoint union of two
affine opens is affine, and we iterate. It contains $x$ and all
$\eta_1,\dots,\eta_n$, as required.
