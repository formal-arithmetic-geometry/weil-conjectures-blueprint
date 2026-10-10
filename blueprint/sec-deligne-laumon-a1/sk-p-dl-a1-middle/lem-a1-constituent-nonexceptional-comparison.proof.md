+++
kind  = "proof"
of    = "lem-a1-constituent-nonexceptional-comparison"
+++
First translate [def-fd-nonexceptional] into a condition on $U$.
Over $k$, the middle extension of [def-wf-middle-extension]
satisfies $j^*j_*\mathcal M=\mathcal M$. Conversely, if $\mathcal L$ is a
lisse sheaf on $\mathbf A^1_k$ (a constant sheaf, or some
$\mathcal L_{\psi(ax)}$), then $j_*(\mathcal L|_U)=\mathcal L$, because
the stalks of the ordinary direct image at the missing points are the
inertia invariants, and inertia acts trivially on a sheaf that is lisse
there. Geometrically, a constant Weil twist of
[def-wf-constant-weil-twist] becomes the constant sheaf. Hence
$j_*\mathcal M$ is Fourier-exceptional exactly when
$\mathcal M_{\bar k}$ is a constant sheaf or is isomorphic to
$\mathcal L_{\psi(ax)}|_U$ for some $a$.

(1) Suppose $j_*\mathcal M$ is Fourier-exceptional. If
$\mathcal M_{\bar k}$ is constant, it is nonzero, and every geometric
irreducible constituent is the trivial rank-one sheaf
$\mathcal L_{\psi(0\cdot x)}|_U$. If
$\mathcal M_{\bar k}\cong\mathcal L_{\psi(ax)}|_U$, this rank-one sheaf
is its only geometric constituent. In both cases $\mathcal M$ is not
constituent-nonexceptional.

(2) If the geometric fundamental representation $V$ is irreducible,
then $V$ is the only geometric irreducible constituent. If it is
isomorphic to $\mathcal L_{\psi(ax)}|_U$, then
$\mathcal M_{\bar k}\cong\mathcal L_{\psi(ax)}|_U$. For $a=0$ this sheaf
is constant, and for $a\ne0$ it is an Artin–Schreier restriction. In
either case $j_*\mathcal M$ is Fourier-exceptional by the translation
above.

Without geometric irreducibility, the converse of (1) is not asserted.
Fourier-nonexceptionality looks at the whole geometric sheaf, while
constituent-nonexceptionality looks at each geometric constituent.
