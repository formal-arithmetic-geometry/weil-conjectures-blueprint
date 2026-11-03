+++
kind  = "proof"
of    = "lem-chow-disjoint-affines"
+++
For $k\neq i$ we have $\eta_i\notin Z_k$: otherwise
$Z_i=\overline{\{\eta_i\}}\subseteq Z_k$, contradicting that $Z_i$ and $Z_k$
are distinct irreducible components. Hence
$\bigcap_{k\neq i}(X\setminus Z_k)$ is an open neighbourhood of $\eta_i$, and
since the affine opens form a basis of the topology we may choose an affine
open $V_i$ with

$$
\eta_i\in V_i\subseteq\bigcap_{k\neq i}(X\setminus Z_k).
$$

In particular $V_i\cap Z_k=\emptyset$, and a fortiori $\eta_k\notin V_i$, for
all $k\neq i$.

Fix $i$ and put $W_i:=\bigcup_{j\neq i}(V_i\cap V_j)$. Each $V_i\cap V_j$ is
quasi-compact because $X$ is quasi-separated, so $W_i$ is a quasi-compact open
subset of $V_i$, and $\eta_i\notin W_i$ because $\eta_i\notin V_j$ for
$j\neq i$. Write $V_i=\Spec R_i$. The irreducible components of the open
subscheme $V_i$ are the nonempty intersections $C\cap V_i$ with $C$ an
irreducible component of $X$, so $Z_i\cap V_i$ is an irreducible component of
$V_i$ with generic point $\eta_i$; equivalently $\eta_i$ corresponds to a
minimal prime $\mathfrak p_i\subseteq R_i$. By 00EV applied to
$R_i$, the minimal prime $\mathfrak p_i$ and the quasi-compact open
$W_i\subseteq\Spec R_i$, there is $f_i\in R_i\setminus\mathfrak p_i$ with
$D(f_i)\cap W_i=\emptyset$. Put $U_i:=D(f_i)$. Then $U_i$ is an affine open
containing $\eta_i$, and for $j\neq i$ we have
$U_i\cap V_j\subseteq V_i\cap V_j\subseteq W_i$, whence
$U_i\cap V_j=\emptyset$ and in particular $U_i\cap U_j=\emptyset$.

Finally, a scheme that is the disjoint union of two affine opens is affine by
01I5; iterating, $U_1\cup\dots\cup U_n$ is affine.
