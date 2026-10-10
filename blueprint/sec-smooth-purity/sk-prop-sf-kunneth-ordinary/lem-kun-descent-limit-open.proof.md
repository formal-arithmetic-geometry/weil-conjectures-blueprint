+++
kind  = "proof"
of    = "lem-kun-descent-limit-open"
+++
An inverse limit of affine schemes with affine transition morphisms is
affine, with coordinate ring the filtered colimit of the coordinate rings,
and the transition maps of the limit are the maps
$\Spec(A)\to\Spec(A_i)$ induced by the structural maps
$A_i\to A$; moreover
$p_i^{-1}(D(g))=D(p_i^\sharp(g))$ for $g\in A_i$.

A quasi-compact open subscheme of the affine scheme $X=\Spec(A)$ is the
complement of the zero set of a finitely generated ideal: there are
$f_1,\dots,f_n\in A$ with

$$
U=D(f_1)\cup\cdots\cup D(f_n)=D(f_1,\dots,f_n).
$$

Each $f_j$ is the image of an element of some $A_i$, and because the
index system is directed and filtered, the finitely many elements
$f_1,\dots,f_n$ all come from a common index: there are $i$ and
$g_1,\dots,g_n\in A_i$ with $p_i^\sharp(g_j)=f_j$ for all $j$. Put
$U_i=D(g_1,\dots,g_n)\subseteq X_i$, a quasi-compact open subscheme.
Then

$$
p_i^{-1}(U_i)=D(p_i^\sharp(g_1),\dots,p_i^\sharp(g_n))
=D(f_1,\dots,f_n)=U,
$$

which is the assertion.
